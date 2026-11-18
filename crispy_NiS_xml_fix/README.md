# NiS Faction Relations Bullet Fix

**Version:** `1.0.0`

## Description

Repairs the malformed bullet character displayed in faction relationship descriptions on the new-game faction selection screen.

## Preview

<img src="https://github.com/user-attachments/assets/b93af64d-8685-4f5d-9516-2cf765f14060" alt="NiS Bullet Fix" width="900" />

## Features

After the original `UINewGame:UpdateDescr` runs, replaces UTF-8 replacement-character bytes in the relationship text with the Windows-1251 bullet expected by the game's font. When replacements occur, recalculates the text height.

## Requirements and compatibility

Requires Anomaly and [Modded Exes](https://github.com/themrdemonized/xray-monolith) supporting the ModXML script entry point and `main_menu_on_init` callback. No settings or MCM dependency. This is specifically a faction-relations text fix; it does not repair every possible NiS/encoding issue elsewhere in the game. A replacement faction menu must retain `UINewGame`, `UpdateDescr` and `text_relations`.

## Credits

- Anomaly developers: original menu, relationship descriptions and font system.
- Modded Exes contributors: script loading and menu callback support.
- No separately named third-party base addon is identified in the supplied script.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
