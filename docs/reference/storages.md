# Storages

## Parameters

#### Group

<span class="param-badge badge-enum">enum</span>
The type of storage for aggregation in the general values output:

- `psp_open`
- `psp_closed`
- `pondage`
- `battery`
- `other1`
- `other2`
- `other3`
- `other4`
- `other5`

#### Name

<span class="param-badge badge-string">string</span>
User defined name for the cluster.

#### Enabled

<span class="param-badge badge-bool">bool</span>
Whether to enable this cluster.

#### Stock (MWh)

<span class="param-badge badge-float">float</span>
The maximum capacity of the storage.

#### Initial level (%)

<span class="param-badge badge-int">int</span>
To be considered only if Initial level optimized is disabled. In this case
corresponds to the ratio of the storage level between empty 0 and full 100.

#### Initial level optimized

<span class="param-badge badge-bool">bool</span>
Whether to allow each week to reoptimize the initial storage level.
**In this case the level is discontinuous between weeks.** Otherwise, the
initial level is imposed by the user and is identical each week.

#### Stored (MW)

<span class="param-badge badge-float">float</span>

#### Stored efficiency (%)

<span class="param-badge badge-int">int</span>

#### Released (MW)

<span class="param-badge badge-float">float</span>

## Time series

### Modulation

#### Stored modulation

<span class="param-badge badge-matrix">matrix</span>
The values entered are dimensionless decimal numbers, between 0 and 1.
This involves modulation of the injection capacity each hour, reflecting lower
availability of the storage at certain times (planned or forced outages).

#### Released modulation

<span class="param-badge badge-matrix">matrix</span>
The values entered are dimensionless decimal numbers, between 0 and 1. This
involves modulation of the withdrawal capacity each hour, reflecting lower
availability of the storage at certain times (planned or forced outages).

### Rule curves

#### Lower rule curve

<span class="param-badge badge-matrix">matrix</span>
The values entered are dimensionless decimal numbers, between 0 and 1.
This is the lower limit for filling the stock, expressed as a filling rate,
imposed each hour.

#### Upper rule curve

<span class="param-badge badge-matrix">matrix</span>
The values entered are dimensionless decimal numbers, between 0 and 1.
This is the upper limit for filling the stock, expressed as a filling rate,
imposed each hour.

### Inflows

#### Time series (MW)

<span class="param-badge badge-matrix">matrix</span>
Natural inflows in MW that enters into the storage. The values for this file
can be negative, corresponding to withdrawals imposed on the stock for other
uses (for example agricultural withdrawals or imposed discharging of EV
batteries).
