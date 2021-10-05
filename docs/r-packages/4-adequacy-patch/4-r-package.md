# R package : AdequacyPatch
## References
**Title:** Applies the Adequacy Patch Curtailment Sharing Rules to an Antares Study

**Description:** This package provides tools to apply the Adequacy patch on an Antares study. It provides functions to import:  - an Antares study, and in particular the time-steps where at least one country is in loss of load - the flow-based related files (time-serires, weigths and second-members) - the NTC links, formatted like the flow-based ones It also defines the main Adequacy patch function, taking the previously imported data and applying the following rules:  - Local matching: a country in loss of load cannot be globally exporting (it can on certain of its borders though) - Curtailment sharing: the "curtailment ratios" of countries in loss of load should be relatively close The optimization process of the patch is delegated to the optimization modelling langugage AMPL, and to the solver XPRESS.

**Version:** 0.0.0.9000

**License:** GPL-3

**Imports:** `data.table`, `antaresRead`, `stats`, `rAMPL`, `doParallel`, `plyr`, `antaresEditObject`, `fs`, `pipeR`


### `extract_FB_ptdf`
**Extracts the Power Transmission and Distribution Flows on each CB for each
country for the flow-based domain of a study.
It also converts the initial PTDFs, given for each link in PTDFs fiven for
each country.**




 **Usage:**
```
extract_FB_ptdf(sim_opts = antaresRead::simOptions())
```
**Arguments**

- `sim_opts`:  (list) Simulation options as given by antaresRead::setSimulationPath


**Value**

(data.table) Table containing the PTDFs of each country for each
critical branch

**Examples**
```
sim_opts = antaresRead::setSimulationPath("path/to/my/simulation")

ptdf_FB_data = extract_FB_ptdf(sim_opts=sim_opts)
```


### `extract_FB_ts`
**Extracts the flow-based time-series from an Antares study**




 **Usage:**
```
extract_FB_ts(sim_opts = antaresRead::simOptions())
```
**Arguments**

- `sim_opts`:  (list) Simulation options as given by antaresRead::setSimulationPath


**Value**

(data.table) Table containing the typical day for each day in each
Monte-Carlo year of the simulation.

**Examples**
```
sim_opts = antaresRead::setSimulationPath("path/to/my/simulation")

ts_FB_data = extract_FB_ts(sim_opts=sim_opts)
```


### `extract_patch`
**Extracts the data relevant for the Adequacy patch for a simulation output.**

It selects the time-steps in an ANtares study when at least one country is in
loss of load.


 **Usage:**
```
extract_patch(
  areas,
  virtual_areas,
  mcYears = "all",
  sim_opts = antaresRead::simOptions()
)
```
**Arguments**

- `areas`:  (string or vector of strings) what areas the patch should be applied on. Default: ""

- `virtual_areas`:  (string or vector of strings) Virtual areas of the study, excluded from the patch. Default: NULL

- `mcYears`:  (numeric or vector of numeric) The Monte-Carlo years to extract from. The special value "all" extracts all Monte-Carlo Years. Default: "all"

- `sim_opts`:  (list) Simulation options as given by antaresRead::setSimulationPath


**Value**

(data.table) Table containing, for each mcYear, time-step and country,
the DENS (domestic Energy Not Served) and DMRG (Domestic Margin).

**Examples**
```
sim_opts = antaresRead::setSimulationPath("path/to/my/simulation")
areas = antaresRead::getAreas()

patch_data = extract_patch(areas=areas, mcYears=c(1, 3), sim_opts=sim_opts)
```


### `adq_patch`
**Applies the Adequacy patch on given DENS and DMRG for countries and
constrained by the flow_based and NTC data.**

The Adequacy patch is a post-processing phase on an Antares study simulation,
applying the local-matching and curtailment sharing rules as defined by the
EUPHEMIA to correct situations with at least one country in loss of load.

*Details:*This function does not solve anything itself, it sets up and transfers the
relevant data to an AMPL model which then solves it using XPRESS.
 **Usage:**
```
adq_patch(
  patch_data,
  ts_FB_data,
  capacity_FB_data,
  capacity_NTC_data,
  ptdf_FB_data,
  ptdf_NTC_data
)
```
**Arguments**

- `patch_data`:  (data.table) DENS and DMRG for each country at each time-step

- `ts_FB_data`:  (data.table) typical day for each day

- `capacity_FB_data`:  (data.table) Capacity on each critical branch in the flow-based domain depeding on the typical day

