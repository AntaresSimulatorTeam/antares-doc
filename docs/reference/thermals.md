# Thermals

A thermal cluster is a grouping of plants with close parameters.

## Parameters

### Operating parameters

#### Group

<span class="param-badge badge-string">string</span>
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

#### Name

<span class="param-badge badge-string">string</span>
User defined name of the cluster.

#### Enabled

<span class="param-badge badge-bool">bool</span>
Whether to enable this cluster for production.

#### Must run

<span class="param-badge badge-bool">bool</span>
If enabled, the plants will generate at their maximum capacity defined in availability time-serie, regardless of
market conditions. Otherwise, above a partial "must-run level" (that may exist
or not, see below), plants will be dispatched on the basis of their market bids.

#### Unit

<span class="param-badge badge-int">int</span>
The number of units in the cluster. Only used to generate time series and to compute the [NODU](./outputs.md#nodu) in the outputs. The number of available units in the optimization is derived from the nominal capacity and the availability time series.

#### Nominal capacity (MW)

<span class="param-badge badge-float">float</span>
The nominal capacity of one unit.

!!! note
    The installed power is the product of the number of units and their nominal capacity. The availability time-serie may exceed the installed power.

#### Min stable power (MW)

<span class="param-badge badge-float">float</span>
The minimum power to keep a plant on.

#### Spinning (%)

<span class="param-badge badge-int">int</span>
Default contribution to the spinning reserve, between 0 and 100 (percentage of nominal capacity).

#### Min uptime (h)

<span class="param-badge badge-int">int</span>
Minimum time a plant must stay on after starting before it can be shut down again.

#### Min downtime (h)

<span class="param-badge badge-int">int</span>
Minimum time a plant must stay off after stopping before it can be started again.

### Operating costs

#### TS cost

<span class="param-badge badge-enum">enum</span>
Cost generation

- `SetManually`
- `useCostTimeseries`

!!! note
    If `Cost generation` is set to `SetManually` marginal and market bid costs (€/MWh)
    are specified directly in **Time series** > **Common** tab and have the same
    value for all time series and hours.

    If `Cost generation` is set to `useCostTimeseries` Marginal and Market bid costs
    (€/MWh) are calculated separately for all the time series and hours using
    the following equation:
    ```
    Marginal_Cost[€/MWh] = Market_Bid_Cost[€/MWh] = (Fuel_Cost[€/GJ] * 3.6 * 100 / Efficiency[%]) + CO2_emission_factor[tons/MWh] * C02_cost[€/tons] + Variable_O&M_cost[€/MWh]
    ```
    where Efficiency[%], CO2_emission_factor[tons/MWh] and Variable_O&M_cost[€/MWh]
    are specified in the Common tab under operating costs and parameters, while
    Fuel_Cost[€/GJ] and C02_cost[€/tons] are provided as time series in separate
    tabs.

#### Efficiency (%)

<span class="param-badge badge-int">int</span>
Fuel efficiency. Only used if `Cost generation` is set to `useCostTimeseries`.

#### Variable O&M (€/MWh)

<span class="param-badge badge-float">float</span>
Variable operation and maintenance costs, only used if `Cost generation` is set to `useCostTimeseries`.

#### Marginal cost (€/MWh)

<span class="param-badge badge-float">float</span>
Marginal cost. Only used to compute operating costs in the outputs.

#### Startup cost (€)

<span class="param-badge badge-float">float</span>
Cost of starting a new plant. Used in the optimization for `accurate` and `milp` mode and in the outputs for all modes.

#### Market bid cost (€/MWh)

<span class="param-badge badge-float">float</span>
Market bid cost. Only used in the optimization for defining operating costs.

#### Fixed O&M cost (€/h)

<span class="param-badge badge-float">float</span>
Fixed operation and maintenance costs.  Used in the optimization for `accurate` and `milp` mode and in the outputs for all modes.

#### Random spread (€/MWh)

<span class="param-badge badge-float">float</span>
Used to define noise on market bid cost in the optimization to avoid equivalent solutions. Even with a null value, a small noise (absolute value between 5e-4 and 6e-4) is applied.

!!! note
    The **optimal dispatch plan** as well as **marginal prices** are
    based on **market bids**, while the assessment of the operating costs
    associated with this optimum are based on cost parameters. In standard
    "perfect" market modeling, there is no difference of approaches because
    market bids are equal to marginal costs.

### Other emission rates

The following parameters allow the user to indicate the rates of emission of
different polluants for a given cluster. They are not used in the optimization.

#### CO2 (t/MWh)

<span class="param-badge badge-float">float</span>
Carbon dioxide emission rate.

#### SO2 (t/MWh)

<span class="param-badge badge-float">float</span>
Sulfur dioxide emission rate.

#### NH3 (t/MWh)

<span class="param-badge badge-float">float</span>
Ammonia emission rate.

#### NOx (t/MWh)

<span class="param-badge badge-float">float</span>
Nitrogen oxides emission rate.

#### NMVOC (t/MWh)

<span class="param-badge badge-float">float</span>
Non-methane volatile organic compounds emission rate.

#### PM2.5 (t/MWh)

<span class="param-badge badge-float">float</span>
Fine particulate matter (diameter below 2.5 µm) emission rate.

#### PM5 (t/MWh)

<span class="param-badge badge-float">float</span>
Particulate matter (diameter below 5 µm) emission rate.

#### PM10 (t/MWh)

<span class="param-badge badge-float">float</span>
Particulate matter (diameter below 10 µm) emission rate.

#### Other polluant 1 (t/MWh)

<span class="param-badge badge-float">float</span>
User defined pollutant emission rate.

#### Other polluant 2 (t/MWh)

<span class="param-badge badge-float">float</span>
User defined pollutant emission rate.

#### Other polluant 3 (t/MWh)

<span class="param-badge badge-float">float</span>
User defined pollutant emission rate.

#### Other polluant 4 (t/MWh)

<span class="param-badge badge-float">float</span>
User defined pollutant emission rate.

#### Other polluant 5 (t/MWh)

<span class="param-badge badge-float">float</span>
User defined pollutant emission rate.

### Time series generation

#### Parameter

<span class="param-badge badge-enum">enum</span>
Parameter to specify the behavior of this cluster for time series generation.
**This cluster-wise parameter takes priority over the study-wide one.**
It can hold three values:

- `use global`: use study parameter
- `force no generation`: time series for this cluster will not be generated.
- `force generation`: time series for this cluster will be generated.

#### Volatility forced

<span class="param-badge badge-float">float</span>
A parameter between 0 and 1.

#### Volatility planned

<span class="param-badge badge-float">float</span>
A parameter between 0 and 1.

#### Law forced

<span class="param-badge badge-enum">enum</span>
Probabilistic law used for the generation of the forced outage time series.

- `geometric`
- `uniform`

#### Law planned

<span class="param-badge badge-enum">enum</span>
Probabilistic law used for the generation of the planned outage time series.

- `geometric`
- `uniform`

## Time series

### Common

<span class="param-badge badge-matrix">matrix</span>
Hourly time series for:

- `Marginal cost modulation` Seasonal evolution of the marginal cost variations (gas more expensive in winter). Used for both values of `Cost generation`.
- `Market bid modulation` Seasonal market bid modulations (assets costs charging strategy). Used for both values of `Cost generation`.
- `Capacity modulation` Nominal capacity modulations (seasonal thermodynamic efficiencies, special
  over-generation allowances, etc.). These modulations are only taken into account
  during the generation of available power time series.
- `Min gen modulation` Minimal generation commitment (partial must-run level) set for the cluster.

### TS generator

<span class="param-badge badge-matrix">matrix</span>
Daily time series of:

- `FO duration` Forced outage duration (in days)
- `PO duration` Planned outage duration (in days)
- `FO rate` Forced outage rate (in $[0,1]$)
- `PO rate` Planned outage rate (in $[0,1]$)
- `NPO min` Minimum number of units able to go into maintenance at the same time
- `NPO max` Maximum number of units able to go into maintenance at the same time

### Availability

<span class="param-badge badge-matrix">matrix</span>
Hourly availability of the cluster. Used in optimization to define maximum generation power and the number of available units.

### Fuel cost

<span class="param-badge badge-matrix">matrix</span>
Hourly fuel cost of the cluster. Only used if [`Cost generation`](#ts-cost) is set to `useCostTimeseries`.

### CO2 cost

<span class="param-badge badge-matrix">matrix</span>
Hourly CO2 cost of the cluster. Only used if [`Cost generation`](#ts-cost) is set to `useCostTimeseries`.
