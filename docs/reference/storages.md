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
The storage capacity (linked to an 
[hourly modulation of min and max capacities time series](#rule-curves)).

#### Initial level optimized

<span class="param-badge badge-bool">bool</span>
Whether to allow each week to reoptimize the initial storage level.
**In this case the level is discontinuous between weeks.** Otherwise, the
initial level is imposed by the user and is identical each week.

#### Initial level (%)

<span class="param-badge badge-int">int</span>
To be considered only if [**Initial level optimized**](#initial-level-optimized) is disabled. 
In this case corresponds to the ratio of the storage level between empty 0 and full 100.

#### Stored (MW)

<span class="param-badge badge-float">float</span>
Maximum possible power injection in the storage linked to
[hourly modulation of the maximum injection power time series](#stored-modulation).

#### Stored efficiency (%)

<span class="param-badge badge-int">int</span>
Efficiency of the process of injecting power inside the storage. 

#### Released (MW)

<span class="param-badge badge-float">float</span>
Maximum possible power withdrawal from the storage (linked to an 
[hourly modulation of the maximum withdrawal power](#released-modulation)).

#### Released efficiency (%)

<span class="param-badge badge-int">int</span>
Efficiency of the process of withdrawing power from the storage. 

!!! info
    Antares Web doesn't use the terms **Max Injection** for **Stored**
    and **Max withdrawal** for **Released** because it depends whether you do a study
    from the point of view of the grid or from the point of view of the storage.

## Time series

### Modulation

#### Stored modulation

<span class="param-badge badge-matrix">matrix</span>
The values entered are dimensionless decimal numbers, between 0 and 1.
This involves modulation of the injection capacity each hour in the storage, reflecting lower
availability of the storage at certain times (planned or forced outages).

#### Released modulation

<span class="param-badge badge-matrix">matrix</span>
The values entered are dimensionless decimal numbers, between 0 and 1. This
involves modulation of the withdrawal capacity each hour from the storage, reflecting lower
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

!!! info
    Implicit rule for all hours : modulation of min capacity $\leq$ modulation of max capacity

### Inflows

#### Time series (MW)

<span class="param-badge badge-matrix">matrix</span>
Natural inflows in MW that enters into the storage. The values for this file
can be negative, corresponding to withdrawals imposed on the stock for other
uses (for example agricultural withdrawals or imposed discharging of EV
batteries).

## Equations

The goal of Antares is to find the variables:

- $P_{\text{injection}}(h)$
- $P_{\text{withdrawal}}(h)$
- $\text{Level(h)}$

To do that there are a set of equations and inequations.

### Bounds

$$
0 \leq P_{\text{injection}}(h) \leq P_{\text{injection max}}(h)
$$

with:

$$
P_{\text{injection max}}(h) = \text{Injection max power} \times \text{hourly modulation of injection max power } (h)
$$

$$
0 \leq P_{\text{withdrawal}}(h) \leq P_{\text{withdrawal max}}(h)
$$

with:

$$
P_{\text{withdrawal max}}(h) = \text{Withdrawal max power} \times \text{hourly modulation of withdrawal max power } (h)
$$

$$
\text{Level}_{\text{min}}(h) \leq \text{Level}(h) \leq \text{Level}_{\text{max}}(h)
$$

with:

$$
\text{Level}_{\text{min}}(h) = \text{Storage capacity} \times \text{hourly modulation of min capacities } (h)
$$

and 

$$
\text{Level}_{\text{max}}(h) = \text{Storage capacity} \times \text{hourly modulation of max capacities } (h)
$$

### Storage level tracking (dynamic equation)

$$
\text{Level}(h) = \text{Level}(h-1) + P_{\text{injection}}(h) \times \text{efficiency} - P_{\text{withdrawal}}(h) + \text{hourly inflows } (h)
$$

With the implicit convention that the stock level at the end of the week is equal to the initial level:

$$
\text{Level}(168) = \text{Level}(0) \quad (\text{= Initial level} \times \text{Storage capacity})
$$