- `capacity_NTC_data`:  (data.table) Maximum transfer capacity of each NTC border, mimicking capacity_FB_data

- `ptdf_FB_data`:  (data.table) PTDF for each country on each critical branch

- `ptdf_NTC_data`:  (data.table) Mimics ptdf_FB_data for each border


**Value**

(data.table) Table giving the MRG, ENS and net-position for each country
at each time-step

**Examples**
```
sim_opts = antaresRead::setSimulationPath("path/to/my/simulation")
areas = antaresRead::getAreas()

patch_data = extract_patch(areas=areas, mcYears=c(1, 3), sim_opts=sim_opts)
ts_FB_data = extract_FB_ts(sim_opts=sim_opts)
capacity_FB_data = extract_FB_capacity(sim_opts=sim_opts)
ptdf_FB_data = extract_FB_ptdf(sim_opts=sim_opts)
links_NTC_data = extract_NTC_links(areas=areas, sim_opts=sim_opts)

output = adq_patch(
patch_data,
ts_FB_data,
capacity_FB_data, links_NTC_data$capacity,
ptdf_FB_data, links_NTC_data$ptdf
)
```


### `extract_FB_capacity`
**Extracts the maximum transfer capacity on each CB for the flow-based domain of a study**




 **Usage:**
```
extract_FB_capacity(sim_opts = antaresRead::simOptions())
```
**Arguments**

- `sim_opts`:  (list) Simulation options as given by antaresRead::setSimulationPath


**Value**

(data.table) Table containing the limit capacity for each critical
branch on each typical day and for each hour.

**Examples**
```
sim_opts = antaresRead::setSimulationPath("path/to/my/simulation")

capacity_FB_data = extract_FB_capacity(sim_opts=sim_opts)
```


### `adq_write`
**Applies the Adequacy and write study by mc year**




 **Usage:**
```
adq_write(
  sim_opts,
  areas,
  virtual_areas,
  links_NTC_data,
  ptdf_FB_data,
  capacity_FB_data,
  ts_FB_data,
  mcYears,
  antaresfbzone,
  thresholdFilter
)
```
**Arguments**

- `sim_opts`:  Simulation options, as returned by antaresRead::setSimulationPath

- `areas`:  (string or vector of strings) what areas the patch should be applied on. Default: ""

- `virtual_areas`:  (string or vector of strings) Virtual areas of the study, excluded from the patch. Default: NULL

- `links_NTC_data`:  NTC

- `ptdf_FB_data`:  ptdf

- `capacity_FB_data`:  capa

- `ts_FB_data`:  ts

- `mcYears`:  (numeric or vector of numeric) The Monte-Carlo years to extract from. The special value "all" extracts all Monte-Carlo Years. Default: "all"

- `antaresfbzone`:  name for new antares area


**Value**



**Examples**
```

```


### `.single_time_step`
**Calls the AMPL Adequacy patch at each time-step**




 **Usage:**
```
.single_time_step(ampl, patch, capacity)
```
**Arguments**

- `ampl`:  (rAMPL::AMPL) AMPL object, with model and PTDF already loaded

- `patch`:  (data.table) Relevant data form the simulation for this time-step

- `capacity`:  (data.table) Limit capacity on each CB, containing both flow-based and NTC data


**Value**

(data.table) Table giving the MRG, ENS and net-position for each country
at this time-step

**Examples**
```

```


### `apply_adq_patch`
**Applies the Adequacy Patch on a given simulation**

The Adequacy patch is a post-processing phase on an Antares study simulation,
applying the local-matching and curtailment sharing rules as defined by the
EUPHEMIA to correct situations with at least one country in loss of load.


 **Usage:**
```
apply_adq_patch(
  sim_opts = antaresRead::simOptions(),
  areas = "all",
  virtual_areas = NULL,
  mcYears = "all",
  links_NTC_data = NULL,
  ptdf_FB_data = NULL,
  capacity_FB_data = NULL,
  ts_FB_data = NULL
)
```
**Arguments**

- `sim_opts`:  (string) Simulation options, as returned by antaresRead::setSimulationPath

- `areas`:  (string or vector of strings) what areas the patch should be applied on. Default: ""

- `virtual_areas`:  (string or vector of strings) Virtual areas of the study, excluded from the patch. Default: NULL

- `mcYears`:  (numeric or vector of numeric) The Monte-Carlo years to extract from. The special value "all" extracts all Monte-Carlo Years. Default: "all"

- `links_NTC_data`:  links_NTC_data

- `ptdf_FB_data`:  ptdf_FB_data

