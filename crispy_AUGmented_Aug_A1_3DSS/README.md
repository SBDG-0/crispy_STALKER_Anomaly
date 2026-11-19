# AUGmented AUG A1 3DSS Patch

**Version:** `1.0.0.0`

## Description

Adapts the AUG A1 (`wpn_aug`) for Shader 3D Scopes using a replacement HUD model, reticle texture and DLTX configuration overrides.

## Preview

<img src="https://github.com/user-attachments/assets/e3e4e487-36bb-471d-a5a4-45c24e891545" alt="AUG A1 with Shader 3D Scopes" width="900" />

## Features

- Clears the original 2D scope texture.
- Sets 3DSS dirt intensity, eye relief and reticle size.
- Adjusts weapon position, fire points, and primary/alternate HUD aim offsets, including the 16:9 entries.
- Supplies `wpn_aug_a1_hud.ogf` and `wpn/scope/aug/crosshair_dot.dds`.

## Requirements and compatibility

Requires [AUGmented - The AUG Pack](https://www.moddb.com/mods/stalker-anomaly/addons/augmented-the-aug-pack), a working Shader 3D Scopes setup, and [Modded Exes](https://github.com/themrdemonized/xray-monolith) with DLTX/3DSS support. Install after the base weapon/scopes setup and let this patch win conflicts for its model, texture and settings. Only the AUG A1 sections are patched; this is not a conversion of the entire AUG pack. Other AUG model or reposition addons can conflict. There is no MCM menu.

## Credits and asset provenance

- FIREBREATH1001 / Firebreath and Blackgrowl: [original AUGmented pack](https://www.moddb.com/mods/stalker-anomaly/addons/augmented-the-aug-pack)
- Party_50: [Shader 3D Scopes](https://www.moddb.com/mods/stalker-anomaly/addons/shader-3d-scopes).

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, use the repository packaging workflow. ZIP roots contain only `meta.ini` and `gamedata/`; README files are excluded at every depth. Disable the mod in MO2 to remove its files.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
