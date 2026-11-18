# Faction Select Name Randomizer Button

**Version:** `1.0.0`

## Description

Adds a separate random-name button beside the character name field on the new-game faction selection screen. It changes only the name, keeping the selected faction and other starting choices.

## Preview

<img src="https://github.com/user-attachments/assets/9870052f-6fa9-4e51-a6d3-059819375ab1" alt="Faction selection with the separate random-name button" width="900" />

## Features

- Uses the current faction and Anomaly's translated first/last-name pools.
- Army, Duty and UNISG use military rank name pools; other factions use stalker, bandit and science pools.
- Inserts the button dynamically for the standard, 16:9 and 21:9 faction-selection XML files, reducing the name field width to make room.

## Requirements and compatibility

Requires Anomaly and [Modded Exes](https://github.com/themrdemonized/xray-monolith) with the `on_xml_read`/ModXML API. No MCM settings. The menu must retain Anomaly's `UINewGame` class, name field and random-button layout elements; heavily replaced new-game menus may need adaptation. No original XML file is replaced.

## Credits

- SavageBulldog / SavageBulldogOG: button and integration script.
- Anomaly developers: original faction-selection menu, random-name logic, translations and name pools. The script explicitly follows the name step of `UINewGame:OnRandomize`.
- Modded Exes contributors: runtime XML editing and callbacks.

## Installation

Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