- `capacity_FB_data`:  capacity_FB_data

- `ts_FB_data`:  ts_FB_data


**Value**

(data.table) Table giving the MRG, ENS and net-position for each country
at each time-step

**Examples**
```

```


### `run_adq`
**Applies the Adequacy Patch on a study**




 **Usage:**
```
run_adq(
  opts,
  areas,
  virtual_areas,
  mcYears,
  ext = NULL,
  nbcl = 10,
  antaresfbzone = "model_description_fb",
  showProgress = TRUE,
  thresholdFilter = 1e+06
)
```
**Arguments**

- `opts`:  Simulation options, as returned by antaresRead::setSimulationPath

- `areas`:  (string or vector of strings) what areas the patch should be applied on. Default: ""

- `virtual_areas`:  (string or vector of strings) Virtual areas of the study, excluded from the patch. Default: NULL

- `mcYears`:  (numeric or vector of numeric) The Monte-Carlo years to extract from. The special value "all" extracts all Monte-Carlo Years. Default: "all"

- `ext`:  name extand for output study.

- `nbcl`:  numeric, number of process in cluster

- `antaresfbzone`:  antares names of flowbased zone

- `showProgress`:  show progress

- `thresholdFilter`:  filtering to important modification


**Value**



**Examples**
```
opts <- setSimulationPath("path", 4)

areas = c("fr", "lu", "de", "cz", "pl", "ch", "at", "itn", "nl", "be", "es", "non", "se1", "model_description_fb_adq")
virtual_areas = getAreas(select = "_", regexpSelect = TRUE, exclude = c("model_description_fb", "x_open_turb", "x_open_pump"), regexpExclude = FALSE)
run_adq(opts, areas, virtual_areas, 1)
```


### `extract_NTC_links`
**Extracts the NTC links data from a study and formats the like the flow-based data**




 **Usage:**
```
extract_NTC_links(areas = NULL, sim_opts = antaresRead::simOptions())
```
**Arguments**

- `areas`:  (string or vector of strings) Areas between which we want to extract the links.

- `sim_opts`:  (list) Simulation options as given by antaresRead::setSimulationPath


**Value**

(list) such that $capacity is a data.table containing the maximum
transfer capacity for each link (divided in Direct and Indirect)
and $ptdf is a data.table containing, for each link, a PTDF of 1 for the
origin country of the link if it is direct, or for the destination country
if it is indirect.

**Examples**
```
sim_opts = antaresRead::setSimulationPath("path/to/my/simulation")
areas = antaresRead::getAreas()

links_NTC_data = extract_NTC_links(areas=areas, sim_opts=sim_opts)
```


### `.pos`
**Computes the positive part of a numeric.**

The positive part is defined as follows:
.pos(x) = x if x >= 0
.pos(x) = 0 otherwise


 **Usage:**
```
.pos(x)
```
**Arguments**

- `x`:  (numeric)


**Value**

(numeric) the positive part of x

**Examples**
```
.pos(3)  # 3
.pos(-5)  # 5
```

## adq
### Introduction

L’algorithme opérationnel du couplage des marchés Euphémia implémente des règles de « dés-optimisation » permettant de définir le partage de la défaillance entre les zones de marché lorsqu’il y en a (de telle sorte d’assurer une certaine équité dans le partage de la défaillance) : il s’agit de l’adequacy patch. 

Le problème lié à l’absence d’adequacy patch dans les études Antares est devenu visible avec l’introduction de la modélisation Flow-Based. Auparavant, ce problème était contourné par le biais d’un mécanisme de hurdle costs (petits coûts sur les interconnexions) limitant les exports à partir d’une zone défaillante. Or ce contournement ne s’applique pas sur les frontières Flow-Based. 

Qui plus est les règles de partage de la défaillance, même en dehors du domaine Flow-Based ne sont pas correctement pris en compte par les hurdle costs qui priorise le traitement de la défaillance dans les pays directement connectés aux pays disposant de marges, au détriment du traitement de la défaillance dans les pays plus éloignés

Les conséquences sont les suivantes :

* La France peut exporter et se mettre en défaillance de manière artificielle par ses exports ou au contraire importer de façon trop importante d’autres pays et leur transmettre sa défaillance ;
* Le nombre d’heures de défaillance, en France et dans les autres pays européens, n’est pas juste (a priori sous-estimé pour la France) ;  
* Si une zone au moins est en défaillance, les échanges sont faussés. Or la contribution des interconnexions au mécanisme de capacité est aujourd’hui calculée à partir des imports simulés aux heures où la France est en défaillance.

