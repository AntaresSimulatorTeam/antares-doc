# Storages

Storages allow to represent the management of any short-term storage 
with the following main characteristics :

- Storages managed on cycles that are sub-multiples of the Antares optimization
  window (week or day) - by cycle we mean that at the end of the cycle 
  the stock must return to the level at the start of the cycle.
- Rule curves that frame the admissible levels hour by hour,
  the authorized range is a subset of the 0-100 range 
- Maximum power chronicles for storage and releasing
- Natural inflows (case of open cycle Pump-Storage Plants)

In order to control the trajectory of each storage 
and discriminate between equivalent solutions, it is possible since v9.2 to add:

- [Penalties](#penalty-model)
- [Constraints](#additional-constraint-model)

Multiple short-term storages can be created by considering the following relationships :

- Each storage belongs to a given node
- Each node can contain several storages

## Parameters

### Operating parameters
Remarque générale : il faudrait préciser l'existence ou non d'une valeur par défaut et dans ce cas sa valeur.
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
User defined name for the storage cluster.

#### Enabled

<span class="param-badge badge-bool">bool</span>
Whether to enable this cluster.

#### Stock (MWh)

<span class="param-badge badge-float">float</span>
Nominal maximum storage capacity $S_\text{max}$ 
This capacity corresponds to the volume stored when the reservoir is full.
A fluctuating restriction can be defined (linked to an 
[hourly modulation of min and max capacities time series](#rule-curves)).

#### Initial level optimized

<span class="param-badge badge-bool">bool</span>
Whether to allow each week to reoptimize the initial storage level.
**In this case the level is discontinuous between weeks.** Otherwise, the
initial level is imposed by the user and is identical each week.

#### Initial level (%)

<span class="param-badge badge-int">int</span>
To be considered only if [**Initial level optimized**](#initial-level-optimized) is disabled ($p_0$). 
In this case corresponds to the ratio of the storage level between empty 0 and full 100.

### Stored parameters

#### Stored (MW)

<span class="param-badge badge-float">float</span>
Nominal maximum power injection $P_\text{stored}^\text{max}$ in the storage. A fluctuating restriction can be defined, linked to
[hourly modulation of the maximum injection power time series](#stored-modulation).

#### Stored efficiency (%)

<span class="param-badge badge-int">int</span>
Efficiency $e_\text{stored}$ of the process of injecting power inside the storage. 
This is the ratio between the stored energy and the energy taken from the system.
This ratio should be lower or equal to 1.

#### Penalty on injection variation

<span class="param-badge badge-bool">bool</span>
Whether to penalize the variation in the injection flowrate.
If "true", new variables to penalize the variation in the injection flowrate are created. 

### Released parameters

#### Released (MW)

<span class="param-badge badge-float">float</span>
Maximum possible power withdrawal $P_\text{released}^\text{max}$ from the storage A fluctuating restriction can be defined, linked to an 
[hourly modulation of the maximum withdrawal power](#released-modulation).

#### Released efficiency (%)

<span class="param-badge badge-int">int</span>
Efficiency $e_\text{released}$ of the process of withdrawing power from the storage. 
This is the ratio between the energy withdrawn from storage to the energy returned to the system.
This ratio should be greater or equal than 1.

#### Penalty on withdrawal variation

<span class="param-badge badge-bool">bool</span>
Whether to penalize the variation in the withdrawal flowrate.
If "true", new variables to penalize the variation in the withdrawal flowrate are created. 

!!! info
    Antares Web doesn't use the terms **Max Injection** for **Stored**
    and **Max withdrawal** for **Released** because it depends whether you do a study
    from the point of view of the grid or from the point of view of the storage.

## Time series

### Modulation

#### Stored modulation

<span class="param-badge badge-matrix">matrix</span>
The entered values $\text{mod}_\text{stored}(h)$ are dimensionless decimal numbers, between 0 and 1.
They represent an hourly modulation of the storage injection capacity, reflecting reduced
availability at certain times (planned or forced outages).

#### Released modulation

<span class="param-badge badge-matrix">matrix</span>
The entered values $\text{mod}_\text{released}(h)$ are dimensionless decimal numbers, between 0 and 1. 
They represent an hourly modulation of the storage withdrawal capacity, reflecting reduced
availability at certain times (planned or forced outages).

### Rule curves

#### Lower rule curve

<span class="param-badge badge-matrix">matrix</span>
The entered values $S_\text{lower}(h)$ are dimensionless decimal numbers, between 0 and 1.
This is the lower limit for filling the stock, expressed as a filling rate,
imposed each hour.

#### Upper rule curve

<span class="param-badge badge-matrix">matrix</span>
The values $S_\text{upper}(h)$ entered are dimensionless decimal numbers, between 0 and 1.
This is the upper limit for filling the stock, expressed as a filling rate,
imposed each hour.

!!! info
    Implicit rule for all hours : modulation of min capacity $\leq$ modulation of max capacity

### Inflows

#### Time series (MW)

<span class="param-badge badge-matrix">matrix</span>
Natural inflows $I(h)$ in MW that enters into the storage. The values for this file
can be negative, corresponding to withdrawals imposed on the stock for other
uses (for example agricultural withdrawals or imposed discharging of EV
batteries).

### Flow Costs (€/MW)

#### Stored cost

<span class="param-badge badge-matrix">matrix</span>
Penalizes the injection flowrate at each hour ($c_\text{stored}(h)$). This penalty must be positive.
This penalty will add an injection cost in the model.

#### Released cost

<span class="param-badge badge-matrix">matrix</span>
Penalizes the withdrawal flowrate at each hour ($c_\text{released}(h)$). This penalty must be positive.
This penalty will add a withdrawal cost in the model.

### Flow-Variation costs (€/MW/h)

#### Stored variation cost 

<span class="param-badge badge-matrix">matrix</span>
Penalizes the injection flowrate variation every hour ($c_\text{var, stored}(h)$). 
This penalty must be positive. 
This penalty is only enabled if the boolean parameter 
[penalty on injection variation](#penalty-on-injection-variation) is enabled.
This penalty will penalize proportionally any injection flowrate variation between 2 hours.

#### Released variation cost

<span class="param-badge badge-matrix">matrix</span>
Penalizes the withdrawal flowrate variation every hour ($c_\text{var, released}(h)$). 
This penalty must be positive.
This penalty is only enabled if the boolean parameter 
[penalty on withdrawal variation](#penalty-on-withdrawal-variation).
This penalty will penalize proportionally any withdrawal flowrate variation between 2 hours.

### Level cost (€/MWh)

<span class="param-badge badge-matrix">matrix</span>
Penalizes the volume of stored energy at each hour ($c_S (h)$).
A negative penalty is allowed for this cost. 
If the penalty is positive, it will favor lower-level trajectories. 
If the penalty is negative, it will favor higher-level trajectories.

## Additional constraints

When solving the problem of short-term storages, Antares determines the evolution of 3 types of variables:

- Level $S(h)$ (in MWh) of the storage 
- Charge $P_\text{stored}(h)$ (in MW): incoming power flow
- Discharge $P_\text{released}(h)$ (in MW): outgoing power flow

You can define additional constraints on these variables to restrict the solutions of the problem.
However, you cannot combine variables of different types within the same constaint. 

These additional constraints are linked to a powerful feature that allows you to select any set of time steps
to which the constraint applies (see the [constraint equation](#additional-constraint-model)). 
For example, this feature enables the modeling of a daily constraint over a specific time window, 
such as requiring that power be injected into storage only between 10am and 2pm.

#### Name

<span class="param-badge badge-string">string</span>
Name of the additional constraint.

#### Variable

<span class="param-badge badge-enum">enum</span>
The differents types of variable on which you can apply the additional constraint:

- Level variation $S(h) - S(h-1) - I(h)$. 
- Charge $P_\text{stored}(h)$.
- Discharge $P_\text{released}(h)$.

#### Bounds

<span class="param-badge badge-enum">enum</span>
The different possibilities of bounds for the constraint:

- $=$
- $<$
- $>$

#### Enabled

<span class="param-badge badge-bool">bool</span>
Whether to enable this additional constraint for the simulation.

#### Occurences

<span class="param-badge badge-matrix">matrix</span>
Boolean matrix of the hours where there the constraint applies 
(see more in the [additional constraint equation](#additional-constraint-model)).

#### Time series

<span class="param-badge badge-matrix">matrix</span>
Right-hand side $\text{RHS}$ of the constraint.

## Equations

### General model

The goal of Antares is to find the variables:

- $P_{\text{stored}}(h)$ the power injection inside the storage at each hour.
- $P_{\text{released}}(h)$ the power withdrawal from the storage at each hour.
- $S(h)$ the stock level at each hour.

These variables are bounded by:

$$
0 \leq P_{\text{stored}}(h) \leq P_\text{stored}^\text{max} \, \text{mod}_\text{stored}(h)
$$

$$
0 \leq P_{\text{released}}(h) \leq P_\text{released}^\text{max} \, \text{mod}_\text{released}(h)
$$

$$
S_\text{max} \, \text{mod}_\text{lower}(h) \leq S(h) \leq S_\text{max} \, \text{mod}_\text{upper}(h)
$$
Remarque JMJ : Smin n'existe pas !
Finally, these variables are related in the dynamical equation:

$$
S(h) = S(h-1) + (P_\text{stored}(h) \, e_\text{stored} - P_\text{released}(h) \, e_\text{released} + I(h)) \times \text{1h}
$$

!!! info
    The implicit convention is that the stock level at the end of the week 
    is equal to the initial level if the parameter 
    [initial level optimized](#initial-level-optimized) is disabled.

    $$
    S(\text{168 h}) = S(\text{0 h}) = p_0 \, S_\text{max}
    $$

### Penalty model

Penalties can be added to the objective function.

- On level: $S(h) \, c_{S}(h)$
- On injection flowrate: $P_\text{stored} \, c_\text{stored}(h)$
- On withdrawal flowrate: $P_\text{released} \, c_\text{released}(h)$

When there is penalization on the stored/released variation there are two new variables introduced:

- $P_\text{var, stored}(h)$
- $P_\text{var, released}(h)$

$$
P_\text{var, stored}(h) \geq P_\text{stored}(h) - P_\text{stored}(h-1)
$$

$$
P_\text{var, stored}(h) \geq P_\text{stored}(h-1) - P_\text{stored}(h)
$$

$$
P_\text{var, released}(h) \geq  P_\text{released}(h) - P_\text{released}(h-1)
$$

$$
P_\text{var, released}(h) \geq P_\text{released}(h-1) - P_\text{released}(h)
$$

Then the penalty is:

- $P_\text{var, stored}(h) \, c_\text{var, stored}(h)$
- $P_\text{var, released}(h) \, c_\text{var, released}(h)$

### Additional constraint model

For a given constraint, with hours $(h_{i,j})$ such as:

$$
\underbrace{[h_{1,1}, h_{1,1}, \dots, h_{1,n_1}]}_{\text{Occurence 1}}, \,
\underbrace{[h_{2,1}, h_{2,2}, \dots, h_{2,n_2}]}_{\text{Occurence 2}}, \dots,
\underbrace{[h_{k,1}, h_{k,2}, \dots, h_{k,n_k}]}_{\text{Occurence k}} 
$$

Let $s \in [1,52]$ a week of an Antares sub-problem to solve, and $H_s$
the hour in the annual reference frame that preceded the first hour of week $s$,
such as $H_s = 168 \times (s - 1)$ for the week $s.$ 

The constraint $i$ corresponding to the $i$-th block or occurrence of the hours $(h_{i,j})$ is

$$
\sum_{j=1}^{n_i} \text{variable}(h_{i,j}) \text{ bounded by } \sum_{j=1}^{n_i} \text{RHS}(H_s + h_{i,j})
$$

where $\text{variable}$ corresponds to the variable charge, discharge or level,
and $\text{bounded by}$ corresponds to one of the following operators $\{\leq, =, \geq\}$.
