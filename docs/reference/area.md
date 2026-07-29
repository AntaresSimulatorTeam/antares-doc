# Areas

Areas are one of the fundamental objects in Antares alongside links. Areas
correspond to nodes on the map and can be tied to a physical aggregated area.
However, they can represent much more in advanced modelisation.

The equilibrium between supply and demand of electricity must be satisfied
at the node level. That's why you can attach to a map:

- Consumption which is called [load](load.md)
- Generation
    - [Thermal plants](thermals.md)
    - [Renewable](renewables.md) sources
    - [Hydro](hydro.md) objects
    - [Reserves](reserves.md)
    - Other [miscellenous generation](misc-gen.md)
- Storage
    - Short-term [storage](storages.md)
## Properties

#### Unsupplied (€/MWh)

<span class="param-badge badge-float">float</span>
Average cost of failure for each area of the study (or value of lost of load VOLL).

!!! tip
    It is recommended that the unsupplied energy cost is much larger than
    the cost of the most expensive generating plant of the area, otherwise such plant will never be activated.

#### Spilled (€/MWh)

<span class="param-badge badge-float">float</span>
Average cost of spillage for each area of the study.

!!! info
    Even if this parameter is fixed to 0 €/MWh, no energy will be shed needlessly.

#### Spread unsupplied (€/MWh)

<span class="param-badge badge-float">float</span>
Spread on the cost of failure.

#### Spread supplied (€/MWh)

<span class="param-badge badge-float">float</span>
Spread on the cost of spillage.

#### Non dispatch. power

<span class="param-badge badge-bool">bool</span>
Whether spillage can be performed from must-run production.

#### Dispatch. hydropower

<span class="param-badge badge-bool">bool</span>
Whether spillage can be performed from hydro production.

#### Other dispatch. power

<span class="param-badge badge-bool">bool</span>
Whether spillage can be performed from thermal production

#### Adequacy patch

<span class="param-badge badge-enum">enum</span>
Allow to set the integration or not of the zone in the [adequacy patch](adequacy-patch.md).

- `outside`
- `inside`
- `virtual`

## Equations

!!! info
    You can check the section 
    [Balance between load and generation](./optimization-problem.md#balance-between-load-and-generation)
    from the [Optimization problem](./optimization-problem.md) page for details
    about the **equations for a give node.**

2 hourly variables are created per node:

- The hourly spillage power 
- The hourly unsupplied power

4 parameters are created per node :

- Average unsupplied energy cost 
- Average spilled energy cost 
- Spread unsupplied energy cost 
- Spread spilled energy cost 

