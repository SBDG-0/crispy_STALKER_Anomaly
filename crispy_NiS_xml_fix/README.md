# NiS XML and Faction Relations Fix

**Version:** `1.0.0.0`

## Description

Repairs malformed bullets in faction relationship descriptions and supplies replacement English item string tables for ammo, glowsticks, and medical items.

## Preview

<img src="https://github.com/user-attachments/assets/b93af64d-8685-4f5d-9516-2cf765f14060" alt="NiS Bullet Fix" width="900" />

## Features

- Includes `st_items_ammo_new.xml`, `st_items_glowstick.xml`, and `zzz_st_items_medical.xml` under `gamedata/configs/text/eng/`. These are complete string tables, not runtime patches.

After the original `UINewGame:UpdateDescr` runs, replaces UTF-8 replacement-character bytes in the relationship text with the Windows-1251 bullet expected by the game's font. When replacements occur, recalculates the text height.

## Requirements and compatibility

- [Modded Exes](https://github.com/themrdemonized/xray-monolith)

No settings or MCM dependency. <br> The runtime hook specifically fixes faction-relations text. <br> The bundled English string tables replace files with the same names; merge them if another addon changes those files. This does not repair every possible NiS/encoding issue elsewhere in the game.

`zzz_st_items_medical.xml` is designed around BHSRO, remove it if you dont use BHSRO.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
