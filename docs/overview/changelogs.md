# Release notes

!!! info "Technical changelogs"

    For complete technical changelogs check out the respective ones on the respo:
    [Antares Web](https://github.com/AntaresSimulatorTeam/AntaREST/blob/dev/docs/CHANGELOG.md),
    [Antares Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator/blob/develop/docs/developer-guide/CHANGELOG.md),
    [Antares Xpansion](https://github.com/AntaresSimulatorTeam/antares-xpansion/blob/develop/docs/changelog/CHANGELOG.md) or
    [Antares Craft](https://github.com/AntaresSimulatorTeam/antares_craft/blob/main/docs/CHANGELOG.md).

:arrow_down: Check out our curated feed of user-friendly release notes !

---

## Antares Web v2.33.00

## 🎉 What's New

- **User Name on Outputs** — Output information now displays the name of the user who launched the calculation, for better traceability.
- **Import Study into Target Folder** — You can now import a study directly into the folder of your choice.
- **Disabled "Launch" Button for Archived Studies** — Prevents accidental launches of archived studies. The button is now disabled.
- **Explorer: Clearer Selected Tree View** — The visualization of the selected tree has been improved for clearer navigation.

## 🐛 Notable Bug Fixes

- Fixed a bug causing simultaneous execution of multiple auto-archiving processes.
- Fixed a bug preventing the display of "Allocation" and "Correlation" matrices.
- Various other bug fixes.

## ⚡ Performance

Extensive technical improvements have been made: 

- Integration of reserves in optimization endpoints
- Overhaul of reserve parameter management endpoints (global and per reserve)
- X.Y format for study version in the API
- Optimization of database storage methods (study management, variants, calculation launches)
- DAO alignment
- Switching archiving from 7z to zip. 

These updates enhance the stability and performance of the application.

---

## Antares Simulator v9.3.11

### 🐛 Notable Bug Fixes

- **Digest Issue** — When using dynamic groups, production values were correctly calculated and returned, but their summary was missing from the digest.
- **Hydro: Inter-Monthly Breakdown Parameter Ignored** — Since version 9.2, even if a value was specified for the `inter-monthly-breakdown` parameter, it was not taken into account, and the default value was used instead.
- **Hydro: Infeasibility in Hydro Remix** — Fixed an issue where the hydro remix became infeasible when using the "accurate hydro remix" option with short-term storage.

---

## Antares Web v2.31.00

### 🎉 What's New

- **Archived Studies Better Highlighted** — The screen now adapts to the archived status of a study for clearer reading.
- **Full Column Names in Outputs** — Columns always display their full labels in resultsno more ambiguity.
- **Favorites: Display Preferences Saved** — Your display preferences in favorites are now persisted in localStorage.
- **Suffix Verification Before Simulation** — Output suffixes are checked before launching to prevent errors during runs.
- **Disk Space Hidden for Disk-Based Studies** — Disk space visualization is removed for disk-based studiesstreamlined interface.
- **Matrix: Auto-Resized Columns on Paste** — Pasting content that exceeds column width now triggers automatic adjustment.

### 🐛 Notable Bug Fixes

- Fixed a bug that prevented support for the in-memory version of Xpansion.
- Fixed a bug that blocked requests to `/download/metadata`.
- Fixed a bug that slowed down queries on coupling constraints.
- Fixed a bug that allowed generating variants from archived studies.
- Fixed a bug that caused erratic log display during simulations.
- Various other bug fixes.

---

## Antares Web v2.31.00

### 🎉 What's New

- **📁 Favorites** — You can now favorite your folders for even faster access.
- **📋 List View** — In addition to grid mode, a new list view is available to display your studies according to your preferences.
- **🗑️ Disk-Based Studies** — The delete button is removed for non-managed studies: no more accidental clicks!
- **🌡️ Thermal Clusters** — The "Other emission rates" block is now collapsible for a cleaner display. The "CO2" field has been moved out of the "Other emission rates" group for better clarity and readability.
- **🔢 Matrix Filters** — Decimal values are now accepted in filters.
- **📍 Scroll Position Preserved** — The explorer automatically restores your position after navigating within a study.

### 🐛 Notable Bug Fixes

- Fixed a bug that prevented accessing files via the exploration pane in debug view.
- Fixed a bug that prevented migrating a study from version 8.8 to 9.3 without going through 9.2.
- Fixed a bug that deleted simulation results from managed studies after archiving and unarchiving.
- Fixed a bug that prevented bulk copy/paste from Excel into a matrix.
- Fixed a precision issue that distorted the averages displayed in matrices.
- Various other bug fixes.

### ⚡ Performance

Numerous optimizations have been implemented you should notice faster loading and smoother handling of your studies.