# Assumptions on the problem

## Breakdown of weekly supproblems

- All uncertainties known within the week are considered, with no visibility on other weeks (except for long-term storage through the heuristic’s deliberately limited visibility, and probabilistically for VU).​

- Over-optimization of dispatch → lower marginal prices.​

- Dynamic constraints between weeks are taken into account through cyclicity, which assumes that the residual consumption is the same at the beginning and at the end of the week.​

## Centralized planner with 1-hour time steps​

- Simple market bid formats.​

- Actor strategies inconsistent with the minimization of total system costs (EVs not exposed to market prices, monopoly situations leading actors to influence prices to maximize their profits).​

- Actors arbitrate between preserving flexibility to minimize imbalance settlement, or conversely not necessarily remaining balanced.​

- More successive optimizations are required to converge toward the minimum cost so that all actors have the same information.​

## DC assumptions on the network

- The studied network is a high-voltage grid: the reactance $X$ is much greater than
the resistance $R$ in a high-voltage network, therefore $X \gg R$.​

- The network is highly meshed with relatively short line lengths: the voltage angle
difference between two nodes is small.​

- The voltage level $V$ is similar along the same line between two nodes: the network
is meshed with sufficiently well-distributed generation and consumption.​

## Aggregation of zones

- The zone is assimilated to a copper plate with optimal dispatch.​

- In NTC, the influence on lines is independent of the location of
injections/withdrawals within the zone. In FB and in equivalent network models,
part of this information is recovered.​

## Representatino of line capactities

- Maximum/minimum flows obtained from different studied supply demand equilibrium situations on the
detailed network (in $N$ or $N-1$) → this method overestimates/underestimates
capacity.​

- Linear regression between the equivalent branch flow (sum of line flows) and the
maximum congestion rates of lines (in $N-1$ or $N$) → this method is a compromise.​

## Aggregation of generation assets

- Clusters include units with the same characteristics.​

- Storages have the same values of P_inj / stock_max and P_inj / P_withdraw,
otherwise flexibility would change.​

## Simplified modeling of assets

- Incomplete technical constraints (e.g., two deep ramp-downs for nuclear units).​

## Simplified optimization

- Prices are determined with fixed UC (Unit Commitment); the impact of a start-up
is not taken into account → lower marginal prices.​

- Negative or very low prices require the integration of curtailable power, restrictions
on pumping/turbining, and the inclusion of start-up/shutdown information for units
(MILP).​

- Solution close to the optimum but not exact.​