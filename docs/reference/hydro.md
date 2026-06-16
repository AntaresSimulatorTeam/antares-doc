# Hydro

## Management options

#### Follow load modulation

<span class="param-badge badge-bool">bool</span>
Defines whether an ideal seasonal generation profile should somehow follow the
load or an ideal seasonal generation profile should remain as close as possible
to the natural inflows (i.e. instant generation whenever possible).

#### Inter-daily breakdown

<span class="param-badge badge-int">int</span>

#### Inter-daily modulation

<span class="param-badge badge-int">int</span>
For the storage power, the maximum authorized value for the ratio of the daily
peak to the average power generated throughout the day. This parameter is meant
to allow simulating different hydro management strategies. Extreme cases are:
`1` generated power should be constant throughout the day and `24` use of the
whole daily energy in one single hour is allowed.

#### Reservoir management

<span class="param-badge badge-bool">bool</span>
Define whether the storage should be explicitly modeled or not.
If enabled:

```
level(t) = level(t-1) - H. STOR(t) + efficiency * H. PUMP(t) + H. INFL(t) – H. OVF(t)​
0 <= level(t) <= storage capacity
```

The initial level is randomly choosed between low and high rule curves of the first day
See [outputs](outputs.md) for the definition of `H. STOR`, `H. PUMP`, `H. INFL` and `H. OVF`.

#### Hard bounds on rules curves

<span class="param-badge badge-bool">bool</span>
State whether, beyond the preliminary heuristic stage (if any),
lower and upper reservoir rule curves should still be taken into account
as constraints in the hydro-thermal unit-commitment and dispatch problems.

#### Use heuristic target

<span class="param-badge badge-bool">bool</span>
Define whether an "ideal" seasonal generation profile should be heuristically
determined or not.

#### Reservoir capacity (MWh)

<span class="param-badge badge-float">float</span>
Size of the reservoir.

#### Inter-monthly breakdown

<span class="param-badge badge-int">int</span>

#### Pumping efficiency ratio

<span class="param-badge badge-int">int</span>
Setting the value to $r$ means that, for the purpose of storing 1 gravitational
MWh, pumps will have to use $1/r$ electrical MWh.

#### Initialize reservoir level on

<span class="param-badge badge-enum">enum</span>
Date at which the reservoir level should be initialized by a random draw.
The "initial level" is assumed to follow a "beta" variable with expectation
"average level", upper bound $U$ (max level), lower bound $L$ (min level),
standard deviation $\sigma = (U-L)/3$. Initialization will occur on the 1st
of the month:

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

#### Use water values

<span class="param-badge badge-bool">bool</span>
States whether the energy taken from / stored into the reservoir should be
given the reference value defined in the ad hoc table or should be given a
zero value.

!! warning
    When water values are used, the respect of rule curves is not guaranteed unless 
    the “hard bounds on rule curves” option is activated, 
    and the reservoir level at the end of the year will not necessarily 
    be the same as at the beginning!​

#### Use leeway

<span class="param-badge badge-bool">bool</span>
State whether the heuristic hydro ideal target ($HIT$) should be followed
exactly or not.

- `False` implies that, in optimization problems, the hydro energy generated
  throughout the time interval will be subject to an equality constraint, which
  may include short-term pumping cycles independent of water value:
  $\sum_{t=1}^{T} \text{hydro(t)} – \sum_{t=1}^T \text{r. pump(t)} = *HIT$.
- `True` with bounds $L$ and $U$, implies that, in optimization problems, the
  hydro energy generated throughout the time span will be subject to inequality
  constraints: $L_{HIT} \leq \sum_{t=1}^{T} \text{hydro}(t) \leq U \times HIT$

Independently, short- or long-term pumping may also take place if deemed
profitable in the light of water values.

#### Power to level modulations

<span class="param-badge badge-bool">bool</span>
Define whether the standard maximum daily energy and power credit should be or
not multiplied by level-dependent modulation coefficients.

#### Leeway low bound

<span class="param-badge badge-int">int</span>
Leeway lower bound.

#### Leeway upper bound

<span class="param-badge badge-int">int</span>
Leeway upper bound.

## Inflow structure

#### Inter-monthly correlation

<span class="param-badge badge-float">float</span>
The average correlation between the energy of a month and that of the next
month.

#### Inflow pattern

