# Hydro heuristic

## Introduction

The aim of the hydro heuristic is to 
**determine amounts of energy to use from storage for each area for each optimization period** 
(usually one week). This is equivalent to 
**determining initial and final level of the reservoir for each week**. 
See the formulation of the [optimization problem](optimization-problem.md) to see 
how the output from the heuristic is used.

Basically, the seasonal hydro heuristic process comprises **two stages carried out twice** 
(first time at a monthly time scale; second time at a daily time scale) for each area sequentially.

- **Stage 1:** Definition of an **ideal generation profile**, 
  which may be based (or not) on local and/or remote load profiles.
- **Stage 2:** Adjustment of the previous raw profile to obtain a 
  **feasible hydro generation profile**, 
  compatible as much as possible with reservoir constraints through the resolution 
  of an optimization problem.

## Notations

The description given hereafter makes use of the following local notations, 
not to be confused with those of the section [optimization problem](optimization-problem.md) 
(dedicated to the optimal hydro-thermal unit-commitment and dispatch problem). 
As the heuristic is applied for each reservoir independently, 
indexes concerning the studied reservoir are omitted. 
All variables and parameters are local to linear optimization problems 
$M$ and $D(m)$ solved within the heuristic. 
For the sake of clarity, the same generic index is used for all time steps, 
knowing that in $M$ there are 12 monthly time-steps, 
while in $D(m)$ there are from 28 to 31 daily time-steps. 
Time step $t$ could either represent one month $m \in \mathcal{M}$ or one day $d \in \mathcal{D}(m)$.

## Parameters

| Notation | Explanation |
|----------|-------------|
| $\alpha$ | inter-monthly generation breakdown parameter |
| $\beta$ | inter-daily generation breakdown parameter |
| $j$ | follow-load parameter |
| $\mu$ | reservoir-management parameter |
| $m \in \mathcal{M}$ | Months of the year |
| $d \in \mathcal{D}(m)$ | Days of month $m$ |

## Input data

| Notation | Explanation |
|----------|-------------|
| $S$ | Reservoir size |
| $S_0$ | Reservoir initial level at the beginning of the first day of the year |
| $\overline{S_t}, \underline{S_t}$ | Maximum level, minimum level at the end of time step $t$ (please note that rule curves given in the reservoir levels tab corresponds to bounds on the level at the **beginning of each day**) |
| $L_t$ | Weighted net load on time step $t$ for the studied reservoir |
| $\underline{G_t},\overline{G_t}$ | Minimum and maximum generation on time step $t$. Note that power-to-level modulation are not taken into account. |
| $I_t$ | Natural inflow on time step $t$ |

!!! note
    $L_t$ is computed as $L_t = A\tilde{L_t}$ with:

    - $\tilde{L_t}$: the vector of net loads for all areas. 
      The net load for each area corresponds to the difference between the non-flexible load 
      and must-generation of all kinds 
      (renewable production, thermal must-run generation and miscellaneous generation).

    - $A$: the inter-area hydro-allocation matrix for the studied area. 
      $A_u$ is a weight given to the load of area $u$ in the definition of the monthly 
      and daily primary hydro generation target of the studied area. Extreme cases are:
        - $A_u = 1$ if $u$ is the studied area and $A_u = 0$ for all other areas: 
          the hydro storage energy monthly and weekly profiles depend only on the local demand 
          and must-run generation of the studied area.
        - $A_u = 0$ if $u$ is the studied area: the hydro storage energy monthly 
          and weekly profiles do not depend at all on the local demand 
          and must-run generation of the studied area.

## Variables

| Notation | Explanation |
|----------|-------------|
| $G^{k}_t$ | Energy to generate on each time step $t$, at the end of stage $k$ |
| $O_t$ | Overflow from the reservoir on time step $t$ |
| $S_t$ | Optimal stock level at the end of time step $t$ |
| $W_t$ | Amount of generation determined on stage 1 but not used in month $t$ |

Costs $\gamma_{\text{variable}}$ given to the variables are chosen to enforce a logical hierarchy 
of penalties (letting the reservoir overflow is worse than violating rule curves, 
which is worse than deviating from the generation objective assessed in stage 1, etc.).

