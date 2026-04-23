# Renewables

## Parameters

#### `Group`

`enum` Renewables sources:

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

#### `Name`

`string` User defined name of the cluster. 

#### `Enabled`

`bool` Whether this cluster is enabled

#### `TS interpretation`

`enum` The type of data recorded in the time series chronicles. 

- `power-generation`
- `production-factor`

#### `Unit`

`int` Number of units inside the cluster.

#### `Nominal capacity` (MW)

`float` Nominal capacity of a single unit. 

## Time series

#### Time series

`matrix` Hourly time series of Production Factors or Power generations as input for the associated renewable cluster.

