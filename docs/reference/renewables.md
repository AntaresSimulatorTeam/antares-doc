# Renewables

## Parameters

#### <span class="param-badge badge-enum">enum</span> `Group`

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

#### <span class="param-badge badge-string">string</span> `Name`

User defined name of the cluster. 

#### <span class="param-badge badge-bool">bool</span> `Enabled`

Whether this cluster is enabled

#### <span class="param-badge badge-enum">enum</span> `TS interpretation`

The type of data recorded in the time series chronicles. 

- `power-generation`
- `production-factor`

#### <span class="param-badge badge-int">int</span> `Unit`

Number of units inside the cluster.

#### <span class="param-badge badge-float">float</span> `Nominal capacity` (MW)

Nominal capacity of a single unit. 

## Time series

#### <span class="param-badge badge-matrix">matrix</span> Time series

Hourly time series of Production Factors or Power generations as input for the associated renewable cluster.
