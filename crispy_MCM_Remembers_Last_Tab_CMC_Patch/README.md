# MCM Remembers Last Tab + Custom Mod Categories Compatibility Patch

**Version:** `1.1.0.0`

## Description

Adds Custom Mod Categories compatibility to MCM Remembers Last Tab.

## Features

- Live search respects CMC's search suppression, and queues tree rebuilds through CMC's next-frame refresh.
- Apply saves the current page and reopens it on the next UI frame, replacing CMC's return to the category overview.
- Restart-required settings retain the original close/restart flow.
- Search is cleared when reopening; ordinary category-list scrolling is restored when the category still matches.
- Remembers the category overview separately from a settings page, so stale last_path values do not reopen the wrong page.
- Scroll offsets are restored only when the category and page match.
- Search text is not persisted; search-result offsets are discarded because reopening uses the normal category list.
- The right-hand settings pane scroll is saved separately and restored after Apply and reopening the same page, including when its category has changed.
- All Mods stays selected after Apply and reopening.
- Saved category browsing is preserved when the selected mod still belongs to that list; otherwise its current category is used.
- Removed categories fall back to the category overview. Reassigned pages use their current category.
- Existing Enable and Remember Scroll settings remain available. The legacy page is imported on first use without its unqualified scroll offset.

## Requirements

- [Mod Configuration Menu - ravenascendant](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu)
- [Custom Mod Categories - elseform](https://github.com/elseform/anomaly-mods/tree/release/Custom%20Mod%20Categories)
- [MCM Remembers Last Tab v1.2 - turretrider](https://www.moddb.com/mods/stalker-anomaly/addons/mcm-remembers-last-tab)

## Installation

Install the ZIP from [releases](https://github.com/SBDG-0/crispy_stalker_anomaly/releases) as a separate mod in MO2.

Enable this patch below both original mods in Mod Organizer 2 so its scripts override turretrider’s version.

## Changelog

### 1.1.0.0

Previously labeled `1.01`; recorded as `1.1.0.0` under the repository’s four-part package version format. Internal component labels such as `1.8-cmc` and `1.1-cmc` identify the bundled scripts, not the package version.

Fixed compatibility with Back and Forth Buttons for MCM.

---

## Reuse

This software is provided “as is”, without warranty of any kind. You may use, modify, and distribute it, provided you credit SavageBulldogOG and include a link to this repository.

[crispy_stalker_anomaly](https://github.com/SBDG-0/crispy_stalker_anomaly)

---

[Back to main page](../README.md)

made with ❤️ by SavageBulldogOG
