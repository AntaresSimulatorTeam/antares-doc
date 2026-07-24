# Hydro

## Management options

#### Follow load modulation

<span class="param-badge badge-bool">bool</span>
Defines whether the seasonal heuristic target should follow the
residual demand. Used in the [heuristic](hydro-heuristic.md) to dispatch inflows.

#### Inter-daily breakdown

<span class="param-badge badge-float">float</span>
Used in the [heuristic](hydro-heuristic.md) to dispatch the monthly generation target across days, proportionally to the residual demand (the load net of non-dispatchable generation, e.g. run-of-river) raised to the power of this coefficient. If equal to one, inflows are split proportionally to the residual demand; if lower than one, inflows are dispatched more evenly (flatter profile); if greater than one, more importance is given to periods of high residual demand.

#### Intra-daily modulation

<span class="param-badge badge-float">float</span>
Value between 1 and 24, only used in the [optimization](optimization-problem.md) when [`Use heuristic target`](#use-heuristic-target) is enabled. For storage power, this is the maximum authorized ratio between the daily
peak and the average power generated throughout the day. The average power per day is the result of the [heuristic](hydro-heuristic.md) and may not be equal to the real average power. This parameter is meant
to allow simulating different hydro management strategies. Extreme cases are:
`1`, where the generated power must be constant throughout the day, and `24`, where the
whole daily energy may be used within a single hour.

#### Reservoir management

<span class="param-badge badge-bool">bool</span>
Defines whether the storage capacity should be explicitly modeled. Used in both the
[heuristic](hydro-heuristic.md) and the [optimization](optimization-problem.md): if enabled,
the optimization includes a variable storage level.

#### Hard bounds on rules curves

<span class="param-badge badge-bool">bool</span>
States whether, in addition to being targeted on a best-effort basis by the preliminary
[heuristic](hydro-heuristic.md) stage (if any), the lower and upper reservoir rule curves
should also be enforced as hard constraints in the [optimization](optimization-problem.md). This option is not recommended, as it could lead to infeasibility.

#### Use heuristic target

<span class="param-badge badge-bool">bool</span>
Defines whether a seasonal heuristic target should be computed for hydro generation.
See the [heuristic](hydro-heuristic.md) for more details.

#### Reservoir capacity (MWh)

<span class="param-badge badge-float">float</span>
Size of the reservoir. Only used if [`Reservoir management`](#reservoir-management) is enabled, in both the [heuristic](hydro-heuristic.md) and the [optimization](optimization-problem.md).

#### Inter-monthly breakdown

<span class="param-badge badge-int">int</span>
Used in the [heuristic](hydro-heuristic.md) to dispatch the annual inflows across months, proportionally to the residual demand (the load net of non-dispatchable generation, e.g. run-of-river) raised to the power of this coefficient. If equal to one, inflows are split proportionally to the residual demand; if lower than one, inflows are dispatched more evenly (flatter profile); if greater than one, more importance is given to periods of high residual demand.

#### Pumping efficiency ratio

<span class="param-badge badge-float">float</span>
Between 0 and 1. Only used in the [optimization](optimization-problem.md). Setting the value to $r$ means that, for the
purpose of storing 1 gravitational MWh, pumps will have to use $1/r$ electrical MWh.

#### Initialize reservoir level on

<span class="param-badge badge-enum">enum</span>
Month whose 1st day is used to initialize the reservoir level. Only used if
[`Reservoir management`](#reservoir-management) is enabled, in both the
[heuristic](hydro-heuristic.md) and the [optimization](optimization-problem.md).

If the corresponding entry in the [scenario builder](../tutorials/build-scenario.md) is
left to `rand` (the default), the initial level is drawn at random: the "initial level" is
assumed to follow a "beta" variable with expectation "average level", upper bound $U$ (max
level) and lower bound $L$ (min level) — read from the average, maximum and minimum values
of the [`Reservoir levels`](#reservoir-levels) time series on the initialization date — and standard deviation
$\sigma = (U-L)/3$. If a specific value is set instead in the scenario builder, that value
is used directly as the initial reservoir level.

- `January`
- `February`
- `March`
- `April`
- `May`
- `June`
- `July`
- `August`
- `September`
- `October`
- `November`
- `December`

#### Use water values

<span class="param-badge badge-bool">bool</span>
States whether the energy generated from / pumped into the reservoir should be optimized based on the prices defined in the [`Water values`](#water-values) table below.

!!! warning
    When water values are used, compliance with the rule curves is not guaranteed unless
    the [`Hard bounds on rules curves`](#hard-bounds-on-rules-curves) option is activated, and the reservoir level at the
    end of the year will not necessarily be the same as at the beginning.

#### Use leeway

<span class="param-badge badge-bool">bool</span>
States whether, in the [optimization](optimization-problem.md), the heuristic target defined
by the [heuristic](hydro-heuristic.md) should be followed exactly, or within a margin defined by [`Leeway low bound`](#leeway-low-bound) and [`Leeway upper bound`](#leeway-upper-bound). Should be used together with [`Use heuristic target`](#use-heuristic-target), and can be used with or without [`Use water values`](#use-water-values).

#### Power to level modulations

<span class="param-badge badge-bool">bool</span>
Only used in the [optimization](optimization-problem.md). Defines whether the standard maximum generating and pumping power should be multiplied by level-dependent modulation coefficients defined in the [`Credit modulations`](#credit-modulations) table, based on the reservoir level at the beginning of each week.

#### Leeway low bound

<span class="param-badge badge-int">int</span>
Leeway lower bound. See [`Use leeway`](#use-leeway).

#### Leeway upper bound

<span class="param-badge badge-int">int</span>
Leeway upper bound. See [`Use leeway`](#use-leeway).

## Inflow structure

#### Inter-monthly correlation

<span class="param-badge badge-float">float</span>
The average correlation between the energy of a month and that of the next
month. Used to generate inflows if not set by the user.

#### Inflow pattern

<span class="param-badge badge-matrix">matrix</span>
The average daily pattern of inflows within each month. Each day is given a
relative "weight" in the month. If all days are given the same weight, daily
energy time series will be obtained by dividing the monthly energy into equal
days. If not, the ratio between two daily energies will be equal to that of
the daily weights in the pattern array. Used to generate inflows if not set by the user.

#### Overall monthly hydro

<span class="param-badge badge-matrix">matrix</span>
The expectations, standard deviations, minimum and maximum values of monthly
energies (expressed in MWh), and monthly shares of run-of-river (RoR) generation within the overall
monthly hydro inflow. Used to generate inflows and RoR time series if not set by the user.

## Allocation

<span class="param-badge badge-matrix">matrix</span>
Annual inter-area allocation matrix $A(i,j)$ that may be used during a
[heuristic](hydro-heuristic.md) hydro pre-allocation process, regardless of whether the stochastic
time series generator is used or not. This matrix describes the weights that
are given to the residual demand of areas $i$ in the definition of the monthly and
weekly hydro storage generation profiles of areas $j$.

## Correlation

<span class="param-badge badge-matrix">matrix</span>
Annual inter-area correlation matrix that will be used by the stochastic
generator if it is activated. Correlations are expressed as percentages; to be valid,
this matrix must be symmetric, positive semi-definite (PSD), with a main diagonal of 100s
and all terms lying between -100 and +100. Used to generate inflows and RoR time series if not set by the user.

## Daily power & energy credits

A "credit" is the maximum power or energy allowed for hydro generation or pumping. Standard
credits set these maximum values, and credit modulations can adjust them based on the
reservoir level.

#### Credit modulations

<span class="param-badge badge-matrix">matrix</span>
Two level-dependent time series (101 rounded percentage values ranging from 0% to 100%)
of modulation coefficients, defined for either generating or pumping.

These modulations, which can take any positive value, are only used if
[`Power to level modulations`](#power-to-level-modulations) is enabled, in which case they
increase (value > 1) or decrease (value < 1) the standard credits defined below for the
maximum daily power and energy, depending on the reservoir level at the beginning of each week.

#### Standard credits

<span class="param-badge badge-matrix">matrix</span>
Four daily time series (365 values) defined for hourly maximum generation power, daily maximum generation energy, hourly maximum pumping power, and daily maximum pumping energy. Maximum daily energies are expressed as a number of hours at maximum power. These values are used, along with the hourly maximum power, to define a weekly maximum energy bound in the [optimization](optimization-problem.md), and are also used in the [heuristic](hydro-heuristic.md) to define daily and monthly maximum energies.

## Reservoir levels

<span class="param-badge badge-matrix">matrix</span>
Daily time series (365 values) for the minimum, average and maximum levels set for the
reservoir at the beginning of each day, expressed as a percentage of the overall
reservoir volume. The lower and upper level time series form a pair of
curves known as the lower and upper reservoir "rule curves".

Depending on the set of parameters chosen in the **Management options** tab,
these rule curves may be used in different ways in the course of both the [heuristic](hydro-heuristic.md)
seasonal hydro pre-allocation process and the subsequent weekly [optimization](optimization-problem.md). See [`Initialize reservoir level on`](#initialize-reservoir-level-on) for
details on how the initial level is derived, depending on the [scenario builder](../tutorials/build-scenario.md) configuration.

## Water values

<span class="param-badge badge-matrix">matrix</span>
Marginal values for the stored energy, which depend on the date (365 days)
and the reservoir level (100 percentage values ranging from 0% to
100%). These values may have different origins. They should theoretically be
obtained from a comprehensive stochastic dynamic programming study
carried out over the whole dataset and dealing simultaneously with all
reservoirs.
Only used when [`Use water values`](#use-water-values) is enabled.

## Hydro storage

<span class="param-badge badge-matrix">matrix</span>
Hydro inflows for each day. Only used if the generation of hydro time series is disabled;
when enabled, this series is generated by Antares instead, from the
[Inflow structure](#inflow-structure) parameters. Used in both the [heuristic](hydro-heuristic.md) and the [optimization](optimization-problem.md). May be used
immediately to generate energy if [`Follow load modulation`](#follow-load-modulation) is
disabled, or stored in the reservoir to be generated later if [`Follow load modulation`](#follow-load-modulation) or [`Use water values`](#use-water-values) is enabled.

## Run of river

<span class="param-badge badge-matrix">matrix</span>
Hourly time series of power in MW. Only used if the generation of hydro time series is
disabled; when enabled, this series is generated by Antares instead, based on the
run-of-river share defined in [`Overall monthly hydro`](#overall-monthly-hydro). Used in the [optimization](optimization-problem.md), and in the [heuristic](hydro-heuristic.md) to
compute the residual demand. Run-of-river (RoR) hydroelectric
generation is a type of electricity production that relies on the natural flow
of a river without significant water storage. Unlike traditional hydroelectric
dams, RoR plants generate power continuously based on the river's current water
level and flow rate. This makes them highly dependent on seasonal variations
and weather conditions, leading to fluctuations in electricity production.

!!! info
    Run-of-river generation is non-dispatchable. There is no storage of energy.

## Min gen

<span class="param-badge badge-matrix">matrix</span>
Minimum generation to satisfy. Defaults to 0 if not otherwise specified. Used in the [heuristic](hydro-heuristic.md) and in the [optimization](optimization-problem.md).
