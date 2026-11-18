# NiS XML and Faction Relations Fix

**Version:** `1.0.0`

## Description

Repairs malformed bullets in faction relationship descriptions and supplies replacement English item string tables for ammo, glowsticks, and medical items.

## Preview

<img src="https://github.com/user-attachments/assets/b93af64d-8685-4f5d-9516-2cf765f14060" alt="NiS Bullet Fix" width="900" />

## Features

- Includes `st_items_ammo_new.xml`, `st_items_glowstick.xml`, and `zzz_st_items_medical.xml` under `gamedata/configs/text/eng/`. These are complete string tables, not runtime patches.

After the original `UINewGame:UpdateDescr` runs, replaces UTF-8 replacement-character bytes in the relationship text with the Windows-1251 bullet expected by the game's font. When replacements occur, recalculates the text height.

## Requirements and compatibility

Requires Anomaly and [Modded Exes](https://github.com/themrdemonized/xray-monolith) supporting the ModXML script entry point and `main_menu_on_init` callback. No settings or MCM dependency. The runtime hook specifically fixes faction-relations text. The bundled English string tables replace files with the same names; merge them if another addon changes those files. This does not repair every possible NiS/encoding issue elsewhere in the game. A replacement faction menu must retain `UINewGame`, `UpdateDescr` and `text_relations`.

## Credits

- Anomaly developers: original menu, relationship descriptions and font system.
- Modded Exes contributors: script loading and menu callback support.
- No separately named third-party base addon is identified in the supplied script.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
