# Getting started

## Software Presentation

[Antares-Simulator](https://antares-simulator.org ) is an Open Source (GNU GPL 3.0) standalone software. It is a sequential Monte-Carlo simulator designed for short to long term studies of large interconnected power grids. It simulates the economic behavior of the whole transmission-generation system, throughout the year and with a resolution of one hour.


**Antares-Simulator can be downloaded free of charge, installed on any local computer or server and use without any limitation.**


RTE (French Electricity Transmission system Operator) has initially developed the tool for its own purposes and keeps on improving and enhancing its capabilities. Antares-Simulator is currently one of key tool of [reference studies](https://antares-simulator.org/pages/etudes/4/) such as the French Generation Adequacy Report, published by RTE, or the ENTSO-E’s Ten Years Network Development Plan (TYNDP). More generally, the tool has been proving very useful for assessing the economic performances, ecological impact and security of supply levels of power systems, as well as the contribution of its assets (generation units, interconnectors, storages, etc.) to these three axes.


The executable file of Antares-Simulator is [provided free of charge](https://antares-simulator.org/pages/antares-simulator/6/). By subscribing to the User’s Club, one can also benefit from services such as software maintenance or trainings.

### Starting with _Antares-Simulator_

User can define an electrical network using _nodes_ (or _areas_) that represent regions or countries. Each _area_ will have specific parameters, powerplants, and links with other _areas_ etc. Each _node_ represents an independent system with its own production fleet and hourly consumption. Within a zone, it is assumed that there is no network constraint on energy exchanges. Several _nodes_ can be interconnected to exchange power with one another, with specific network constraints.

The consumption of a _node_ is defined by its _Load_. The _Load_ can be an user-input with _Time-series_ or it can be generated via probabilistic models.

The _Thermal_ production units are defined in _clusters_. The _clusters_ can be defined as containing _Gas_, _Hard Coal_, _Lignite_, _Mixed Fuel_, _Nuclear_, _Oil_ or _Other_ production units. They are set using their _Operating Parameters_, _Operating Costs_ and _Reliability Model_. Then, the production of the thermal units is generated and optimized using the **TS generator**. Production is limited by the units’ outages which are simulated through multiple parameters.


The _Wind_ and _Solar_ production is fatal and cannot be optimized. It is either input by the user or randomly generated using probabilistic models. The parameters of theses models can be derived from historical data.


Hydroelectricity generation is both Run of the River (_ROR_) and _hydro storage_.

_ROR_ uses streamflow to produce electricity. This generation is non-dispatchable.

_Hydro storage_ refers to the water stored in dams and lakes. Two types of storage can be employed: 

-	**Hydro plants with storage**: releasing water through turbines when needed.

-	**Pumped storage**: like hydro plants with storage with a high and a low reservoir but with a turbine between. When the when demand and price are low, water is pumped, from the lower to the higher levels. If the demand and price are high, water is turbinated

Hydro with storage is dispatchable generation unlike RoR, Antares Simulator will optimize the use of water week by week throughout the year. Reservoirs depend on inflows such as melting ice which correspond to the daily amount of hydro energy being added to the reservoir. These inflows are modeled by daily TS.


Miscellaneous generation can also be set, it contains all other internal electricity production and external (ROW - representing electricity interconnections) electricity production. Negative values mean that the actual area exports electricity to the ROW. This data is “deterministic”, as the corresponding Time-Series are the same whatever Monte-Carlo year is considered.

Finally, additional economic information, such as the _unsupplied energy cost_ can be added to the study, before launching the simulation. The output is a data table containing _costs_, _balance_, _production_, etc.


Antares' outputs can then be processed and visualized using spreadsheet software or using the developped R-packages.

### Post-processing with R-packages

Different R-packages have been developed to process the output of an Antares study. They can be used to manipulate simulation output, read or visualize them:

- [**antaresRead**](https://rte-antares-rpackage.github.io/antaresRead/index.html) to import the output to a R session;

- [**antaresProcessing**](https://github.com/rte-antares-rpackage/antaresProcessing) to manipulate data on Antares output;

- [**antaresViz**](https://rte-antares-rpackage.github.io/antaresViz/index.html) to visualize Antares output using interactive graphs.


### Pre-processing with R-packages

Different packages have been developed to launch Antares studies from a R session:

- [**antaresEditObject**](https://rte-antares-rpackage.github.io/antaresEditObject/index.html) to edit an Antares study before launching it; 

- [**antaresXpansion**](https://github.com/rte-antares-rpackage/antaresXpansion) to optimizes the installed capacities of an Antares study;

- [**antaresFlowbased**](https://github.com/rte-antares-rpackage/antaresFlowbased) to  launch a flowBased study from an existed Antares study; 

- [**antaresWaterValues**](https://rte-antares-rpackage.github.io/antaresWaterValues/index.html) to  generate water values for Antares and to run specific simulations.
