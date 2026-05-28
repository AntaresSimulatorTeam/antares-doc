# File structure of an Antares study

!!! warning
    This page is under construction.

An on disk Antares study has a certain structure and is composed of different configuratin files
(`.ini`) and some delimiter separated value files such as `.csv`. 

## Overview of the file structure

The file structure is the following:

```
my_study
├── input
├── layers
├── logs
├── output
├── settings
├── user
├── Desktop.ini
└── study.antares
```

## Input folder

The input folder centralize all the different parameters and time series necessary for the simulation.

```
inputs
├── areas
├── bindingconstraints
├── hydro
├── links
├── load
├── misc-gen
├── renewables
├── reserves
├── solar
├── st-storage
├── thermal
└── wind
```

## Layer folder

The layer folder stores information about the layers you have on your map to display your nodes.
Indeed, layers allow you for big studies to see only some nodes and links not to overcrowd the view.

## Logs folder

In the log folder, you will find every log related to the core computation executables: 

- antares-simulator
- antares-xpansion-launcher

This is especially useful to debug your study and check whether some process finished
without any problem.

## Outputs folder

Inside this folder, you have one folder per simulation regrouping of the different results
of the simulation. 

## Settings folder

This folder comprise mainly the files `generaldata.ini` with all the settings
and the `scenariobuilder.dat` which contains the information 
to [set the random draw during the simulation](../tutorials/build-scenario.md). 

## User settings

Inside the user folder, there is notably an `expansion` folder that stores the candidates,
link profiles, capacities...

## Other files

At last, the `Desktop.ini` and `study.antares` files contain some general information
about the study, notably the version of the study and the author.