<span class="param-badge badge-matrix">matrix</span>
The average daily pattern of inflows within each month. Each day is given a
relative "weight" in the month. If all days are given the same weight, daily
energy time series will be obtained by dividing the monthly energy in equal
days. If not, the ratio between two daily energies will be equal to that of
the daily weights in the pattern array.

#### Overall monthly hydro

<span class="param-badge badge-matrix">matrix</span>
The expectations, standard deviations, minimum and maximum values of monthly
energies (expressed in MWh), monthly shares of Run of River within the overall
hydro monthly inflow.

## Allocation

#### Allocation

<span class="param-badge badge-matrix">matrix</span>
Annual inter-area allocation matrix $A(i,j)$ that may be used during a
heuristic hydro pre-allocation process, regardless of whether the stochastic
time series generator is used or not. This matrix describes the weights that
are given to the loads of areas $i$ in the definition of the monthly and
weekly hydro storage generation profiles of areas $j$.

## Correlation

#### Correlation

<span class="param-badge badge-matrix">matrix</span>
Annual inter-area correlation matrix that will be used by the stochastic
generator if it is activated. Correlations are expressed in percentages, hence
to be valid this matrix must be symmetric, p.s.d, with a main diagonal of 100s
and all terms lying between (-100 ,+100).

## Daily power & energy credits

#### Credit modulations

<span class="param-badge badge-matrix">matrix</span>
Two level-dependent (101 round percentage values ranging from 0% to 100%)
time series of modulation coefficients defined for either generating or
storing (pumping).

These modulations, which can take any positive value, may (depending on the
options chosen in the management options Tab) be used to increase (value >1)
or to decrease (value <1) the standard credits defined previously for the
maximum daily power and energies.

#### Standard credits

<span class="param-badge badge-matrix">matrix</span>
Two daily time series (365 values) defined for energy generation/storage (hydro
turbines or hydro pumps). Both arrays represent the maximum daily energy (either
generated or stored).

For the sake of clarity, maximum daily energies are expressed as a number of
hours at maximum power and these values are used along with the Maximum
Generation and Maximum Pumping TS's to calculate daily mean energy.

## Reservoir levels

#### Reservoir levels

<span class="param-badge badge-matrix">matrix</span>
Hourly time series for the minimum, average and maximum levels set for the
reservoir at the beginning of each day, expressed in percentage of the overall
reservoir volume. The lower and upper level time series form a pair of
so-called lower and upper "reservoir rule curves".

Depending on the set of parameters chosen in the **Management options** tab,
these rule curves may be used in different ways in the course of both heuristic
seasonal hydro pre-allocation process and subsequent weekly optimal
hydro-thermal unit-commitment and dispatch process.

## Water values

#### Water values

<span class="param-badge badge-matrix">matrix</span>
Marginal values for the stored energy, which depends on the date (365 days)
and of the reservoir level (101 round percentage values ranging from 0% to
100%). These values may have different origins. They theoretically should be
obtained by a comprehensive (dual) stochastic dynamic programming study
carried out over the whole dataset and dealing simultaneously with all
reservoirs.

Depending on the set options chosen in the **Mangement options** tab,
these values may be used or not in the course of the weekly optimal
hydro-thermal unit-commitment and dispatch process.

## Hydro storage

#### Hydro storage (MWh)

<span class="param-badge badge-matrix">matrix</span>
Hydro storage energy generated for each day (if [**Follow load**](#follow-load-modulation)
is enabled) or daily inflows (if [**Follow load**](#follow-load-modulation)
is disabled).

## Run of river

#### Run of river

<span class="param-badge badge-matrix">matrix</span>
Hourly time series of power in MW. Run-of-river (RoR) hydroelectric
generation is a type of electricity production that relies on the natural flow
of a river without significant water storage, not considered in the modelling. 
Unlike traditional hydroelectricdams, RoR plants generate power continuously based 
on the river's current water level and flow rate, considered as stochastic input data, like other RES generation. 
This makes them highly dependent on seasonal variations and weather conditions, leading to fluctuations in electricity production.

!!! info 
    The run of river is a non dispatchable generation. There is no storage of energy.
    Like other RES, it can be curtailed. 
    This curtailment is not yet implemented in Antares, a post treatment is necessary to convert spillage (area variable) into RES curtailment. 

Remarque JMJ : comme pour tous les autres objets, ce serait bien de préciser dans quelles équations mathématiques les paramètres du RoR interviennent.

## Min gen

#### Min gen

<span class="param-badge badge-matrix">matrix</span>
Minimum generation to satisfy. It defaults to 0 if it's not changed.