### General heuristic for each zone

`Initialization`

If $\text{not } \tilde{\mu}$:

$$ S \leftarrow \infty; \quad \underline{S} \leftarrow 0; \quad \overline{S} \leftarrow \infty; \quad S_0 \leftarrow \frac{S}{2} $$

`Step M1`

- If $j$ and $\mu$, $\forall m \in M$:

$$ G^{M1}_m \leftarrow \frac{L_m^\alpha \cdot \left(\sum_{k \in M} I_k\right)}{\sum_{k \in M} L_k^\alpha} $$

- Else: $\forall m \in M$:

$$ G^{M1}_m \leftarrow I_m $$

`Step M2`

- If $\mu$:

$$ G^{M2} \leftarrow \text{Solution of linear problem } O $$

- Else:

$$ G^{M2} \leftarrow G^{M1} $$

`Step D1`

- If $j$: $\forall m \in M$, for all $d \in D(m)$:

$$ G^{D1}_d \leftarrow \frac{L_d^\beta \cdot G^{M2}_m}{\sum_{k \in D(m)} L_k^\beta} $$

- Else: $\forall m \in M$, for all $d \in D(m)$:

$$ G^{D1}_d \leftarrow I_d $$

`Step D2`

- If $\mu$: $\forall m \in M$:

$$ G^{D2}_m \leftarrow \text{Solution of linear problem } O^m $$

- Else: $\forall m \in M$:

$$ G^{D2}_m \leftarrow \text{Solution of a simplified version of linear problem } O^m \text{ without reservoir levels} $$

`End`


In the formulation of the optimal hydro-thermal unit-commitment and dispatch problem, 
the reference hydro energy $HIT$ used to set the right hand sides of the hydro-constraint 
(constraint 17) depends on the value chosen for the optimization preference simplex range 
and is defined as follows:

- **Daily**: for each day $d$, $HIT = G^{D2}_d$
- **Weekly**: for week $\omega$, $HIT = \sum_{d\in\omega} G^{D2}_d$

For versions higher than 9.0, $HIT = \sum_{d\in\omega} (G^{D2}_d + O_d)$

## Optimization problem $\mathcal{O}$

This optimization problem dispatches the generation between months 
while respecting bounds on the reservoir level and on the generation variable. 
The objective is to keep generation variables close to generation targets 
and to keep reservoir level between rule curves.

For the sake of clarity, the optimization problem has been simplified here 
so that intermediate variables enforcing min, max and absolute values are not defined.

$$\begin{aligned}
& \min_{G^{M2}_m, S_m} & & \gamma_{\Delta}\max_m(\|G^{M1}_m-G^{M2}_m\|) + \gamma_Y\max_m(\|\underline{S_m}-S_m\|^+) \\
&&&+\sum_{m}{(\gamma_D \|G^{M1}_m-G^{M2}_m\| + \gamma_{V+} \|S_m-\overline{S_m}\|^+ + \gamma_{V-} \|\underline{S_m}-S_m\|^+)} \\
& \text{subject to} & & 0 \leq S_m \leq S, \; \forall m\\
&&& \underline{G_m} \leq G^{M2}_m \leq \overline{G_m},\; \forall m \\
&&& S_{m} + G^{M1}_{m} - S_{m-1} = I_{m},\; \forall m\in [1,12] \\
&&& S_{12} = S_{0} \\
\end{aligned}$$

For this optimization problem: $\gamma_D = 1$, $\gamma_{\Delta} = 1$, $\gamma_Y = 100000$, $\gamma_{V+} = 100$, $\gamma_{V-} = 100$

## Optimization problem $\mathcal{O}^m$

This optimization problem dispatches the generation of a given month between days 
while respecting bounds on the reservoir level and on the generation variable. 
The generation over the month cannot be greater than the monthly generation found at step D1. 
If the target is not reached at a given month, the surplus is reported to the next month. 
The objective is to keep generation variables close to generation targets, 
to keep reservoir level above the bottom rule curve, 
to minimize overflow and to maximize reservoir level.

