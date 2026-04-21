## Antares as a SCOPF ("flow-based model")

When problems $\mathcal{P}^k$ do not include any instance of so-called "binding constraints" and if no market pools are defined, the flows within the grid are only committed to meet the bounds set on the initial transmission capacities, potentially reinforced by investments (problem ).In other words, there are no electrical laws enforcing any particular pattern on the flows, even though hurdles costs and may influence flow directions through an economic signal.

In the general case, such a raw backbone model is a very simplified representation of a real power system whose topology and consistency are much more complex. While the full detailed modeling of the system within Antares is most often out of the question, it may happen that additional data and/or observations can be incorporated in the problems solved by the software.

In a particularly favorable case, various upstream studies, taking account the detailed system characteristics in different operation conditions (generating units outages and/or grid components outages N, N-1 , N-k,…) may prove able to provide a translation of all relevant system limits as a set of additional linear constraints on the power flowing on the graph $G(N,L)$ handled by Antares.

These can therefore be readily translated as "hourly binding constraints", without any loss of information. This kind of model will be further referred to as a "flow-based model"[^FB]. Its potential downside is the fact that data may prove to be volatile in short-term studies and difficult to assess in long-term studies.

## Antares as a SCOPF ("KL model")

When a full flow-based model cannot be set up (lack of robust data for the relevant horizon), it remains possible that classical power system studies carried on the detailed system yield sufficient information to enrich the raw backbone model. An occurrence of particular interest is when these studies show that the physics of the active power flow within the real system can be valuably approached by considering that the edges $l$ of $G(N,L)$ behave as simple impedances $Z_l$.This model can be further improved if a residual (passive) loop flow is to be expected on the real system when all nodes have a zero net import and export balance (situation typically encountered when individual nodes actually represent large regions of the real system). This passive loop flow should therefore be added to the classical flow dictated by Kirchhoff's rules on the basis of impedances $Z_l$. This model will be further referred to as a "KL model"[^KL]. Different categories of binding constraints, presented hereafter, make it possible to implement this feature in $\mathcal{P}^k$ and $\mathcal{P}$.

### Implementation of Kirchhoff's second law

The implementation ofKirchhoff's second law for the reference state calls for the following additional hourly binding $L+1-N$ constraints:

$$
\forall t \in T, C\_{g}^t Diag(Z\_{l}) \tilde{F}\_{t} = 0
$$

### Implementation of a passive loop flow

In cases where a residual passive loop flow $\tilde{\phi}\_{t}$ should be incorporated in the model to complete the enforcement of regular Kirchhoff's rules, the binding constraints mentioned in 7.1 should be replaced by:

$$
\forall t \in T, C\_{g}^t Diag(Z\_{l}) \tilde{F}\_{t} = C\_{g}^t Diag(Z\_{l}) \tilde{\phi}\_{t}
$$

### Modelling of phase-shifting transformers

In cases where the power system is equipped with phase-shifting transformers whose ratings are known, ad hoc classical power studies can be carried out to identify the minimum and maximum flow deviations and phase-shift that each component may induce on the grid. The following additional notations are in order:

| Notation                                | Explanation                                                                                     |
|-----------------------------------------|-------------------------------------------------------------------------------------------------|
| $\Pi\_{l}^{+shift} \in \mathbb{R}\_{+}$ | Maximum positive shifting ability of a device equipping link $l$                                |
| $\Pi^{+shift} \in \mathbb{R}^{L}$       | Snapshots formed by all positive synchronous deviations $\Pi\_{l}^{+shift} \in \mathbb{R}\_{+}$ |
| $\Pi\_{l}^{+shift} \in \mathbb{R}\_{-}$ | Maximum negative shifting ability of a device equipping link $l$                                |
| $\Pi^{-shift} \in \mathbb{R}^{L}$       | Snapshots formed by all negative synchronous deviations $\Pi\_{l}^{-shift} \in \mathbb{R}\_{-}$ |

The enhancement of the model with a representation of the phase-shifting components of the real system then requires to re-formulate as follows the binding constraints defined in 7.2:

$$
\forall t \in T, C\_{g}^t Diag(Z\_{l}) \tilde{\phi}\_{t} - \Pi^{-shift} \leq C\_{g}^t Diag(Z\_{l}) \tilde{F}\_{t} \leq C\_{g}^t Diag(Z\_{l}) \tilde{\phi}\_{t} + \Pi^{+shift}
$$

### Modelling of DC components

When the power system graph contains edges that represent DC components, additional notations need be defined:

| Notation              | Explanation                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|
| $L^* \subset L$       | subset of edges representing AC components                                                                          |
| $G^*(N,L^*)$          | subgraph of $G(N,L)$                                                                                                |
| $g^*$                 | spanning tree of $G^*(N,L^*)$                                                                                       |
| $C^*_{g^*}$           | cycle matric of $G^*(N,L^*)$ associated with $g^*$                                                                  |

The proper modeling of the system then requires that all "load flow" constraints defined previously be formulated using notations $(L^*, G^*(N,L^*), C^*\_{g^*})$ instead of $(L, G(N,L), C_{g})$.

### Implementation of security rules N-1,..., N-k

It is assumed here that upstream power system classical calculations on the detailed system are assumed to have provided appropriate estimates for line outage distribution factors (LODFs) for all components involved in the contingency situations to consider. The following additional notations can therefore be introduced:

| Notation                             | Explanation                                                                                                         |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| $O \subset PL$                       | set of situations (single or multiple outages) considered in the contingency analysis                               |
| $Q \in O$                            | situation (incident) considered in the contingency analysis                                                         |
| ${}^Qp_l^m \in [-1,1]$               | LODFs from component $m$ (involved in $Q$) on component $l$ if $Q$ occurs                                           |
| $\underline{F}_l^Q \in \mathbb{R}^T$ | lower bound of the power flow through $l$ if $Q$ occurs                                                             |
| $\overline{F}_l^Q \in \mathbb{R}^T$  | upper bound of the power flow through $l$ if $Q$ occurs                                                             |

The implementation of security rules for the chosen situations requires the following $|L||O|$ additional binding constraints:

$$
\forall Q \in O, \forall l \in L, \underline{F}\_l^Q \leq F_l + \sum_{m \in Q} {}^Qp_l^m F_m \leq \overline{F}_l^Q
$$


[^FB]: FB stands for "flow-based", denomination used in the framework given to the internal electricity market of western Europe.

[^KL]: KL stands for "Kirchhoff-and-Loop". Such a model was used in the European [E-Highway project](http://www;e-highwy2050.eu).