Dans un contexte de déclassement des parcs charbon et nucléaires en France et en Europe, les cas de défaillance simultanées tendent à augmenter. Le problème lié à l’absence d’adequacy patch est en conséquence plus visible. Ainsi, dans l’exercice 2019 et pour les configurations les plus défavorables, la France pouvait exporter dans la moitié des situations de défaillance rencontrées.  

Dans un contexte où les marges de de capacité se réduisent, la question de la gestion de la défaillance simultanée dans les études EOD doit être instruite.

Ce package à été construit pour appliquer l'adquacy patch aux output antares.


### Notice d'utilisation


#### L'utilisation de la fonction `run_adq`

La fonction principale est nommée `run_adq` et permet de lancer l'adequacy patch sur une étude Antares.



La fonction accepte 8 arguments :

* opts
* areas : Areas concernées par l'adquacy patch.
* virtual_areas : Plus utilisé aujourd'hui (à supprimer)
* mcYears : mcYears sur lesquelles appliquer le traitement.
* antaresfbzone : Nom de la zone flow-based
* ext : Nom de l'output pour la sortie après adequacy, si NULL, la sortie sera écrasée
* nbcl : Nombre de coeurs de calcul 
* thresholdFilter : Filtre des résultats (seuil d'accéptabilité)

```r
library(AdequacyPatch)
opts <- setSimulationPath("myoutputstudy")

areas <- c("fr", "at", "be", "de", "nl", "es", "ukgb", "ch", "ie", "itn", "model_description_fb")
virtual_areas = getAreas(select = "_", regexpSelect = TRUE,
                         exclude = c("model_description_fb"), regexpExclude = FALSE)


run_adq(opts = opts,
					areas = areas,
					virtual_areas = virtual_areas,
					mcYears = "all",
					antaresfbzone = "model_description_fb",
					ext = 'adq',
					nbcl = 8, thresholdFilter = 100)



```

####  Les développements complémentaires

Le développement de l'adequacy patch à nécessité d'enrichir le package `antaresEditObject` avec des fonctionnalités pouvant être transposées à d'autres besoins. 

##### Copier une sortie d'étude `copyOutput`

Cette fonctionnalité permet de copier une sortie antares (dans le dossier output) et lui donnant un suffixe pour la renommer.

La fonction accepte deux arguments :

* opts
* extname : Nom du suffixe


```r
library(antaresRead)
## Set simulation path
opts = setSimulationPath(path = "PATH/TO/SIMULATION", simulation = "input")

## Copy study
copyOutput(opts, "_adq")

```

##### Ecrire des output antares `write_output_values`

La fonctionnalité suivante permet d'écrire des output antares à partir d'un readAntares. 

La fonction accepte deux arguments :

* opts
* data : Données issues d'un readAntares et potentiellement modifiées par l'utilisateur.

```r
library(antaresRead)
library(data.table)
opts <- setSimulationPath("PATH/TO/SIMULATION")
data <- readAntares(links = "all", areas = "all", clusters = "all")

###Production of clusters to 0
data$clusters$production <- 0
write_output_values(data)
```

##### Génération à partir des données horraires `computeTimeStampFromHourly`

La fonctionnalité suivante permet de générer les données des différents par de temps à partir des données horaires.

La fonction prends en entrée 5 arguments :

* opts
* mcYears : Les mcyears à traiter.
* nbcl : Pour une utilisation en parallèle, le nombre de cœurs de calcul.
* verbose : Pour la log console.
* type : Type de données à traiter (areas, links, clusters)

```r

library(antaresEditObject)
opts <- setSimulationPath("PATH/TO/SIMULATION")
computeTimeStampFromHourly(opts)

```


##### Construction des mc-all `parallelAggregMcall` & `aggregateResult`

La fonctionnalité suivante permet de reconstruire le mc-all à partir des mc-ind.
La fonction aggregateResult prends en entrée 5 arguments :

* opts
* verbose : Pour la log console.
* filtering : Traiter tout ou un sous sélection de données
* selected : Liste des areas, links et clusters à traiter
* timestep : timestep à traiter.

La fonction parallelAggregMcall permet de lancer aggregateResult pour toute l'étude en parallel (traitement global)


```r
parallelAggregMcall(opts)
```


```r
aggregateResult(opts, filtering = TRUE,
                selected = list(areas = "at"),
                timestep = "annual")
```

## my-vignette
### Bonjour tout le monde

Ma super vignette

