# Adequacy patch calculation

## Foreword

The operational algorithm of EUPHEMIA market coupling implements
"de-optimization" rules in order to fix the sharing of "Energy Not Served" (ENS)
between the market areas when there is any (in a way to ensure a certain fairness
in the sharing of this ENS): this is what we call the adequacy patch.

The requirement of fairness rules in the sharing of ENS within Antares studies
increased with the introduction of [flow-based modelling](flow-models.md).
Previously, this problem was mainly solved with the hurdle cost mechanism (small
costs on interconnections) limiting exports from areas where ENS was encountered.
However, implicit rules in Antares for sharing ENS, even outside the Flow-Based
domain, are not fully satisfactory, even with hurdle costs, because they prioritize
the treatment of ENS in countries directly connected to countries with margins,
to the detriment of more distant countries. In a context of decommissioning of
coal and nuclear plants in France and in Europe, cases of simultaneous ENS over
the domain will increase. Consequently, the need of adequacy patch to share fairly
this ENS is arising.

It should be noted that, in the current implementation of the patch within Antares,
the implementation covers only one of the three main features of the
'curtailment sharing and minimization' principles in EUPHEMIA, namely:

1. Local matching constraint.

2. Secondary problem of sharing of curtailment by the quadratic term.

3. The implemented solution does not yet consider the feature in EUPHEMIA, related
   to 'minimization of curtailment' in the primal problem which includes an extra
   penalty term directly in the global objective function in EUPHEMIA by
   multiplying the maximum curtailment ratio with a large $M$ pre-factor in the
   total welfare.

## Local matching rule

!!! note
    The implementation of the adequacy patch is available since v8.3.

The rule implemented is called the "Local Matching" rule:

- This rule consists in satisfying
  $\text{ENS} \leq \text{DENS}$ (Domestic Energy not Served)
  for all physical areas inside the adequacy patch.
- It specifies that an area cannot export more than its local margin.

This means that an area which can serve local demand with local generation,
should never have ENS.

!!! note

    - The local matching rule is only part of the economic mode of Antares
      (not the adequacy mode).
    - DENS outputs of Antares, for all selected areas, are available in the
      General values tab, as year-by-year and synthetic results. All the statistic
      values for it are calculated as well (min, max, mean, standard deviation).
      For the areas not part of the patch, the output DENS is set to 0.

### Specifications of the evolution concerning the optimization problem

To calculate the DENS used to constrain the ENS variations of each area,
a first iteration is performed. During this first iteration,
the usual optimization problem is slightly modified before being solved.
The objective of this first iteration is to get an ENS of each area
which will represent its DENS. In order to achieve this,
links between areas are forced to have a capacity of 0.
To ensure that customizable models will still work using this new feature,
different categories are created for the areas,
enabling different behaviours as needed. The different categories are:

- `virtual`: The area is a virtual area.
- `physical outside`: The area is a physical area not included in the adequacy
  patch domain.
- `physical inside`: The area is a physical area included in the adequacy patch
  domain.

In case Flow-Based is represented in the study,
the "hub" node introduced for the flow-based modelling should also be included
in the list of physical areas (this one should be declared by the user
in its list of physical nodes).

#### First iteration

In the first iteration, the following link capacities in the following direction
will be set to 0 MW:

- node "physical inside" <-> node "physical inside"
- node "physical inside" -> node "physical outside"
- node "physical outside" -> node "physical inside": optional/user defined
  (default `true`),
- node "physical outside" <-> node "physical outside": optional/user defined
  (default `true`).

Once the first iteration is completed, we have access to the DENS value,
which represents the ability of an area to fulfil its local load
thanks to its local production capacities:

- $\text{DENS} = \text{ENS}$ for each physical area inside the adequacy patch
  perimeter

#### Second iteration

During the second iteration, all link capacities between physical nodes are set
to the values provided as input data (as it is done in the current Antares
version). The only change compared to a simulation without the adequacy patch is
that the upper bound of the ENS on the areas included in the patch is now
constrained by the DENS found during the first iteration. This is introduced
in the optimization problem for physical areas that are declared in the adequacy
patch domain (areas declared as "physical inside"):

- $\text{ENS} \leq \text{DENS}$ (for all physical areas inside the adequacy patch).

## Curtailment sharing rule

!!! note
    This rule is available since v8.5.

The second implemented rule is called the "Curtailment Sharing" rule
(henceforth CSR).

The idea is that when countries on the network have positive DENS,
they should have relatively similar levels of unsupplied energy (as the name
suggests, so that the curtailment is shared). The quantity that is to be
measured and compared across countries is: $\text{ENS} / \text{PTO}$ where PTO
is the Price Taking Orders. There are different options of defining the PTOs.
In this development we will consider two:

