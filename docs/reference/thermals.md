# Thermals

A thermal cluster is a grouping of plants with close parameters. 

## Operating parameters

#### <span class="param-badge badge-string">string</span> `Group`

Group in which the cluster is, only for organization purpose.

- `gas`
- `hard coal`
- `lignite`
- `mixed fuel`
- `nuclear`
- `oil`
- `other 1`
- `other 2`
- `other 3`
- `other 4`
- `other 5`

#### <span class="param-badge badge-string">string</span> `Name`

User defined name of the cluster.

#### <span class="param-badge badge-bool">bool</span> `Enabled`

Whether to enable this cluster for production. 

#### <span class="param-badge badge-bool">bool</span> `Must run`

If enabled, the plants will generate at their maximum capacity, regardless of market conditions. Otherwise, above a partial "must-run level" (that may exist or not, see infra) plants will be dispatched on the basis of their market bids.

#### <span class="param-badge badge-int">int</span> `Unit`

The number of units in the cluster. 

#### <span class="param-badge badge-float">float</span> `Nominal capacity` (MW)

The nominal capactity of one unit. 

!!! note

    The installed power is the product of the number of units and their nominal capacity. 

#### <span class="param-badge badge-float">float</span> `Min stable power` (MW)

The minimum power to keep a plant on. 

#### <span class="param-badge badge-int">int</span> `Spinning` (%)

Default contribution to the spinning reserve (percentage of nominal capacity).

#### <span class="param-badge badge-int">int</span> `Min uptime` (h)

Minimum uptime for a plant to go from off to its nominal capacity.

#### <span class="param-badge badge-int">int</span> `Min downtime` (h)

Minimu downtime for a plant to go from its nominal capacity to completly off. 

## Operating costs

#### <span class="param-badge badge-enum">enum</span> `TS cost`

Cost generation

- `SetManually`
- `useCostTimeseries`

!!! note

    If `Cost generation` is set to `SetManually` marginal and market bid costs (€/MWh) are specified directly in **Time series** > **Common** tab and have the same value for all time-series and hours.

    If Cost generation is set to Use cost timeseries Marginal and Market bid costs (€/MWh) are calculated separately for all the time-series and hours using the following equation:
    ```
    Marginal_Cost[€/MWh] = Market_Bid_Cost[€/MWh] = (Fuel_Cost[€/GJ] * 3.6 * 100 / Efficiency[%]) + CO2_emission_factor[tons/MWh] * C02_cost[€/tons] + Variable_O&M_cost[€/MWh]
    ```
    where Efficiency[%], CO2_emission_factor[tons/MWh] and Variable_O&M_cost[€/MWh] are specified in the Common tab under operating costs and parameters, while Fuel_Cost[€/GJ] and C02_cost[€/tons] are provided as time-series in separate tabs.

#### <span class="param-badge badge-int">int</span> `Efficiency` (%)

Fuel efficiency.

#### <span class="param-badge badge-float">float</span> `Variable O&M` (€/MWh)

Variable operation and maintenance costs only use if cost generation is set to use cost timeseries.

#### <span class="param-badge badge-float">float</span> `Marginal cost` (€/MWh)

Marginal cost.

#### <span class="param-badge badge-float">float</span> `Startup cost` (€)

Cost of starting a new plan

#### <span class="param-badge badge-float">float</span> `Market bid cost` (€/MWh)

Market bid cost.

#### <span class="param-badge badge-float">float</span> `Fixed O&M cost` (€/h)

Fixed operation and maintenance costs.

#### <span class="param-badge badge-float">float</span> `Random spread` (€/MWh)

Random spread on the market bid. 

!!! note

    The **optimal dispatch plan** as well as **locational marginal prices** are based on **market bids**, while the assessment of the operating costs associated with this optimum are based on cost parameters. In standard "perfect" market modeling, there is no difference of approaches because market bids are equal to marginal costs.


## Other emission rates

The following parameters allow the user to indicate the rates of emission of different polluants for a given cluster.

#### <span class="param-badge badge-float">float</span> `CO2` (t/MWh)


#### <span class="param-badge badge-float">float</span> `SO2` (t/MWh)


#### <span class="param-badge badge-float">float</span> `NH3` (t/MWh)


#### <span class="param-badge badge-float">float</span> `NOx` (t/MWh)


#### <span class="param-badge badge-float">float</span> `NMVOC` (t/MWh)


#### <span class="param-badge badge-float">float</span> `PM2.5` (t/MWh)


#### <span class="param-badge badge-float">float</span> `PM5` (t/MWh)


#### <span class="param-badge badge-float">float</span> `PM10` (t/MWh)


#### <span class="param-badge badge-float">float</span> `Other polluant 1` (t/MWh)


#### <span class="param-badge badge-float">float</span> `Other polluant 2` (t/MWh)


#### <span class="param-badge badge-float">float</span> `Other polluant 3` (t/MWh)


#### <span class="param-badge badge-float">float</span> `Other polluant 4` (t/MWh)


#### <span class="param-badge badge-float">float</span> `Other polluant 5` (t/MWh)


## Time series generation

#### <span class="param-badge badge-enum">enum</span> `Parameter`

Parameter to specify the behavior of this cluster for time-series generation. **This cluster-wise parameter takes priority over the study-wide one.** It can hold three values:

- `use global`: 
- `force no generation`: time-series for this cluster will not be generated. 
- `force generation`: time-series for this cluster will be generated.

#### <span class="param-badge badge-float">float</span> `Volatility forced`

A parameter between 0 and 1.

#### <span class="param-badge badge-float">float</span> `Volatility planned`

A parameter between 0 and 1.

#### <span class="param-badge badge-enum">enum</span> `Law forced`

Probabilistic law used for the generation of the forced outage time-series.

- `geometric`
- `uniform`

#### <span class="param-badge badge-enum">enum</span> `Law planned`

Probabilistic law used for the generation of the planned outage time-series.

- `geometric`
- `uniform`

## Time series

### Common

`matrix` Hourly time-series for:

- Seasonal evolution of the marginal cost variations (gas more expensive in winter).
- Seasonal market bid modulations (assets costs charging strategy).
- Nominal capacity modulations (seasonal thermodynamic efficiencies, special over-generation allowances, etc.). These modulations are taken into account during the generation of available power time-series.
- Minimal generation commitment (partial must-run level) set for the cluster.

### TS generator

`matrix` Daily time series of:

- Forced outage duration
- Planned outage duration
- Forced outage rate
- Planned outage rate
- Minimum number of units able to go into maintenance at the same time
- Maximum number of units able to go into maintenance at the same time

### Availability

`matrix` Hourly availability of the cluster.

### Fuel cost

`matrix` Hourly fuel cost of the cluster.

### CO2 cost

`matrix` Hourly CO2 cost of the cluster.
