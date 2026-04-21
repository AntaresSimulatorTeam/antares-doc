technicals# Areas

Areas are one of the fundamental objects in Antares alongside links. Areas correspond to nodes on the map and can be tied to a physical aggregated area.
However, they can represent much more in advanced modelisation: water reservoirs... TODO: add more examples

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

`float`

#### `Spilled` (€/MWh)

`float`

#### `Spread unsupplied` (€/MWh)

`float`

#### `Spread supplied` (€/MWh)

`float`

#### `Non dispatch. power`

`bool`

#### `Dispatch. hydropower`

`bool`

#### `Other dispatch. power`

`bool`

#### `Adequacy patch`

`enum`

- `outside`
- `inside`
- `virtual`
