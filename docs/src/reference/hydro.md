# Hydro

## Management options

#### <span class="param-badge badge-bool">bool</span> `Follow load modulation`

Defines whether an ideal seasonal generation profile should somehow follow the load or an ideal seasonal generation profile should remain as close as possible to the natural inflows (i.e. instant generation whenever possible).

#### <span class="param-badge badge-int">int</span> `Inter-daily breakdown`



#### <span class="param-badge badge-int">int</span> `Inter-daily modulation`

For the storage power, the maximum authorized value for the ratio of the daily peak to the average power generated throughout the day.
This parameter is meant to allow simulating different hydro management strategies. 
Extreme cases are: `1` generated power should be constant throughout the day and `24` use of the whole daily energy in one single hour is allowed.

#### <span class="param-badge badge-bool">bool</span> `Reservoir management`

Define whether the storage should be explicitly modeled or not.

#### <span class="param-badge badge-bool">bool</span> `Hard bounds on rules curves`

State whether, beyond the preliminary heuristic stage (if any), 
lower and upper reservoir rule curves should still be taken into account
as constraints in the hydro-thermal unit-commitment and dispatch problems.

#### <span class="param-badge badge-bool">bool</span> `Use heuristic target`

Define whether an "ideal" seasonal generation profile should be heuristically determined or not.

#### <span class="param-badge badge-float">float</span> `Reservoir capacity` (MWh)

Size of the reservoir. 

#### <span class="param-badge badge-int">int</span> `Inter-monthly breakdown`

#### <span class="param-badge badge-int">int</span> `Pumping efficiency ratio`

Setting the value to $r$ means that, for the purpose of storing 1 gravitational MWh, pumps will have to use $1/r$ electrical MWh.

#### <span class="param-badge badge-enum">enum</span> `Initialize reservoir level on`

Date at which the reservoir level should be initialized by a random draw. 
The "initial level" is assumed to follow a "beta" variable with expectation "average level", 
upper bound $U$ (max level), lower bound $L$ (min level), standard deviation $\sigma = (U-L)/3$.
Initialization will occur on the 1st of the month:

- `January`
- `February`
- `March`
- `April`
- `May`
- `June`
- `July`
- `August`
- `September`
- `November`
- `December`

#### <span class="param-badge badge-bool">bool</span> `Use water values`

States whether the energy taken from / stored into the reservoir should be given the reference value defined in the ad hoc table or should be given a zero value.

#### <span class="param-badge badge-bool">bool</span> `Use leeway`

State whether the heuristic hydro ideal target ($HIT$) should be followed exactly or not.

- `False` implies that, in optimization problems, the hydro energy generated throughout the time interval will be subject to an equality constraint, which may include short-term pumping cycles independent of water value: $\sum_{t=1}^{T} \text{hydro(t)} – \sum_{t=1}^T \text{r. pump(t)} = *HIT$.
- `True` with bounds $L$ and $U$, implies that, in optimization problems, the hydro energy generated throughout the time span will be subject to inequality constraints: $L_{HIT} \leq \sum_{t=1}^{T} \text{hydro}(t) \leq U \times HIT$

Independently, short- or long-term pumping may also take place if deemed profitable in the light of water values.

#### <span class="param-badge badge-bool">bool</span> `Power to level modulations`

Define whether the standard maximum daily energy and power credit should be or not multiplied by level-dependent modulation coefficients.

#### <span class="param-badge badge-int">int</span> `Leeway low bound`

Leeway lower bound.

#### <span class="param-badge badge-int">int</span> `Leeway upper bound`

Leeway upper bound.

## Inflow structure

#### <span class="param-badge badge-float">float</span> `Inter-monthly correlation`

The average correlation between the energy of a month and that of the next month.

#### <span class="param-badge badge-matrix">matrix</span> `Inflow pattern`

The average daily pattern of inflows within each month. Each day is given a relative "weight" in the month. If all days are given the same weight, daily energy time-series will be obtained by dividing the monthly energy in equal days. If not, the ratio between two daily energies will be equal to that of the daily weights in the pattern array.

#### <span class="param-badge badge-matrix">matrix</span> `Overall monthly hydro`

The expectations, standard deviations, minimum and maximum values of monthly energies (expressed in MWh), monthly shares of Run of River within the overall hydro monthly inflow.

## Allocation

#### <span class="param-badge badge-matrix">matrix</span> Allocation

Annual inter-area allocation matrix $A(i,j)$ that may be used during a heuristic hydro pre-allocation process, regardless of whether the stochastic time-series generator is used or not. This matrix describes the weights that are given to the loads of areas $i$ in the definition of the monthly and weekly hydro storage generation profiles of areas $j$.
 
## Correlation

#### <span class="param-badge badge-matrix">matrix</span> Correlation

Annual inter-area correlation matrix that will be used by the stochastic generator if it is activated. Correlations are expressed in percentages, hence to be valid this matrix must be symmetric, p.s.d, with a main diagonal of 100s and all terms lying between (-100 ,+100).


## Daily power & energy credits

#### <span class="param-badge badge-matrix">matrix</span> `Credit modulations`

Two level-dependent (101 round percentage values ranging from 0% to 100%) time-series of modulation coefficients defined for either generating or storing (pumping).

These modulations, which can take any positive value, may (depending on the options chosen in the management options Tab) be used to increase (value >1) or to decrease (value <1) the standard credits defined previously for the maximum daily power and energies.

#### <span class="param-badge badge-matrix">matrix</span> `Standard credits`

Two daily time-series (365 values) defined for energy generation/storage (hydro turbines or hydro pumps). Both arrays represent the maximum daily energy (either generated or stored).

For the sake of clarity, maximum daily energies are expressed as a number of hours at maximum power and these values are used along with the Maximum Generation and Maximum Pumping TS's to calculate daily mean energy.

## Reservoir levels

#### <span class="param-badge badge-matrix">matrix</span> Reservoir levels

Hourly time series for the minimum, average and maximum levels set for the reservoir at the beginning of each day, 
expressed in percentage of the overall reservoir volume. The lower and upper level time series form a pair of so-called lower and upper "reservoir rule curves".

Depending on the set of parameters chosen in the **Management options** tab, these rule curves may be used in different ways in the course of both heuristic seasonal hydro pre-allocation process and subsequent weekly optimal hydro-thermal unit-commitment and dispatch process.

## Water values

#### <span class="param-badge badge-matrix">matrix</span> Water values

Marginal values for the stored energy, which depends on the date (365 days) and of the reservoir level (101 round percentage values ranging from 0% to 100%). These values may have different origins. 
They theoretically should be obtained by a comprehensive (dual) stochastic dynamic programming study 
carried out over the whole dataset and dealing simultaneously with all reservoirs.

Depending on the set options chosen in the **Mangement options** tab, 
these values may be used or not in the course of the weekly optimal hydro-thermal unit-commitment and dispatch process.

## Hydro storage

#### <span class="param-badge badge-matrix">matrix</span> Hydro storage

Daily size in (MWh) of hydro storage.

## Run of river

#### <span class="param-badge badge-matrix">matrix</span> Run of river

Hourly time series of power in MW. Run-of-river (RoR) hydroelectric generation is a type of electricity production that relies on the natural flow of a river without significant water storage. Unlike traditional hydroelectric dams, RoR plants generate power continuously based on the river's current water level and flow rate. This makes them highly dependent on seasonal variations and weather conditions, leading to fluctuations in electricity production.

## Min gen

#### <span class="param-badge badge-matrix">matrix</span> Min gen