- PTOs are the DENS of the country
- PTOs are the Load of the country

The considered countries are only nodes "2" (areas defined as physical areas
inside the adequacy patch), the problem to be solved is an hourly problem.
Precisely, the hourly problem to be solved concerns only hours for which
the sum of the ENS in all nodes "2" is exceeding a user-defined threshold.
If it is not the case, all the treatments described below should be ignored
for this hour and the algorithm should then consider the next hour. So, at that
step, we will solve the CSR quadratic optimization problem on a reduced domain,
limited to nodes "2" and the links that exist between these nodes 2.

!!! note
    Local matching and curtailment sharing rule are only part of the economic mode
    of Antares (Not the Adequacy mode).

!!! info "Convention"

    - A is any node of type "2" in the network, an area that is defined as a
      physical area inside the adequacy patch. Each variable/parameter/constraint
      applied on A is implicitly applied to any node of type "2".
    - B represents any node of type "2" linked to A.
    - A is alphabetically before B, therefore their link in Antares would be
      called A/B. Furthermore, regarding the flow on this link (variable that
      contains the algebraic value of the power flow between the 2 nodes to
      be optimized):
        - if the flow value is positive, the power flow goes from node A to node B,
          it is an export for node A and an import for node B.
        - if the flow value is negative, the power flow goes from node B to node A,
          it is an import for node A and an export for node B.

### Variable definitions

- **Flows over links variables** (3 set of variables: "Flow", "Flow_direct" and
  "Flow_indirect"): Inside the optimization problem, the "flow" variable is
  actually split in 2 positive variables for the resolution. It is required
  in order to write some constraints. We define the 2 positive variables,
  "Flow_direct" and "Flow_indirect" with this simple relation:
  $\text{Flow} = \text{Flow}_\text{direct} - \text{Flow}_\text{indirect}$

- **"net_position" variable:** "net_position (node A)" is the balance between node A
  and all other nodes "2" connected to node A.

- **"ENS" variable:** "ENS (node A)" contains the ENS to be optimized for that node.

- **"Spillage" variable:** "Spillage (node A)" contains the Spillage to be
  optimized for that node.

### Parameter definitions

- **"net_position_init" parameter:** The "net_position_init (node A)" parameter value
  is the value of the "net_position" calculated from the output of the
  Antares calculation for node A, considering results we get from the Antares
  calculation at the end of Local matching rule optimization.

- **"ENS_init" parameter:** The "ENS_init (node A)" parameter value is the value of
  the "ENS" obtained from the output of the Antares calculation for node A
  at the end of Local matching rule optimization.

- **"DENS_new" parameter:** The "DENS_new (node A)" parameter value is an update of
  the value of the "DENS" parameter which takes into account the result of
  Antares calculation (therefore different from the one estimated in Local
  matching rule optimization).

- **"Spillage_init" parameter:** The "Spillage_init (node A)" parameter value is
  the value of the "Spillage" obtained from the output of the Antares calculation
  for node A at the end of Local matching rule optimization.

- **"Hurdle cost" parameter on links:** This parameter, fixed on links, is kept
  from the Antares optimization problem. Like "flows" we can split "Hurdle cost"
  in "Hurdle_cost_direct" and "Hurdle_cost_indirect"

### Constraints and relations between variables

- **Constraints on "Flows", "Flow_direct" and "Flow_indirect" variables:**
  These variables should have exactly the same constraints as the ones considered
  in the Antares problem:
  - NTC constrains (independent lower and upper bounds for each link).
  - Flowbased binding constraints to be extracted from the hourly binding
    constraint list.

- **Relation between "Flows" over links and "net_position" on nodes:**
  The value of "net_position (node A)" is deduced from "flow" variable as
  follows:

  $$\text{net}_\text{position} (node A) = \sum \text{algebraic "Flows" over links involving node A}$$ 

  Remember that:
    - a "Flow" that goes from another node "2" to node A is an import for node A
      and should be counted positively
    - a "Flow" that goes from node A to another node "2" is an export for node A
      and should be counted negatively.

- **The detailed formulation for calculating the value of "net_position (node
  A)"** is, for all "nodes 2 upstream" and all "nodes 2 downstream":
  $$\begin{aligned}
  \text{net\_position (node A)} = \sum &\text{flow\_direct (node 2 upstream } \to \text{ node A)} \\
  + \sum &\text{flow\_indirect (node A } \leftarrow \text{ node 2 downstream)} \\
  - \sum &\text{flow\_indirect (node 2 upstream } \leftarrow \text{ node A)} \\
  - \sum &\text{flow\_direct (node A } \to \text{ node 2 downstream)}
  \end{aligned}$$

  Considering that:
    - "Node 2 upstream" is any node "2" which name in alphabetic order is before
      node A
    - "Node 2 downstream" is any node "2" which name in alphabetic order is after
      node A

