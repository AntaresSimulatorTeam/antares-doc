# Thermals

A thermal cluster is a grouping of plants with close parameters. 

## Operating parameters

#### `Group`

`string` Group in which the cluster is, only for organization purpose.

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

#### `Name`

`string` User defined name of the cluster.

#### `Enabled`

`bool` Whether to enable this cluster for production. 

#### `Must run`

`bool` If enabled, the plants will generate at their maximum capacity, regardless of market conditions. Otherwise, above a partial "must-run level" (that may exist or not, see infra) plants will be dispatched on the basis of their market bids.

#### `Unit`

`int` The number of units in the cluster. 

#### `Nominal capacity` (MW)

`float` The nominal capactity of one unit.

!!! note

    The installed power is the product of the number of units and their nominal capacity. 

#### `Min stable power` (MW)

`float` The minimum power to keep a plant on. 

#### `Spinning` (%)

`int` Default contribution to the spinning reserve (percentage of nominal capacity).

#### `Min uptime` (h)

`int` Minimum uptime for a plant to go from off to its nominal capacity.

#### `Min downtime` (h)

`int` Minimu downtime for a plant to go from its nominal capacity to completly off. 

## Operating costs

#### `TS cost`

`enum` Cost generation

- `SetManually`
- `useCostTimeseries`

!!! note

    If `Cost generation` is set to `SetManually` marginal and market bid costs (€/MWh) are specified directly in **Time series** > **Common** tab and have the same value for all time-series and hours.

    If Cost generation is set to Use cost timeseries Marginal and Market bid costs (€/MWh) are calculated separately for all the time-series and hours using the following equation:
    ```
    Marginal_Cost[€/MWh] = Market_Bid_Cost[€/MWh] = (Fuel_Cost[€/GJ] * 3.6 * 100 / Efficiency[%]) + CO2_emission_factor[tons/MWh] * C02_cost[€/tons] + Variable_O&M_cost[€/MWh]
    ```
    where Efficiency[%], CO2_emission_factor[tons/MWh] and Variable_O&M_cost[€/MWh] are specified in the Common tab under operating costs and parameters, while Fuel_Cost[€/GJ] and C02_cost[€/tons] are provided as time-series in separate tabs.

#### `Efficiency` (%)

`int` Fuel efficiency.

#### `Variable O&M` (€/MWh)

`float` Variable operation and maintenance costs only use if cost generation is set to use cost timeseries.

#### `Marginal cost` (€/MWh)

`float` Marginal cost.

#### `Startup cost` (€)

`float` Cost of starting a new plan

#### `Market bid cost` (€/MWh)

`float` Market bid cost.

#### `Fixed O&M cost` (€/h)

`float` Fixed operation and maintenance costs.

#### `Random spread` (€/MWh)

`float` Random spread on the market bid. 

!!! note

    The **optimal dispatch plan** as well as **locational marginal prices** are based on **market bids**, while the assessment of the operating costs associated with this optimum are based on cost parameters. In standard "perfect" market modeling, there is no difference of approaches because market bids are equal to marginal costs.


## Other emission rates

The following parameters allow the user to indicate the rates of emission of different polluants for a given cluster.

#### `CO2` (t/MWh)

`float`

#### `SO2` (t/MWh)

`float`

#### `NH3` (t/MWh)

`float`

#### `NOx` (t/MWh)

`float`

#### `NMVOC` (t/MWh)

`float`

#### `PM2.5` (t/MWh)

`float`

#### `PM5` (t/MWh)

`float`

#### `PM10` (t/MWh)

`float`

#### `Other polluant 1` (t/MWh)

`float`

#### `Other polluant 2` (t/MWh)

`float`

#### `Other polluant 3` (t/MWh)

`float`

#### `Other polluant 4` (t/MWh)

`float`

#### `Other polluant 5` (t/MWh)

`float`

## Time series generation

#### `Parameter`

`enum` Parameter to specify the behavior of this cluster for time-series generation. **This cluster-wise parameter takes priority over the study-wide one.** It can hold three values:

- `use global`: 
- `force no generation`: time-series for this cluster will not be generated. 
- `force generation`: time-series for this cluster will be generated.

#### `Volatility forced`

`float` A parameter between 0 and 1.

#### `Volatility planned`

`float` A parameter between 0 and 1.

#### `Law forced`

`enum` Probabilistic law used for the generation of the forced outage time-series.

- `geometric`
- `uniform`

#### `Law planned`

`enum` Probabilistic law used for the generation of the planned outage time-series.

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
