# Optimization problem

## Introduction

Let's dive into a detailed and comprehensive formulation of the main optimization problems 
solved by Antares inner optimization engine. It is intended as a formal demonstration of 
the inner working of the software for curious users interested in the optimization process and R&D.
The goal here is to explain the resolution of the **hydro-thermal unit-commitment problem**. 
Each optimization problem is solved once when the milp option and twice otherwise.

!!! note
    Antares Simulator offers an option that makes it possible for the user to print, 
    in a standardized format, any or all of the optimization problems actually solved 
    in the course of an Antares Simulation session in 
    [MPS format](https://www.ibm.com/docs/en/icos/22.1.2?topic=cplex-mps-file-format-industry-standard).

The simulation of the system behavior throughout many years, with a **time step of 1 hour** 
is decomposed into a series of smaller problems. 
The elementary optimization problem resulting from this approach is the minimization 
of the overall system operation cost over a week of a given year, 
taking into account all proportional and non-proportional generation costs, 
transmission charges, unsupplied energy (generation shortage) costs and conversely, 
spilled energy (generation excess) costs.

Carrying out generation adequacy studies or transmission projects studies means formulating 
and solving a series of a great many week-long operation problems, 
one for each week of each Monte-Carlo year, assumed to be independent. 
This generic optimization problem will be further denoted $\mathcal{P}^k$, 
where $k$ is an index encompassing all weeks of all Monte-Carlo years.

Note that this independence assumption may sometimes be too lax, 
because in many contexts weekly problems are actually coupled to some degree. 
The only constraint coupling weekly problems is related to the management 
of reservoir-type hydro resources. When appropriate, these effects are therefore dealt with 
before the actual decomposition in weekly problems takes place,
this being done4 either of the following way (depending on simulation options):

1. Use of an economic signal (typically, a shadow "water value") yielded by 
   an external preliminary stochastic dynamic programming optimization 
   of the use of energy-constrained resources.
2. Use of heuristics that provide an assessment of the relevant energy credits 
   that should be used for each period, fitted so as to accommodate with sufficient versatility 
   different operational rules.

Quite different is the situation that prevails in expansion studies, 
in which weekly problems cannot at all be separated from a formal standpoint,
because new assets should be paid for all year-long,
regardless of the fact that they are used or not during such or such week:
the generic expansion problem encompasses therefore all the weeks 
of all the Monte-Carlo years at the same time. It will be further denoted $\mathcal{P}$.


## Notations

### General notations

| Notation              | Explanation                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|
| $k \in  K$            | optimization periods (weeks) over which $P$ and $P^k$ are defined (omitted for simplicity)                          |
| $t \in T$             | individual time steps of any optimization period $k\in K$ (hours of the week)                                      |
| $G(N,L)$              | undirected graph of the power system (connected)                                                                    |
| $n \in N$             | vertices of $G$, $N$ is an ordered set                                                                              |
| $l \in L$             | edges of $G$                                                                                                        |
| $A$                   | incidence matrix of $G$, dimension $N\times L$                                                                      |
| $g$                   | spanning tree of $G$                                                                                                |
| $C_g$                 | cycle basis associated with $g$, dimension $L\times (L+1-N)$                                                        |
| $L_n^+\subset L$      | set of edges for which $n$ is the upstream vertex                                                                   |
| $L_n^-\subset L$      | set of edges for which $n$ is the downstream vertex                                                                 |
| $u_l \in N$           | vertex upstream from $l$                                                                                            |
| $d_l \in N$           | vertex downstream from $l$                                                                                          |
| $u \cdot v$           | inner product of vectors $u$ and $v$                                                                                |
| $u_\uparrow^p$        | vector resulting from the permutation on $u \in \mathbb{R}^s$: $u_\uparrow^p(i)=u(i+p\, \mathrm{mod}\,s)$        |

Problems $P^k$ and $P$ call for the definition of many parameters and variables further described.

The power system is supposed to be operated so as to be able to face some amount 
of unexpected demand increase with redispatching actions only (no change in the unit commitment). 
Two operating states are therefore modelled:

- **nominal**: Actual conditions match exactly all standard forecast. 
  Demand is supplied by optimal generation dispatch (variable notation: _Var_).

- **uplifted**: Additional demand increases are applied to the nominal state 
  and call for redispatch (activation of security reserves; variable notation: $Var^s$).

!!! note
    Almost all variables of the system are defined twice (one value per state).
    For clarity's sake, only the definition of the nominal variables (_Var_) are given hereafter,
    the definition of variables _$Var^s$_ are implicit.

### Grid

#### Parameters

| Notation                                       | Explanation                                                                                             |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| $C_l^+ \in \mathbb{R}^T_+$                     | initial transmission capacity from $u_l$ to $d_l$ (variable of $P$ and $P^k$)                           |
| $\overline{C}_l^+ \in \mathbb{R}^T_+$      | maximum transmission capacity from $u_l$ to $d_l$ (variable of $P$, not used in $P^k$)                  |
| $C_l^- \in \mathbb{R}^T_+$                     | initial transmission capacity from $d_l$ to $u_l$ (variable of $P$ and $P^k$)                           |
| $\overline{C}^{-}_l\in \mathbb{R}^T_{+}$   | maximum transmission capacity from $d_l$ to $u_l$ (variable of $P$, not used in $P^k$)                  |
| $\Psi_l \in \mathbb{R}_+$                      | weekly cost of a maximum capacity investment                                                            |
| $\gamma_l^+\in \mathbb{R}^T$                   | transmission cost through $l$, from $u_l$ to $d_l$. Proportional to the power flow                      |
| $\gamma_l^-\in \mathbb{R}^T$                   | transmission cost through $l$, from $d_l$ to $u_l$. Proportional to the power flow                      |
| $Z_l \in \mathbb{R}_+$                        | overall impedance of $l$                                                                                |

#### Variables

| Notation                                       | Explanation                                                                                             |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| $x_l \in [0,1]$                                | transmission capacity investment level                                                                  |
| $F_l^+ \in \mathbb{R}^T_+$                     | power flow through $l$, from $u_l$ to $d_l$                                                             |
| $F_l^- \in \mathbb{R}^T_+$                     | power flow through $l$, from $d_l$ to $u_l$                                                             |
| $F_l\in \mathbb{R}^T$                          | total power flow through $l$, $F_l=F_l^+-F_l^-$                                                         |
| $\tilde{F}_t \in \mathbb{R}^T$                 | system flow snapshot at time $t$                                                                        |

### Thermal units

#### Parameters

| Notation                                                       | Explanation                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| $\theta \in \Theta_n$                                          | Thermal clusters (sets of identical units) installed in node $n$                        |
| $\overline{P}_\theta \in \mathbb{R}^T_+$                      | Maximum power output from cluster $\theta$, depends on cluster availability. Given directly by the `Availability` time series: the one provided by the user if set, otherwise the one generated by Antares from the `TS generator` parameters |
| $\underline{P}_\theta \in \mathbb{R}^T_+$                     | Minimum power output from cluster $\theta$. Computed as `Min gen modulation` $\times$ `Unit` $\times$ `Nominal capacity`                 |
| $\chi_\theta \in \mathbb{R}^T$                                 | Market bid cost of cluster $\theta$. Equal to `Market bid cost`                                             |
| $\sigma_\theta^+ \in \mathbb{R}^T$                             | Startup cost for each unit. Equal to `Startup cost`                                       |
| $\tau_\theta \in \mathbb{R}^T$                                 | Cost for each running unit, independently of the power output. Equal to `Fixed O&M cost`      |
| $l_\theta \in \mathbb{R}_+$                                    | Minimum stable power output for each running unit. Equal to `Min stable power`                             |
| $u_\theta \in \mathbb{R}_+$                                    | Maximum net power output for each running unit. Equal to `Nominal capacity`                                |
| $\zeta_\theta \in [0,100]$                                     | Default contribution to the spinning reserve (%). Equal to `Spinning`                            |
| $\Delta_\theta^+ \in \lbrace 1,\dots, \|T\|\rbrace$            | Minimum on time when running for each unit. Equal to `Min uptime`                                         |
| $\Delta_\theta^- \in \lbrace 1,\dots, \|T\|\rbrace$            | Minimum off time when not running for each unit. Equal to `Min downtime`                                    |
| $\overline{M}_\theta \in \mathbb{N}^T$                         | Maximum number of running units in cluster $\theta$. Computed as $\lceil \overline{P}_\theta / u_\theta \rceil$                                     |
| $\underline{M}_\theta \in \mathbb{N}^T$                        | Minimum number of running units in cluster $\theta$. Computed as $\lceil \underline{P}_\theta / (u_\theta \times (1 - \zeta_\theta/100)) \rceil$                                     |

#### Variables

| Notation                                                       | Explanation                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| $P_\theta \in \mathbb{R}^T_+$                                  | Power output from cluster $\theta$. Continuous variable, used in "fast", "accurate" and "milp" modes      |
| $M_\theta \in \mathbb{N}^T$                                    | Number of running units in cluster $\theta$. Used only in "accurate" and "milp" modes (integer in "milp" mode, relaxed to continuous in "accurate" mode); derived heuristically in "fast" mode      |
| $M_\theta^+ \in \mathbb{N}^T$                                  | Number of units in cluster changing from state off to state on in cluster $\theta$. Used only in "accurate" and "milp" modes (integer in "milp" mode, relaxed to continuous in "accurate" mode)      |
| $M_\theta^- \in \mathbb{N}^T$                                  | Number of units in cluster changing from state on to state off in cluster $\theta$. Used only in "accurate" and "milp" modes (integer in "milp" mode, relaxed to continuous in "accurate" mode)      |
| $M_\theta^{--} \in \mathbb{N}^T$                               | Number of units in cluster changing from state on to state off due to outages. Used only in "accurate" and "milp" modes (integer in "milp" mode, relaxed to continuous in "accurate" mode)      |

### Reservoir-type hydropower units (or other power storage facilities)

#### Parameters

| Notation                                          | Explanation                                                                                                                                                                        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                
| $\lambda \in \Lambda_n$                           | reservoirs connected to node $n$                                                                                                                                                   |
| $S_\lambda \in \mathbb{R}_+$                      | size of reservoir $\lambda$: amount of energy that can be stored in $\lambda$                                                                                                     |
| $Q\in \mathbb{N}$                                 | number of discrete levels defined in reservoir                                                                                                                                     |
| $\overline{W}_\lambda \in \mathbb{R}_+$          | maximum energy output from $\lambda$ throughout the optimization period                                                                                                            |
| $\underline{W}_\lambda \in \mathbb{R}_+$         | minimum energy output from $\lambda$ throughout the optimization period                                                                                                            |
| $\overline{H}_\lambda \in \mathbb{R}_+^T$        | maximum power output from reservoir $\lambda$. Note: $\sum_{t\in T} \overline{H}_{\lambda_t} \geq \underline{W}_\lambda$                                                       |
| $\underline{H}_\lambda \in \mathbb{R}_+^T$       | minimum power output from reservoir $\lambda$. Note: $\sum_{t\in T} \underline{H}_{\lambda_t} \leq \overline{W}_\lambda$                                                       |
| $r_\lambda \in \mathbb{R}_+$                     | maximum ratio between output power daily peak and daily average ($1 \leq r_\lambda \leq 24$)                                                                                      |
| $\varepsilon_\lambda \in \mathbb{R}$             | reference water value associated with the reservoir's initial state (date, level)                                                                                                  | $\eta_\lambda \in \mathbb{R}^Q$             | reference water value associated with the reservoir's final state (date) <br> if _hydro pricing option:= fast_ then: $\eta_\lambda \leftarrow 0$                                                  <br> if _hydro pricing option:= accurate_ then: $v_\lambda \leftarrow 0$ |
| $\epsilon_\lambda^1 \in \mathbb{R}$              | penalty fee on hydro generation variations (dispatch smoothing effect) <br> if _hydro power fluctuations option:= free modulations_ then $\epsilon_\lambda^1 \leftarrow O$       |
| $\epsilon_\lambda^2 \in \mathbb{R}$              | penalty fee on hydro generation maximum varition (dispatch smoothing effect) <br> if _hydro power fluctuations option:= free modulations_ then $\epsilon_\lambda^2 \leftarrow O$ |
| $\omega_\lambda \in \mathbb{R}$                  | overflow value (value of energy impossible to store in reservoir $\lambda$)                                                                                                         |           |
| $\varepsilon^*_\lambda \in \mathbb{R}$           | random component added to the water value (dispatch smoothing effect)                                                                                                              |
| $\eta_\lambda \in \mathbb{R}^Q$                  | reference water value associated with the reservoir's final state (date)                                                                                                           |
| $\rho_\lambda \in \mathbb{R}_+$                  | efficiency ratio of pumping units (or equivalent devices) available in reservoir $\lambda$                                                                                         |
| $\overline{\Pi}_\lambda \in \mathbb{R}_+^T$      | maximum power absorbed by pumps of reservoir $\lambda$                                                                                                                             |
| $I_\lambda \in \mathbb{R}^T_+$                   | natural power inflow to reservoir $\lambda$                                                                                                                                        |
| $\overline{R}_\lambda \in \mathbb{R}_+^T$        | upper bound of the admissible level in reservoir $\lambda$                                                                                                                         |
| $\underline{R}_\lambda \in \mathbb{R}_+^T$       | lower bound of the admissible level in reservoir $\lambda$                                                                                                                         |

#### Variables

| Notation                                          | Explanation                                                                                                                                                                        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $H_\lambda \in \mathbb{R}_+^T$                   | power output from reservoir $\lambda$                                                                                                                                              |
| $\Pi_\lambda \in \mathbb{R}_+^T$                 | power absorbed by pumps of reservoir $\lambda$                                                                                                                                     |
| $O_\lambda \in \mathbb{R}_+^T$                   | power overflowing from reservoir $\lambda$: part of inflow that cannot be stored                                                                                                  |
| $R_\lambda \in \mathbb{R}^T_+$                   | stored energy level in reservoir $\lambda$                                                                                                                                         |
| $\mathfrak{R}_{\lambda_q} \in \mathbb{R}_+$      | filling level of reservoir layer $q$ at time $T$ (end of the week)                                                                                                                 |

### Short-term storages

#### Parameters

| Notation                                                                      | Explanation                                                                                                                              |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| $s\in \mathcal{S}$                                                            | A single short-term storge reservoir. There is one set of short-term storage per area.                                                   |
| $\underline{L}_s \in \mathbb{R}^T$, $\overline{L}_s \in \mathbb{R}^T$         | Minimum (resp. maximum) level for storage $s$ also known as "rule-curves"                                                                |
| $L_s^0 \in \mathbb{R}_+$                                                      | Initial level for storage $s$ (optional)                                                                                                 |
| $\underline{P}^i_s \in \mathbb{R}^T$, $\overline{P}^i_s \in \mathbb{R}^T$     | Minimum (resp. maximum) injection for storage $s$                                                                                        |
| $\eta^i_s \in [0, 1]$                                                         | Injection efficiency for storage $s$                                                                                                     |
| $\underline{P}^w_s \in \mathbb{R}^T$, $\overline{P}^w_s \in \mathbb{R}^T$     | Minimum (resp. maximum) withdrawal for storage $s$                                                                                       |
| $\eta^w_s \in [0, 1]$                                                         | Withdrawal efficiency for storage $s$                                                                                                    |
| $I_s \in \mathbb{R}^T$                                                        | Inflows for storage $s$. Energy that is injected into the storage over time                                                              |

#### Variables

| Notation                                                                      | Explanation                                                                                                                              |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| $L_s \in \mathbb{R}_+^T$                                                      | Level for storage $s$                                                                                                                    |
| $P^w_s \in \mathbb{R}_+^T$                                                    | Withdrawal for storage $s$. Note that this is from the storage's perspective: the amount of power withdrawn from the storage            |
| $P^i_s \in \mathbb{R}_+^T$                                                    | Injection for storage $s$. Note that this is from the storage's perspective: the amount of power injected into the storage              |


### Binding constraints

In problems $\mathcal{P}^k$, the need for a versatile modelling of the power system calls 
for the introduction of an arbitrary number of linear binding constraints 
between system's variables throughout the grid, expressed either in terms of hourly power,
daily energies or weekly energies.
These constraints may bind together synchronous flows as well as thermal units power outputs.
They may be related to synchronous values or bear on different times.
Herebelow, the generic notation size is used for the relevant dimension of the set to which parameters belong.

These dimensions stand as follow

$\mathrm{size}=T=168$: applicable to lower and upper bounds of constraints between hourly powers
$\mathrm{size}=\frac{T}{7}=24$: applicable to lower and upper bounds of constraints between daily energies
$\mathrm{size}=\frac{T}{168}=1$: applicable to lower and upper bounds of constraints between weekly energies

Generic notations for binding constraints:

#### Parameters

| Notation                                  | Explanation                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| $e \in E$                                 | set of all grid interconnections and thermal clusters. $E = L \cup \Theta$                                   |
| $b \in B$                                 | binding constraints                                                                                          |
| $B_h \subset B$                           | subset of $B$ containing the binding constraints between hourly powers                                       |
| $B_d \subset B$                           | subset of $B$ containing the binding constraints between daily energies                                      |
| $B_w \subset B$                           | subset of $B$ containing the binding constraints between weekly energies                                     |
| $\alpha_e^b \in \mathbb{R}$               | weight of $e$ (flow within $e$ or output from $e$) in the expression of constraint $b$                       |
| $o_e^b \in \mathbb{N}$                    | time offset of $e$ (flow within $e$ or output from $e$) in the expression of constraint $b$                  |
| $u^b \in \mathbb{R}^{\mathrm{size}}$      | upper bound of binding constraint $b$                                                                        |
| $l^b \in \mathbb{R}^{\mathrm{size}}$      | lower bound of binding constraint $b$                                                                        |

### Demand, security uplift, unsupplied and spilled energies

#### Parameters

| Notation                      | Explanation                                                                        |
|-------------------------------|------------------------------------------------------------------------------------|
| $D_n \in \mathbb{R}^T$        | net power demand expressed in node $n$, including must-run generation              |
| $S_n \in \mathbb{R}^T_+$      | demand security uplift to be faced in node $n$, by activation of security reserves |
| $\delta_n^+ \in \mathbb{R}^T$ | normative unsupplied energy value in node $n$. Value of lost load - VOLL           |
| $\delta_n^- \in \mathbb{R}^T$ | normative spilled energy value in node $n$ (value of wasted energy)                |

#### Variables

| Notation                      | Explanation                                                                        |
|-------------------------------|------------------------------------------------------------------------------------|
| $G_n^+ \in \mathbb{R}^T_+$    | unsupplied power in the nominal state                                              |
| $G_n^- \in \mathbb{R}^T_+$    | spilled power in the nominal state                                                 |

## Formulation of the problem 

Let's formulate the $\mathcal{P}^k$ problem. 
The superscript $k$ is implicit in all subsequent notations of this section 
(omitted for simplicity's sake).

## Objective
$$
\begin{equation}
    \min_{M_\theta \in \mathrm{Argmin} \Omega_{\mathrm{unit com}}}(\Omega_{\mathrm{dispatch}})
\end{equation}
$$


with


$$
\begin{equation}
    \Omega_{\mathrm{dispatch}} = \Omega_{\mathrm{transmission}}+\Omega_{\mathrm{hydro}}+\Omega_{\mathrm{thermal}}+\Omega_{\mathrm{unsupplied}}+\Omega_{\mathrm{spillage}}
\end{equation}
$$


$$
\begin{equation}
    \Omega_{\mathrm{transmission}}=\sum_{l \in L} \gamma_l^+ \cdot F_l^+ + \gamma_l^- \cdot F_l^-
\end{equation}
$$


$$
\begin{equation}
    \Omega_{\mathrm{hydro}} = \sum_{n \in N} \sum_{\lambda in \Lambda_n} (\varepsilon_\lambda + \varepsilon^*_\lambda)\cdot(H_\lambda - \rho_\lambda \Pi_\lambda + O_\lambda) - \sum_{n \in N} \sum_{\lambda \in \Lambda_n}\sum_{q=1}^Q \eta_{\lambda_q} \mathfrak{R}_{\lambda_q}
\end{equation}
$$


$$
\begin{equation}
    \Omega_{\mathrm{thermal}}=\sum_{n \in N} \sum_{\theta \in \Theta_n} \chi_\theta \cdot P_\theta + \sigma_\theta^+ \cdot M_\theta^+ + \tau_\theta \cdot M_\theta
\end{equation}
$$


$$
\begin{equation}
    \Omega_{\mathrm{unsupplied}}=\sum_{n \in N} \delta_n^+ \cdot G_n^+
\end{equation}
$$


$$
\begin{equation}
    \Omega_{\mathrm{spillage}}=\sum_{n \in N} \delta_n^- \cdot G_n^-
\end{equation}
$$

$\Omega_{\mathrm{unit com}}$ is the expression derived from $\Omega_{\mathrm{dispatch}}$ 
by replacing all variables that depend on the system's state by their equivalent in the uplifted state.

## Constraints related to the nominal system state

### Short-term storage

Level equation. For each short-term storage $s\in\mathcal{S}$,

$$
\begin{equation}
    L_s(t) - L_s(t-1) = \eta^i_s * P^i_s(t) - \eta^w_s * P^w_s(t) + I_s(t)
\end{equation}
$$

Note that in this equation, time-steps are cycled. 
From now on, time indices are omitted for simplicity.

Bounded level

$$
\begin{equation}
    0 \leq \underline{L}_s \leq L_s \leq \overline{L}_s
\end{equation}
$$

Bounded injection

$$
\begin{equation}
    \underline{P}^i_s \leq P^i_s \leq \overline{P^i}_s
\end{equation}
$$

Bounded withdrawal

$$
\begin{equation}
    \underline{P}^w_s \leq P^w_s \leq \overline{P^w}_s
\end{equation}
$$

Initial level (optional)

$$
\begin{equation}
    L_s(0) = L_s^0
\end{equation}
$$

### Balance between load and generation

First Kirchhoff's law:

$$
\begin{equation}
    \forall n \in N, \quad \sum_{l \in L_n^+} F_l - \sum_{l \in L_n^-} F_l = \left( G_n^+ + \sum_{\lambda \in \Lambda_n}(H_\lambda - \Pi_\lambda) + \sum_{\theta \ \in \Theta_n} P_\theta + \sum_{s \in \mathcal{S}} \left(P^w_s - P^i_s\right)\right)-(G_n^-+D_n)
\end{equation}
$$


On each node, the unsupplied power is bounded by the net positive demand:

$$
\begin{equation}
    \forall n \in N, \quad 0 \leq G_n^+ \leq \max(0, D_n)
\end{equation}
$$

On each node, the spilled power is bounded by the overall generation of the node
(must-run + dispatchable power):

$$
\begin{equation}
    \forall n \in N, \quad 0 \leq G_n^- \leq -\min(0, D_n) + \sum_{\lambda \in \Lambda_n}H_\lambda + \sum_{\theta \ \in \Theta_n} P_\theta
\end{equation}
$$

Flows on the grid:

$$
\begin{equation}
    \forall l \in L, \quad 0 \leq F_l^+ \leq C_l^+ +(\overline{C}^{+}_l - C_l^+)x_l
\end{equation}
$$

$$
\begin{equation}
    \forall l \in L, \quad  0 \leq F_l^- \leq C_l^- +(\overline{C}^{-}_l - C_l^-)x_l
\end{equation}
$$

$$
\begin{equation}
    \forall l \in L, \quad  F_l = F_l^+ - F_l^-
\end{equation}
$$

Flows are bounded by the sum of an initial capacity and of a complement brought by investment

### Binding constraints

$$
\begin{equation}
    \forall b \in B_h, \quad  l^b \leq \sum_{e \in E} \alpha_e^b (F_e)_{\uparrow}^{o_e^b} \leq u^b
\end{equation}
$$

$$
\begin{equation}
    \forall b \in B_d, \forall k \in \lbrace 0,\dots,6\rbrace, \quad  l^b \leq \sum_{e \in E} \alpha_e^b \sum_{t \in \lbrace 1,\dots,24\rbrace} (F_e)_{\uparrow {24k+t}}^{o_e^b} \leq u^b
\end{equation}
$$

$$
\begin{equation}
    \forall b \in B_w, \quad  l^b \leq \sum_{e \in E} \alpha_e^b \sum_{t \in T} F_{e_t} \leq u^b
\end{equation}
$$

### Hydropower units

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \quad  \underline{W}_{\lambda} \leq \sum_{t\in T} H_{\lambda_t} \leq \overline{W}_{\lambda}
\end{equation}
$$

FIXME: RHS
$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \quad  \sum_{t\in T} H_{\lambda_t} - \sum_{t\in T} \rho_t \Pi_{\lambda_t} = \overline{W}_{\lambda}
\end{equation}
$$

Instantaneous generating power is bounded

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \quad  \underline{H}_{\lambda} \leq H_{\lambda} \leq \overline{H}_{\lambda}
\end{equation}
$$

Intra-daily power modulations are bounded and power fluctuations may be subject to penalty fees [^1]

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \forall k \in \lbrace 1, \ldots, 6 \rbrace, \quad  \frac{\max_{t \in \lbrace 24k+1,\ldots, 24k+24 \rbrace} H_{\lambda_t}}{\sum_{t \in \lbrace 24k+1,\ldots, 24k+24 \rbrace} H_{\lambda_t}} \leq r_{\lambda}
\end{equation}
$$

Instantaneous pumping power is bounded

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \quad  0 \leq \Pi_{\lambda} \leq \overline{\Pi}_{\lambda}
\end{equation}
$$

Reservoir level evolution depends on generating power, pumping power, pumping efficiency, 
natural inflows and overflows

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \forall t \in T, \quad  R_{\lambda_t} - R_{\lambda_{t-1}} = \rho_\lambda \Pi_{\lambda_t} - H_{\lambda_t} + I_{\lambda_t} - O_{\lambda_t}
    \label{eq:reservoir-level-evolution}
\end{equation}
$$

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \quad  R_{\lambda T} = \sum_{q=1,Q} \mathfrak{R}_{\lambda_q}
    \label{eq:reservoir-final-level}
\end{equation}
$$

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, q=1,Q, \quad  \mathfrak{R}_{\lambda_q} \leq \frac{S_{\lambda}}{Q}
    \label{eq:reservoir-layer-bound}
\end{equation}
$$

Reservoir level is bounded by admissible lower and upper bounds (rule curves)

$$
\begin{equation}
    \forall n \in N, \forall \lambda \in \Lambda_n, \quad  \underline{R}_\lambda \leq R_\lambda \leq \overline{R}_\lambda
\end{equation}
$$

### Thermal units


Power output is bounded by must-run commitments and power availability

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \quad  \min(\max(\overline{P}_\theta \cdot (1-\zeta_\theta/100), l_\theta \cdot \overline{M}_\theta),\underline{P}_\theta) \leq P_\theta \leq \max(\overline{P}_\theta \cdot (1-\zeta_\theta/100), l_\theta \cdot \overline{M}_\theta)
    \label{eq:constraint-power-output}
\end{equation}
$$

The number of running units is bounded

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \quad   \min(\underline{M}_\theta,\overline{M}_\theta ) \leq M_\theta \leq \overline{M}_\theta 
    \label{eq:thermal_units}
\end{equation}
$$

Power output remains within limits set by minimum stable power and maximum capacity thresholds

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \quad  l_\theta M_\theta \leq P_\theta \leq u_\theta M_\theta
\end{equation}
$$


Minimum running and not-running durations contribute to the unit-commitment plan. 
Note that this modeling requires[^2] that one at least of the following conditions is met: 
$\Delta_\theta^- \leq \Delta_\theta^+$ or $\overline{M}_\theta \leq 1_T$

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \forall t \in T, \quad  M_{\theta_t} = M_{\theta_{t-1}} + M_{\theta_t}^+ - M_{\theta_t}^-
\end{equation}
$$

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \forall t \in T, \quad  {M_{\theta_t}^{--}} \leq {M_{\theta_t}^{-}}
\end{equation}
$$

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \forall t \in T, \quad  {M_{\theta_t}^{--}} \leq \max(0, \overline{M}_{\theta_{t-1}} - \overline{M}_{\theta_t})
\end{equation}
$$

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \forall t \in T, \quad  M_{\theta_t} \geq \sum_{k=t+1-\Delta_\theta^+}^{k=t}(M_{\theta_k}^+ - {M_{\theta_k}^{--}})
\end{equation}
$$

$$
\begin{equation}
    \forall n \in N, \forall \theta \in \Theta_n, \forall t \in T, \quad  M_{\theta_t} \leq \overline{M}_{\theta_{t - \Delta_\theta^-}} + \sum_{k=t+1-\Delta_\theta^-}^{k=t} \max(0, \overline{M}_{\theta_k} - \overline{M}_{\theta_{k-1}}) - \sum_{k=t+1-\Delta_\theta^-}^{k=t}(M_{\theta_k}^-)
    \label{eq:num-run-unit}
\end{equation}
$$

!!! info
    The constraints implemented depend on the option selected for unit commitment. 
    In "fast" mode, implementation is restricted to $\eqref{eq:constraint-power-output}$, 
    whereas "accurate" and "milp" mode involved modelling of constraints 
    $\eqref{eq:thermal_units}$ to $\eqref{eq:num-run-unit}$. 
    Note that for "fast" and "accurate" mode, all variables are continuous and a heuristic stage takes place between the "uplifted" and "nominal" optimization runs to deal with integrity issues. For "milp" mode, variables representing the number of units are integer.



[^1]: 
    Constraint $\eqref{eq:reservoir-level-evolution}$ is implemented only if the "heuristic" mode is used. 
    **Constraint $\eqref{eq:reservoir-final-level}$ is implemented only if the "power fluctuations" option is set to "minimize ramping".**
    Constraint $\eqref{eq:reservoir-layer-bound}$ is implemented only if the "power fluctuations" option is set to "minimize excursion".


[^2]: This does not actually limit the model's field of application: all datasets can easily be put in a format that meets this commitment.




