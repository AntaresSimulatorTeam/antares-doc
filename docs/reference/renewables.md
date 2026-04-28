# Renewables

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

#### Nominal capacity (MW)

<span class="param-badge badge-float">float</span>
Nominal capacity of a single unit.

## Time series

#### Time series

<span class="param-badge badge-matrix">matrix</span>
Hourly time series of Production Factors or Power generations as input for
the associated renewable cluster.
