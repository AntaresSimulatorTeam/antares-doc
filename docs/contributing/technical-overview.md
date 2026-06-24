# Technical overview

## Repo presentation

Antares [Github](https://github.com/AntaresSimulatorTeam) is a composed of mainly
4 different repositories. However, there are even more used for the development of
Antares that you can see in the [full cartography](#full-cartography-of-the-repositories) below.

### Antares Web

[Antares Web](https://github.com/AntaresSimulatorTeam/AntaREST) main entry points 
with the user interface and the REST API, it allows notably:

- The creation, import and edit of a study
- The raw visualization and edit of input data
- The raw visualization of the [simulator](#antares-simulator) output data
- The launch of simulation on a server or a high performance cluster
    (via the custom library [antares-launcher](https://github.com/AntaresSimulatorTeam/antares-launcher))

### Antares Simulator

[Antares Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator) 
performs the core computations that solves the supply-demand
optimisation problem with all the input data.

### Antares Xpansion

[Antares Xpansion](https://github.com/AntaresSimulatorTeam/antares-xpansion)
is an investment module allowing the user to optimize an investment on a 
set of candidates. That is to say the user would like to increase the 
installed capacity in MW.

### Antares Craft

[Antares Craft](https://github.com/AntaresSimulatorTeam/antares_craft) is a python library that allows users to interact locally or 
via the API with Antares studies.

### Full cartography of the repositories

![](../assets/diagrams/architecture/repo-inventory.drawio)


## Technical information for devops

Here is a draft of the technical reprensation of the data transfers between
APIs, scripts, executables... in the [performance version](../overview/architecture.md#performance-version).

![](../assets/diagrams/architecture/antares-technical-overview.drawio)

## Assets You Shouldn’t Use

### [Antares R Packages](https://rte-antares-rpackage.github.io/rPackagesRte/)

These are the old R packages we used before Antares Craft to interact with Antares studies. They still exist, but we will no longer maintain them.
We strongly recommend using [Antares Craft](https://github.com/AntaresSimulatorTeam/antares_craft) instead.

### [Antares Data Manager](https://github.com/AntaresSimulatorTeam/antares-datamanager-back)

This is a new application used by RTE to prepare data for some Antares studies.
This application is highly specific to RTE’s national studies structure and data. It would not be easy to use with international studies.
Perhaps one day we will make it more generic, but it is not in our [roadmap](../overview/roadmap.md) yet.

