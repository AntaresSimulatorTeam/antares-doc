# Optimization

## General

#### <span class="param-badge badge-enum">enum</span> `Unfeasible problem behaviour`

Define the behavior of the simulator in case of an unfeasible problem.

- `warning-dry`: Continue simulation.
- `warning-verbose`: Continue simulation, but export the MPS of the unfeasible problem. 
- `error-dry`: Stop simulation.
- `error-verbose` Stop simulation, and export the MPS of the unfeasible problem

#### <span class="param-badge badge-enum">enum</span> `Simplex optimization range`

The simplex optimization range:

- `week`
- `day`

In the formulation of the optimal hydro-thermal unit-commitment and dispatch problem, the reference hydro energy $HIT$ used to set the right hand sides of hydro-constraints depends on the value chosen for this parameter, and is defined as follows:

- `day`: for each day $d$ of the week $\omega$, $HIT = W_d^2$

- `week`: for week $\omega$, $HIT = \sum_{d \in \omega} W_d^2$

    Weekly optimization performs a more refined unit commitment, especially when [`Unit commitment mode`](config-advanced-parameters.md#unit-commitment-mode) is set to `accurate`.

!!! info
    You can have more info on the impact of the optimization range in the [heuristic for seasonal hydro pre-allocation](hydro-heuristic.md).

#### <span class="param-badge badge-enum">enum</span> `Export MPS`

Allow to choose which [MPS files](https://en.wikipedia.org/wiki/MPS_(format)) to export during the simulation.

- `none`: Don't export any MPS file.
- `optim-1`: Export only the MPS file from the first optimization.
- `optim-2`: Export only the MPS file from the second optimization.
- `both`: Export both MPS files from the first and second optimization.

#### <span class="param-badge badge-bool">bool</span> `Binding constraints`

Whether to include binding constraints in the simulation.

#### <span class="param-badge badge-bool">bool</span> `Hurdle costs`

Whether to include hurdle costs in the simulation. 

## Links

#### <span class="param-badge badge-enum">enum</span> `Transmission capacities`

Allow the user to override the transmission capacities on links.

- `local-values`: use the local property for all links, including physical links (no override).
- `null-for-all-links`: override all transmission capacities with 0.
- `infinite-for-all-links`: override all transmission capacities with $\infty$.
- `infinite-for-physical-links`: override transmission capacities with $\infty$ on **physical links only**.
- `null-for-physical-links`: override transmission capacities with 0 on **physical links only**.


## Thermal clusters

#### <span class="param-badge badge-bool">bool</span> `Thermal clusters min stable power`

Whether to activate the constraint of minimum stable power for thermal units.

#### <span class="param-badge badge-bool">bool</span> `Thermal clusters min UD time`

Whether to activate the constraint of minimum start-up time for thermal units.

## Reserve 

#### <span class="param-badge badge-bool">bool</span> `Day ahead reserve`

Whether to activate day-ahead reserve constraints.

#### <span class="param-badge badge-bool">bool</span> `Primary reserve`

Whether to activate primary reserve constraints.

#### <span class="param-badge badge-bool">bool</span> `Strategic reserve`

Whether to activate strategic reserve constraints.

#### <span class="param-badge badge-bool">bool</span> `Spinning reserve`

Whether to activate spinning reserve constraints.
