# NiS Faction Relations Bullet Fix

Repairs the malformed bullet character displayed in faction relationship descriptions on the new-game faction selection screen.

### Functionality
After the original `UINewGame:UpdateDescr` runs, replaces UTF-8 replacement-character bytes in the relationship text with the Windows-1251 bullet expected by the game's font. When replacements occur, recalculates the text height.

### Requirements and compatibility
Requires Anomaly and [Modded Exes](https://github.com/themrdemonized/xray-monolith) supporting the ModXML script entry point and `main_menu_on_init` callback. No settings or MCM dependency. This is specifically a faction-relations text fix; it does not repair every possible NiS/encoding issue elsewhere in the game. A replacement faction menu must retain `UINewGame`, `UpdateDescr` and `text_relations`.

### Credits
- SavageBulldog / SavageBulldogOG: repair wrapper.
- Anomaly developers: original menu, relationship descriptions and font system.
- Modded Exes contributors: script loading and menu callback support.
- No separately named third-party base addon is identified in the supplied script.

### Installation
Install this folder as a separate mod in Mod Organizer 2, with `gamedata` at the mod root, then enable it alongside its requirements. To build an archive, ZIP the contents of this mod folder rather than the entire repository. Disable the mod in MO2 to remove its files.

Repository changes by [SavageBulldog / SavageBulldogOG](https://github.com/SBDG-0/crispy_stalker_anomaly). Original authors retain credit for their code and assets.
