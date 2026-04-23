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

#### `Unsupplied` (€/MWh)

`float` Average cost of failure for each area of the study

#### `Spilled` (€/MWh)

`float` Average cost of spillage for each area of the study.

#### `Spread unsupplied` (€/MWh)

`float` Spread on the cost of failure.

#### `Spread supplied` (€/MWh)

`float` Spread on the cost of spillage.

#### `Non dispatch. power`

`bool` Whether spillage can be performed from must-run production.

#### `Dispatch. hydropower`

`bool` Whether spillage can be performed from hydro production.

#### `Other dispatch. power`

`bool` Whether spillage can be performed from thermal production

#### `Adequacy patch`

`enum` Allow to set the integration or not of the zone in the [adequacy patch](adequacy-patch.md).

- `outside`
- `inside`
- `virtual`
