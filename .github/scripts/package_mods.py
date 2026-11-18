"""Validate MO2 metadata and build one installable ZIP per crispy_ folder."""
import argparse
import configparser
from pathlib import Path
import re
import zipfile

REPOSITORY_URL = "https://github.com/SBDG-0/crispy_stalker_anomaly"


def validate(mod):
    metadata = configparser.ConfigParser(interpolation=None)
    with (mod / "meta.ini").open(encoding="utf-8-sig") as source:
        metadata.read_file(source)
    general = metadata["General"]
    expected = {"url": REPOSITORY_URL, "hasCustomURL": "true",
                "installationFile": f"{mod.name}.zip"}
    for key, value in expected.items():
        if general.get(key) != value:
            raise ValueError(f"{mod.name}: {key} must be {value!r}")
    version = general.get("version", "")
    if not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", version):
        raise ValueError(f"{mod.name}: version must use MAJOR.MINOR.PATCH")
    readme = (mod / "README.md").read_text(encoding="utf-8-sig")
    if re.findall(r"(?m)^\*\*Version:\*\* `([^`]+)`\s*$", readme) != [version]:
        raise ValueError(f"{mod.name}: README version must match meta.ini ({version})")
    if not (mod / "gamedata").is_dir():
        raise ValueError(f"{mod.name}: missing gamedata folder")
    payload = [mod / "meta.ini"]
    for path in sorted((mod / "gamedata").rglob("*")):
        if path.is_symlink():
            raise ValueError(f"{mod.name}: symlinks are not supported: {path}")
        if path.is_file() and path.name.lower() != "readme.md":
            payload.append(path)
    if len(payload) == 1:
        raise ValueError(f"{mod.name}: gamedata has no payload files")
    return payload


def description(mod):
    readme = mod / "README.md"
    if readme.is_file():
        section = False
        for line in readme.read_text(encoding="utf-8-sig").splitlines():
            if re.fullmatch(r"#+\s+Description\s*", line, re.IGNORECASE):
                section = True
            elif section and line.startswith("#"):
                break
            elif section and line.strip():
                return line.strip()
    return "No description provided."


def build(root, output):
    mods = sorted(path for path in root.glob("crispy_*") if path.is_dir())
    if not mods:
        raise ValueError("No crispy_ mod folders found")
    # Validate every mod before producing any archives.
    payloads = [(mod, validate(mod)) for mod in mods]
    output.mkdir(parents=True, exist_ok=True)
    notes = ["### Bundled Mods", ""]
    for mod, payload in payloads:
        archive_path = output / f"{mod.name}.zip"
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in payload:
                archive.write(path, path.relative_to(mod).as_posix())
        with zipfile.ZipFile(archive_path) as archive:
            expected = {path.relative_to(mod).as_posix() for path in payload}
            if set(archive.namelist()) != expected or archive.testzip() is not None:
                raise ValueError(f"Archive verification failed: {archive_path}")
        notes.append(f"- **{mod.name}.zip**: {description(mod)}")
        print(f"Verified {archive_path.name}: {len(payload)} files")
    (output / "release_notes.md").write_text("\n".join(notes) + "\n", encoding="utf-8")
    print(f"Built and verified {len(mods)} archives")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    build(args.root, args.output or args.root / ".releases")
