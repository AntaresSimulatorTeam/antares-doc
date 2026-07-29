# Renewables
## Main characteristics of the object

Antares offers heterogeneous possibilities to refine the modelling of a production park according to its nature. Thus, for Renewable Energy Sources (RES), it is possible, via the cluster concept, to create several subsets of production means with specific characteristics, for the same area (or node). Another historical modeling exists for such RES objects, it is an aggregate view of wind and solar generation per node (see [Wind & solar page](wind-and-solar.md)).

There is a restriction for the cluster modelling : only "Ready made" type "Times-Series" are authorized to parameterize the production chronicles of these clusters. Indeed, the "Times-Series Analyser" and "Times-Series Generator" modules only produce aggregated TS of wind or solar generation for each of the nodes in the study area.

Thanks to renewable clusters, it is possible to dissociate a set of given production assets, attached to the same modelling area, according to criteria such as :

- Technology (depending on technological progress, some renewable assets can have very different load factors for the same weather forcing)
- Location (for example, the on-shore/off-shore distinction for wind power or the grouping of structures by geographical sub-sectors can make it possible to calibrate specific weather forcings).

With such RES object, there is no impact on the optimization problem solved at the simulation stage, since this renewable production will be considered as non-dispatchable and is fully deducted from the demand, to constitute a single residual demand chronicle to be satisfied by node.

Cluster modelling brings a significant evolution in the Antares data model that has an impact on the Input/Output data formats and in the User Interface (see [next chapter](wind-and-solar.md)) and this can lead to a significant increase in the memory space occupied by a study.

In addition, similar to what exists for thermal clusters, cluster modelling allows to carry out an intermediate grouping of the different clusters via the definition of categories (or "groups"). From then on, certain information available at the output of Antares will be developed at the level of the new categories proposed.

## Switching between "Renewable clusters" and "Wind & solar aggregated" modeling
There is a cohabitation of the 2 models. The choice of renewable generation modeling is made through an advanced parameter, "Renewable Generation modeling" which can take one of the following 2 values:

- Aggregated (default value)
- Clusters
   
Remarque JMJ : mettre la vue de l'écran "AntaresWeb"

Please note that the renewable generation data loaded or developed in Antares for a modeling will not be switched to the other modeling when this parameter is modified, they will simply be ignored. However, they will not be lost and will be visible again and taken into account during the reverse switch (they are stored in different directories in the "input" folder of an Antares study).

Selecting the "Aggregated" value will lead to keeping the representation of historical renewable production in Antares.

Selecting the "Clusters" value will allow access to the new representation.

## Parameters

#### Group

<span class="param-badge badge-enum">enum</span>
Renewables sources:

- `wind onshore`
- `wind offshore`
- `solar thermal`
- `solar pv`
- `solar rooftop`
- `other res 1`
- `other res 2`
- `other res 3`
- `other res 4`
- `other res 5`

#### Name

<span class="param-badge badge-string">string</span>
User defined name of the cluster.

#### Enabled

<span class="param-badge badge-bool">bool</span>
Whether this cluster is enabled

#### TS interpretation

<span class="param-badge badge-enum">enum</span>
The type of data recorded in the time series chronicles.

- `power-generation`
- `production-factor`

#### Unit

<span class="param-badge badge-int">int</span>
Number of units inside the cluster.

Note that this setting allows you to explicitly divide your cluster into a set of identical units and specify the nominal capacity of each.
However, this feature does not affect the resolution behavior. Therefore, these 2 sets are equivalent :
- Unit = n / Nominal capacity = x
- Unit = 1 / Nominal capacity = n*x

#### Nominal capacity (MW)

<span class="param-badge badge-float">float</span>
Nominal capacity of a single unit.

## Time series

#### Time series

<span class="param-badge badge-matrix">matrix</span>
Hourly time series of Production Factors or Power generations as input for
the associated renewable cluster.