For the sake of clarity, the optimization problem has been simplified here 
so that intermediate variables enforcing min, max and absolute values are not defined.

$$\begin{aligned}
& \min_{G^{D2}_d, S_d, O_d} & & \gamma_{\Delta}\max_d(\|\tilde{G}^{D1}_d-G^{D2}_d\|) + \gamma_Y \max_d(\|\underline{S_d}-S_d\|^+) + \gamma_{W}(\sum_{d}\tilde{G}^{D1}_d-\sum_{d}G^{D2}_d) \\
&&&+ \sum_{d}{(\gamma_D \|\tilde{G}^{D1}_d-G^{D2}_d\| + \gamma_{V-} \|\underline{S_d}-S_d\|^+ + \gamma_{O} O_d + \gamma_S S_d)} \\
& \text{subject to} & & 0 \leq S_d \leq S, \; \forall d\\
&&& \underline{G_d} \leq G^{D2}_d \leq \overline{G_d},\; \forall d \\
&&& S_{d} + G^{D2}_{d} + O_d - S_{d-1} = I_{d},\; \forall d \geq 1 \\
&&& \sum_{d}\tilde{G}^{D1}_d \geq \sum_{d}G^{D2}_d \\
\end{aligned}$$

$$\tilde{G}^{D1}_d = G^{D1}_d + \frac{W_{m-1}}{\|d \in m\|} \text{ with } W_{m-1} = 0 \text{ if } m=1 \text{ else } W_{m-1}=\sum_{d\in \mathcal{D}(m-1)}\tilde{G}^{D1}_d-\sum_{d \in \mathcal{D}(m-1)}G^{D2}_d$$

In the third constraint, $S_{d-1}$ when $d=1$ is the initial stock $S_0$ 
if $m=1$ else it is the final stock level found in the resolution 
of the optimization problem $\mathcal{O}^{m-1}$.

For this optimization problem: $\gamma_D = 1$, $\gamma_{\Delta} = 2$, $\gamma_Y = 68$, $\gamma_W$, $\gamma_{V-} = 68$, $\gamma_O = 32 \times 68 + 1$, $\gamma_{S} = -1/32$, $\gamma_W$ depends on the hydro-heuristic-policy parameter (see above).

## Optimization problem $\mathcal{O}^m$ simplified without reservoir levels

$$\begin{aligned}
& \min_{G^{D2}_d} & & \max_d(\|G^{D1}_d-G^{D2}_d\|^+) + (\sum_{d}G^{D1}_d-\sum_{d}G^{D2}_d) \\
& \text{subject to} & & \underline{G_d} \leq G^{D2}_d \leq \overline{G_d},\; \forall d \\
&&& \sum_{d}G^{D2}_d \leq \sum_{d}G^{D1}_d\\
\end{aligned}$$

!!! warning
    Pumping capacity is not considered in this heuristic. 
    This is equivalent to saying that pumping is only used to optimize inside the week 
    and not at the annual scale. However, if one wants to take into account 
    the pumping capacity in the heuristic, it is possible to modify the model of the storage 
    to put the pumping capacity inside the generating capacity, to add inflows equal to 
    the pumping capacity and to add the pumping capacity to the load of the area.

## Details on the hydro-heuristic-policy parameter

This parameter can take two values: **Accommodate rule curves** (default) or **Maximize generation**.

### General

This parameter is meant to define how the reservoir level should be managed throughout the year, 
either with emphasis put on the respect of rule curves 
or on the maximization of the use of natural inflows.

### Accommodate rule curves

Upper and lower rule curves are accommodated in both monthly and daily heuristic stages. 
In the second stage, violations of the lower rule curve are avoided 
as much as possible ($\gamma_W = 34 \leq \gamma_Y$). This policy may result 
in a restriction of the overall yearly energy generated from the natural inflows.

### Maximize generation

Upper and lower rule curves are accommodated in both monthly and daily heuristic stages. 
In the second stage, incomplete use of natural inflows is avoided as much as possible 
($\gamma_W = 33\times 68 \geq \gamma_Y$).
This policy may result in violations of the lower rule curve.
