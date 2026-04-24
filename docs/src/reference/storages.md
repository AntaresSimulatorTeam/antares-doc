# Storages

## Parameters

#### <span class="param-badge badge-enum">enum</span> `Group`

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

#### <span class="param-badge badge-string">string</span> `Name`

User defined name for the cluster.

#### <span class="param-badge badge-bool">bool</span> `Enabled`

Whether to enable this cluster.

#### <span class="param-badge badge-float">float</span> `Stock` (MWh)

The maximum capacity of the storage.

#### <span class="param-badge badge-int">int</span> `Initial level` (%)

To be considered only if `Initial level optimized` is disabled. In this case corresponds to the ratio of the storage level between empty 0 and full 100.

#### <span class="param-badge badge-bool">bool</span> `Initial level optimized`

Whether to allow each week to reoptimize the initial storage level. **In this case the level is discontinuous between weeks.** Otherwise, the initial lelvel is imposed by the user and is identical each week.

#### <span class="param-badge badge-float">float</span> `Stored` (MW)


#### <span class="param-badge badge-int">int</span> `Stored efficiency` (%)


#### <span class="param-badge badge-float">float</span> `Released` (MW)


## Time series

### Modulation

#### <span class="param-badge badge-matrix">matrix</span> `Stored modulation`

The values ​​entered are dimensionless decimal numbers, between 0 and 1. This involves modulation of the injection capacity each hour, reflecting lower availability of the storage at certain times (planned or forced outages).

#### <span class="param-badge badge-matrix">matrix</span> `Released modulation`

the values ​​entered are dimensionless decimal numbers, between 0 and 1. This involves modulation of the withdrawal capacity each hour, reflecting lower availability of the storage at certain times (planned or forced outages).

### Rule curves

#### <span class="param-badge badge-matrix">matrix</span> `Lower rule curve`

The values ​​entered are dimensionless decimal numbers, between 0 and 1. This is the lower limit for filling the stock, expressed as a filling rate, imposed each hour.

#### <span class="param-badge badge-matrix">matrix</span> `Upper rule curve`

The values ​​entered are dimensionless decimal numbers, between 0 and 1. This is the upper limit for filling the stock, expressed as a filling rate, imposed each hour.

### Inflows

#### <span class="param-badge badge-matrix">matrix</span> Time series (MW)

Natural inflows in MW that enters into the storage. The values ​​for this file can be negative, corresponding to withdrawals imposed on the stock for other uses (for example agricultural withdrawals or imposed discharging of EV batteries).
