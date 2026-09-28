# Release notes

!!! info "Technical changelogs"

    For complete technical changelogs check out the respective ones on the repos:
    [Antares Web](https://github.com/AntaresSimulatorTeam/AntaREST/blob/dev/docs/CHANGELOG.md),
    [Antares Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator/blob/develop/docs/developer-guide/CHANGELOG.md),
    [Antares Xpansion](https://github.com/AntaresSimulatorTeam/antares-xpansion/blob/develop/docs/changelog/CHANGELOG.md) or
    [Antares Craft](https://github.com/AntaresSimulatorTeam/antares_craft/blob/main/docs/CHANGELOG.md).

:arrow_down: Check out our curated feed of user-oriented release notes !

---

## Antares Web v2.35.00 
<span class="release-date">📅 Sep 23, 2026</span>

## 🎉 What's New

- **Database-backed studies: creation and import** — Creating and importing database-backed studies is now available.
- **GDPR: RTE notices displayed** — RTE’s GDPR notices are now displayed in the application, in compliance with regulatory requirements.
- **Documentation: updated link** — The documentation link now points to the new version, so no more broken pages.
- **Outputs: easier access to search fields and filters** — Search fields and filters are now more accessible, making it faster to navigate through outputs.
- **Outputs: annual outputs prioritized** — Output displays now prioritize annual results by default, providing more relevant information at a glance.



## 🐛 Notable Bug Fixes

- Fixed an issue preventing scanning from working when database-backed studies were present.
- Fixed an issue preventing Xpansion link profiles from being viewed.
- Fixed an issue affecting the display of zone dropdown lists in coupling constraints.
- Fixed an issue preventing a value from being propagated across multiple cells in the Scenario Builder.
- Fixed an issue affecting the Scenario Builder on studies using version 8.6 or earlier.

## ⚡ Performance

Extensive technical improvements have been made: 

- removal of unnecessary output compression/decompression (significantly reducing processing time for large managed studies)
- refactoring and fixes to the output/download API for the Parquet format
- adoption of a more compact identifier for database-backed studies.

These updates enhance the stability and performance of the application.

---

## Antares Web v2.34.00 
<span class="release-date">📅 Aug 19, 2026</span>

## 🎉 What's New

- **Launcher: schedule a simulation**  — Delay the launch of a simulation.
- **Favorites: save an external folder** — Add an external folder directly to your favorites for one-click access.
- **Import: multiple studies at once** — Import several studies simultaneously without having to repeat the operation.
- **"Move" button hidden for variants** — This irrelevant button is now hidden for variant studies, making the interface cleaner.
- **Outputs: optimized per-variable output screen** — Navigation and readability of the per-variable output screen have been improved.
- **Table mode stored in the database** — The table display mode is now persisted in the database instead of localStorage, so your preferences follow you wherever you go.

## 🐛 Notable Bug Fixes

- Fixed an issue that made autocompletion unreliable in the "Variable" field in Outputs.
- Fixed an error occurring when importing a failed simulation.
- Fixed an issue with unarchiving studies stored in the database.
- Fixed a bug preventing a study from being launched in Xpansion mode when it is not an Xpansion study. This case is now correctly blocked with a clear error message.
- Fixed an issue causing some outputs to be invisible in adequacy mode.
- Fixed the Digest being unavailable for "adequacy" results.

## ⚡ Performance

Extensive technical improvements have been made: 

- migration to Pydantic for configuration management (for improved robustness and maintainability)
- background loading of cluster load information to prevent the UI from being blocked
- removal of unnecessary output disk-usage recalculations
- harmonization of result aggregation logic.

These updates enhance the stability and performance of the application.

---

## Antares Web v2.33.00 
<span class="release-date">📅 Jun 24, 2026</span>

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
<span class="release-date">📅 May 27, 2026</span>

### 🐛 Notable Bug Fixes

- **Digest Issue** — When using dynamic groups, production values were correctly calculated and returned, but their summary was missing from the digest.
- **Hydro: Inter-Monthly Breakdown Parameter Ignored** — Since version 9.2, even if a value was specified for the `inter-monthly-breakdown` parameter, it was not taken into account, and the default value was used instead.
- **Hydro: Infeasibility in Hydro Remix** — Fixed an issue where the hydro remix became infeasible when using the "accurate hydro remix" option with short-term storage.

---

## Antares Web v2.32.00 
<span class="release-date">📅 May 26, 2026</span>

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
<span class="release-date">📅 Apr 23, 2026</span>

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
