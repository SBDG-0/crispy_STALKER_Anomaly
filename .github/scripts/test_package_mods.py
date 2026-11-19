import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('packager', Path(__file__).parent / 'package_mods.py')
packager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packager)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path.cwd())
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.mod = self.root / 'crispy_test'
        (self.mod / 'gamedata' / 'scripts').mkdir(parents=True)
        (self.mod / 'gamedata' / 'scripts' / 'test.script').write_text('payload')
        self.meta = self.mod / 'meta.ini'
        self.meta.write_text('[General]\nurl=' + packager.REPOSITORY_URL + '\nhasCustomURL=true\ninstallationFile=crispy_test.zip\nversion=1.0.0.0\n')
        (self.mod / 'README.md').write_text('# Test\n\n**Version:** `1.0.0.0`\n')

    def test_only_installable_payload(self):
        for path in [self.mod / 'extra.txt', self.mod / 'gamedata' / 'scripts' / 'ReadMe.MD']:
            path.write_text('excluded')
        packager.build(self.root, self.root / 'output')
        with zipfile.ZipFile(self.root / 'output' / 'crispy_test.zip') as archive:
            self.assertEqual(set(archive.namelist()), {'meta.ini', 'gamedata/scripts/test.script'})

    def test_wrong_archive_name_rejected(self):
        self.meta.write_text(self.meta.read_text().replace('crispy_test.zip', 'old.zip'))
        with self.assertRaises(ValueError):
            packager.validate(self.mod)

    def test_custom_url_required(self):
        self.meta.write_text(self.meta.read_text().replace('hasCustomURL=true', 'hasCustomURL=false'))
        with self.assertRaises(ValueError):
            packager.validate(self.mod)

    def test_nonstandard_versions_rejected(self):
        original = self.meta.read_text()
        for version in ['', '1.3', '1.0.0', 'v1.0.0.0', '1.01.0.0', '1.0.0.01', '1.0.0.0.0', '1.4.0-clean', 'd2026.11.11.0']:
            with self.subTest(version=version):
                self.meta.write_text(original.replace('version=1.0.0.0', f'version={version}'))
                with self.assertRaises(ValueError):
                    packager.validate(self.mod)

    def test_nonzero_revision_accepted(self):
        self.meta.write_text(self.meta.read_text().replace('version=1.0.0.0', 'version=1.0.0.7'))
        (self.mod / 'README.md').write_text('# Test\n\n**Version:** `1.0.0.7`\n')
        self.assertTrue(packager.validate(self.mod))

    def test_readme_version_mismatch_rejected(self):
        (self.mod / 'README.md').write_text('# Test\n\n**Version:** `2.0.0.0`\n')
        with self.assertRaises(ValueError):
            packager.validate(self.mod)

    def test_missing_metadata_rejected(self):
        self.meta.unlink()
        with self.assertRaises(FileNotFoundError):
            packager.validate(self.mod)

    def test_all_metadata_validated_before_build(self):
        (self.root / 'crispy_invalid').mkdir()
        with self.assertRaises(FileNotFoundError):
            packager.build(self.root, self.root / 'output')
        self.assertFalse((self.root / 'output').exists())

    def test_description_does_not_leak_between_mods(self):
        (self.mod / 'README.md').write_text('# Mod\n## Description\nTest description\n')
        self.assertEqual(packager.description(self.mod), 'Test description')
        self.assertEqual(packager.description(self.root), 'No description provided.')


unittest.main()
