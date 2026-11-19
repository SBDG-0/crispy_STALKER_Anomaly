
# Faction Select Name Randomizer Button

**Version:** `1.0.0.0`

## Description

Adds a separate random-name button on the money row below the character name field on the new-game faction selection screen. It changes only the name, keeping the selected faction and other starting choices.

## Preview

<img width="900" alt="_crispy_randomize_names_van" src="https://github.com/user-attachments/assets/ac5bf503-09d0-4eb6-8cc3-5e67045e5673" />
<img width="900" alt="_crispy_randomize_names" src="https://github.com/user-attachments/assets/9ff5df37-1107-4332-96dd-8fc8e7f4f8e3" />

## Features

- Uses the current faction and Anomaly's translated first/last-name pools.
- Army, Duty and UNISG use military rank name pools; other factions use stalker, bandit and science pools.
- Keeps the name field at its original width and leaves the description area unchanged.
- Aligns the money label and amount with the name row, reserving space on the right for the button.
- Uses the vanilla compact button height, `letterica16` font, texture and translated Randomize label.
- Reads the active layout dynamically for the standard, `_16` and `_21` faction-selection XML filenames.
- Requires no MCM menu or settings.

## Requirements and compatibility

- [Modded Exes](https://github.com/themrdemonized/xray-monolith)

Targets **Anomaly 1.5.3** with Modded Exes. No original XML file is replaced: the script inserts the button and adjusts the money row at runtime. UI mods can supply their own layouts, but must retain the controls used by this script. The two supplied vanilla reference sets contain standard and `_16` layouts, with no separate `_21` file.

### Layout and scaling

The button sits to the right of the money amount, below the name. Its right edge aligns with the name field's right edge. The money label moves left to align with the name label; the amount starts immediately after the label's box and uses the remaining space before the button.

- Width: **85%** of the active layout's main Randomize button width.
- Height: the active layout's Faction button height, vertically centered on the money amount.
- Gap before the button: **2%** of the main Randomize button width.
- Text: `letterica16`, centered horizontally and vertically, using Anomaly's existing translated Randomize label.
- Texture: vanilla `ui_inGame2_button`, stretched to the button dimensions.

The name field and description viewport keep their original dimensions. The script skips insertion if required controls or numeric attributes are missing, the button already exists, or the calculated money/button dimensions are not positive.

### Compatibility and validation

- Vanilla Anomaly 1.5.3 
- SOTA UI 

Very long names can still exceed the original name field. Larger money amounts, longer translations, custom fonts and other UI layouts can also need additional space; compatibility with every UI mod or language is not established.

## Credits

- Anomaly developers: original faction-selection menu, random-name logic, translations and name pools. <br>The script explicitly follows the name step of `UINewGame:OnRandomize`.
- Modded Exes contributors: runtime XML editing and callbacks.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. Disable the mod in MO2 to remove its files.

After updating, restart the game and reopen the new-game faction-selection screen. Use the small Randomize button on the money row to change only the character name; the original main Randomize button keeps its normal behavior.

For a distributable archive, use the repository packaging workflow. The ZIP root must contain only `meta.ini` and `gamedata/`, without a containing project folder or README files.

## Layout change notes

- Replaced the original inline button, which reduced the name field width, with a button on the money row.
- Aligned the money label with the name label and kept the amount on one line.
- Preserved the name field, description area, faction-specific name generation and callback behavior.
- Widened the compact button and tightened the money-row spacing to address SOTA 16:9 label overflow.
- Kept positioning automatic; no MCM settings were added.
- Confirmed the current layout and sizing working in-game with vanilla and SOTA UI (user testing, 19 November 2026).

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