- **Formula for calculating DENS_new parameter:**

  $$\text{DENS\_new (node A)} = \max \left[ 0; \text{ENS\_init (node A)} + \text{net\_position\_init (node A)} - \text{DTG.MRG (node A)}\right]$$

  Depending on the parameter in the GUI that includes or not possible imports
  from nodes "1" to nodes "2" in the DENS calculation, we should modify this
  formula. Precisely, it is when "NTC from physical areas outside to physical
  areas inside adequacy patch" is set to null then the formulation should be
  modified as follows:

  $$\text{DENS\_new (node A)} = \max \left[ 0; \text{ENS\_init (node A)} + \text{net\_position\_init (node A)} + \sum \text{flows (node 1 } \to \text{ node A)} - \text{DTG.MRG (node A)}\right]$$

  The detailed formulation for calculating the last term is,
  for all "nodes 1 upstream" and all "nodes 1 downstream":
  $$\begin{aligned}
  \sum \text{flows (node 1 } \to \text{ node A)} = \sum &\text{flow\_direct (node 1 upstream } \to \text{ node A)} \\
  + \sum &\text{flow\_indirect (node A } \leftarrow \text{ node 1 downstream)}
  \end{aligned}$$

  Considering that:
    - "Node 1 upstream" is any node "1" which name in alphabetic order is before
      node A
    - "Node 1 downstream" is any node "1" which name in alphabetic order is after
      node A

  The consideration of a correct DENS_new as presented above should ensure that
  the Local Matching Approach is respected: (node A) can't be "Exporting" and
  having ENS after CSR.

- **Relation induced by node balancing conservation:**
  $$\begin{aligned}
  &\text{ENS (node A)} + \text{net\_position (node A)} - \text{spillage (node A)} \\
  &= \text{ENS\_init (node A)} + \text{net\_position\_init (node A)} \\
  &\- \text{spillage\_init (node A)}
  \end{aligned}$$

  Actually, this simplified formulation takes into account that these variables are
  the only ones we are allowed to update by this optimization (power generation for
  all nodes and power flows between other nodes than nodes "2" will not be
  modified).

- **Constraint induced by Local matching rule:**

  $$\text{ENS (node A)} \leq \text{DENS}_{\text{new}}(\text{node A})$$

- **Positivity constraints:**

  $$\text{ENS (node A)} \geq 0$$
  $$\text{spillage (node A)} \geq 0$$

### Notes

