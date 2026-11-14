# Vanilla Options Script Improvements

Replaces Anomaly's vanilla options-menu script with adjusted slider limits and finer control, plus a runtime label change identifying the expanded carry-weight slider.

## Functionality

- Carry-weight slider: **10–500 kg**, in **5 kg** steps.
- Goodwill, rewards, repair, upgrade, buy/sell and money-loot multipliers use expanded 0.1–4 ranges.
- Trader restock interval: **4–256**, step **2**; expanded battery-consumption and stamina power-loss controls.
- Master, music and ambient volume sliders use **0.01** steps.
- Detail-radius slider uses **10**-unit steps.
- Appends `500kg Slider` to the carry-weight option's English/Russian label through ModXML.

<img src="https://github.com/user-attachments/assets/77e04ddd-3f28-43ff-afeb-c9d6262b78c0" alt="Options menu audio controls" width="900" />

<img src="https://github.com/user-attachments/assets/c8af0676-b16d-4d45-865a-49d409bd4022" alt="Options menu sensitivity controls" width="900" />

## Requirements and compatibility

Requires Anomaly's vanilla-style options system and [Modded Exes](https://github.com/themrdemonized/xray-monolith) with runtime XML editing for the label hook.

This is a complete `gamedata/scripts/ui_options.script` replacement.

Other mods supplying that script need a manual merge; changing priority alone chooses one version and loses the other version's changes. It is intended for vanilla options, not arbitrary modpack menu replacements.
Configure through the normal game options menu; there is no separate MCM page.

## Credits

- Tronex: original Anomaly options-menu implementation.
- Anomaly developers: base options system and gameplay settings.
- Modded Exes contributors: runtime XML editing support.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to all mods](../README.md)

made with ❤️ by SavageBulldogOG
