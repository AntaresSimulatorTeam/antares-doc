# Optimization

## General

#### `Unfeasible problem behaviour`

`enum` Define the behavior of the simulator in case of an unfeasible problem.

- `warning-dry`: Continue simulation.
- `warning-verbose`: Continue simulation, but export the MPS of the unfeasible problem. 
- `error-dry`: Stop simulation.
- `error-verbose` Stop simulation, and export the MPS of the unfeasible problem

#### `Simplex optimization range`

`enum` The simplex optimization range:

- `week`
- `day`

In the formulation of the optimal hydro-thermal unit-commitment and dispatch problem, the reference hydro energy $HIT$ used to set the right hand sides of hydro-constraints depends on the value chosen for this parameter, and is defined as follows:

- `day`: for each day $d$ of the week $\omega$, $HIT = W_d^2$

- `week`: for week $\omega$, $HIT = \sum_{d \in \omega} W_d^2$

    Weekly optimization performs a more refined unit commitment, especially when [`Unit commitment mode`](config-advanced-parameters.md#unit-commitment-mode) is set to `accurate`.

!!! info
    You can have more info on the impact of the optimization range in the [heuristic for seasonal hydro pre-allocation](hydro-heuristic.md).

#### `Export MPS`

`enum` Allow to choose which [MPS files](https://en.wikipedia.org/wiki/MPS_(format)) to export during the simulation.

- `none`: Don't export any MPS file.
- `optim-1`: Export only the MPS file from the first optimization.
- `optim-2`: Export only the MPS file from the second optimization.
- `both`: Export both MPS files from the first and second optimization.

#### `Binding constraints`

`bool` Whether to include binding constraints in the simulation.

#### `Hurdle costs`

`bool` Whether to include hurdle costs in the simulation. 

## Links

#### `Transmission capacities`

`enum` Allow the user to override the transmission capacities on links.

- `local-values`: use the local property for all links, including physical links (no override).
- `null-for-all-links`: override all transmission capacities with 0.
- `infinite-for-all-links`: override all transmission capacities with $\infty$.
- `infinite-for-physical-links`: override transmission capacities with $\infty$ on **physical links only**.
- `null-for-physical-links`: override transmission capacities with 0 on **physical links only**.


## Thermal clusters

#### `Thermal clusters min stable power`

`bool` Whether to activate the constraint of minimum stable power for thermal units.

#### `Thermal clusters min UD time`

`bool` Whether to activate the constraint of minimum start-up time for thermal units.

## Reserve 

#### `Day ahead reserve`

`bool` Whether to activate day-ahead reserve constraints.

#### `Primary reserve`

`bool` Whether to activate primary reserve constraints.

#### `Strategic reserve`

`bool` Whether to activate strategic reserve constraints.

#### `Spinning reserve`

`bool` Whether to activate spinning reserve constraints.