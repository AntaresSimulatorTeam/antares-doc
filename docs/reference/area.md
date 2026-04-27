# Areas

Areas are one of the fundamental objects in Antares alongside links. Areas correspond to nodes on the map and can be tied to a physical aggregated area.
However, they can represent much more in advanced modelisation.

The equilibrium between supply and demand of electricity must be satisfied at the node level. That's why you can attach to a map:

- Consumption which is called [load](load.md)
- Generation
    - [Thermal plants](thermals.md)
    - Short-term [storage](storages.md)
    - [Renewable](renewables.md) sources
    - [Hydro](hydro.md) objects
    - [Reserves](reserves.md) 
    - Other [miscellenous generation](misc-gen.md)

## Properties

#### <span class="param-badge badge-float">float</span> `Unsupplied` (€/MWh)

Average cost of failure for each area of the study

#### <span class="param-badge badge-float">float</span> `Spilled` (€/MWh)

Average cost of spillage for each area of the study.

#### <span class="param-badge badge-float">float</span> `Spread unsupplied` (€/MWh)

Spread on the cost of failure.

#### <span class="param-badge badge-float">float</span> `Spread supplied` (€/MWh)

Spread on the cost of spillage.

#### <span class="param-badge badge-bool">bool</span> `Non dispatch. power`

Whether spillage can be performed from must-run production.

#### <span class="param-badge badge-bool">bool</span> `Dispatch. hydropower`

Whether spillage can be performed from hydro production.

#### <span class="param-badge badge-bool">bool</span> `Other dispatch. power`

Whether spillage can be performed from thermal production

#### <span class="param-badge badge-enum">enum</span> `Adequacy patch`

Allow to set the integration or not of the zone in the [adequacy patch](adequacy-patch.md).

- `outside`
- `inside`
- `virtual`