- "Spillage" variable and "Spillage_init" parameter have been introduced only to
  deal with some situations for which "Flowbased" constraints, combining with
  adequacy patch rules, lead to an increase of Total ENS over the different nodes
  "2". Such increase of Total ENS could happen for 2 reasons:
  - We have new violations of Local Matching rule and the optimal solution found
    by Antares is no longer a valid solution, regards to this rule;
  - The curtailment sharing rule target is to minimize
    $\sum(\text{ENS}^2/\text{PTO})$ and such objective is not exactly
    equivalent than minimizing Total ENS.

  As a matter of fact, if we sum over all nodes "2" the relation induced by node
  balancing conservation, as the sum of all "net_position" is null, it leads to:

  $$\text{Total ENS} - \text{Total Spillage} = \text{Total ENS\_init} - \text{Total Spillage\_init, over all nodes \"2\"}$$

  So, an increase of Total ENS will necessarily lead to the same increase of
  Total Spillage.

- Spillage results after curtailment sharing rule quadratic optimization are
  presented in the separate column inside Antares output, titled "SPIL. ENRG.
  CSR" so the user has access to the spillage results both prior to and after
  CSR optimization.
- In order to avoid solver issues, lower and upper boundaries of the ENS and
  Spillage variables can be relaxed using GUI option "Relax CSR variable
  boundaries". Following relaxations can be imposed:

  $$-10^{-m} \leq \text{ENS(node A)} \leq \text{DENS}_{\text{new}}(\text{node A}) + 10^{-m}$$
  $$-10^{-m} \leq \text{spillage(node A)} \leq + \infty$$

  Where $m$ is an integer defined by the user.

### Objective function

Minimize:
$$\begin{aligned}
\left[ \sum &\frac{\text{ENS}^2}{\text{PTO}} 
+ \sum \frac{1}{M} \left( \text{hurdle cost direct} \times \text{flow direct} \right) \\
&+ \sum \frac{1}{M} \left( \text{hurdle cost indirect} \times \text{flow indirect} \right) 
\right]
\end{aligned}$$

The 2 latest terms are introduced to minimize loop flows in the considering
domain, and $M$ is the highest curtailment cost between a link's origin and
destination nodes, used to adapt the scale of hurdle costs to this new objective
(in practice, those tend to be the same for all nodes, typically 3000\u20ac/MW or
10000\u20ac/MW).

In order to assess the quality of the CSR solution additional verification can be
imposed by activating GUI option "Check CSR cost function value prior and after
CSR optimization". Values of the objective function prior to and after quadratic
optimization will be calculated and compared. If the objective function value
after the quadratic optimization has decreased, the new CSR solution will be
accepted and presented in the Antares output. However, if after quadratic
optimization the objective function value has increased (or stayed the same),
LMR solution will be adopted as final one and warning will be logged out with
the appropriate information (year, hour cost prior to quad optimization, cost
after quadratic optimization).

Initial objective function value:
$$\begin{aligned}
\text{QUAD}_0 = \left[ 
\sum &\frac{\text{ENS}_{\text{init}}^2}{\text{PTO}} \\
+ \sum &\frac{1}{M} \left( \text{hurdle cost}_{\text{direct}} \times \text{flow}_{\text{direct, init}} \right) \\
+ \sum &\frac{1}{M} \left( \text{hurdle cost}_{\text{indirect}} \times \text{flow}_{\text{indirect, init}} \right) 
\right]
\end{aligned}$$

Final objective function value:
$$\begin{aligned}
\text{QUAD}_1 = \left[ 
\sum &\frac{\text{ENS}_{\text{final}}^2}{\text{PTO}} \\
+ \sum &\frac{1}{M} \left( \text{hurdle cost}_{\text{direct}} \times \text{flow}_{\text{direct, final}} \right) \\
+ \sum &\frac{1}{M} \left( \text{hurdle cost}_{\text{indirect}} \times \text{flow}_{\text{indirect, final}} \right) 
\right]
\end{aligned}$$

If:

- $\text{QUAD}_0 \leq \text{QUAD}_1$ (CSR does not improve QUAD) then the
  "_init" solution is kept and the CSR solution is hence disregarded.
- $\text{QUAD}_0 > \text{QUAD}_1$ (CSR does improve QUAD) then the "CSR" solution
  is kept as final result updating the "_init" solution as stated above.

### Post-optimization process

For the CSR triggered hours, if after quadratic optimization,
area inside adequacy patch still experiences unsupplied energy:

- $\text{ENS (node A)} > 0$

following adjustments will be performed. Available dispatchable margin "DTG
MRG" will be used to compensate for the residual unsupplied energy ENS:

- $\text{ENS (node A)} = \max[0.0, \text{ENS (node A)} - \text{DTG.MRG (node A)}]$

Remaining dispatchable margin after above-described post-optimisation
calculation is stored inside new column "DTG MRG CSR":

- $\text{DTG.MRG.CSR (node A)} = \max[0.0, \text{DTG.MRG (node A)} - \text{ENS (node A)}]$

Note that for all the hours for which curtailment sharing rule was not triggered,
as well as for the hours for which curtailment sharing rule was triggered but
after quadratic optimization ENS (node A) is equal to zero,
$\text{DTG.MRG.CSR (node A)}$ will be equal to $\text{DTG.MRG (node A)}$.

For the curtailment sharing rule triggered hours, if after quadratic
optimization and above-described post calculation process,
area inside adequacy patch still experiences unsupplied energy,
marginal price "MRG.PRICE" will be aligned with the price cap in the model
(set to Unsupplied Energy Cost in the results).

- $\text{MRG.PRICE (node A)} = \text{Unsupplied Energy Cost (node A)}$

!!! note

    - SPIL. ENRG. CSR and DTG MRG CSR outputs of Antares, for all selected
      areas, are available in the General values tab, as year-by-year and
      synthetic results. All the statistic values for it are calculated as
      well (min, max, mean, standard deviation). For the areas not part of the
      patch, the default output is set to 0.
    - LMR VIOL. outputs of Antares, for all selected areas, are available in
      the General values tab, as year-by-year and synthetic results.
      For the areas not part of the patch, the default output is set to 0.
      LMR violation check is performed for all hours (CSR triggered or not)
      after LMR linear optimization (prior to CSR quadratic optimization).
      Hourly value of LMR violation is set to value one if all following
      conditions are met:

      - $\text{ENS\_init (node A)} > 0$.
      - $\text{net\_position\_init (node A)} + \sum \text{flows (node 1 } \to \text{ node A)} < 0$.

      $$\text{Abs}\left[\text{net\_position\_init (node A)} + \sum \text{flows (node 1 } \to \text{ node A)}\right] > \text{ENS\_init (node A)} + \text{GUI\_defined\_threshold}$$

        Second equation is satisfied if the area is exporting power.
        Depending on the GUI option member
        $(\sum \text{flows (node 1 } \to \text{ node A)})$ is optional.
