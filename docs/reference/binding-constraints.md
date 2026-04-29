# Binding constraints

## Parameters

#### Enabled

<span class="param-badge badge-bool">bool</span>
Whether to enable the binding constraint for the simulation.

#### Name

<span class="param-badge badge-string">string</span>
Name of the constraint.

#### Group

<span class="param-badge badge-string">string</span>
Random or deterministic scenario generation seems more challenging to implement without 
the possibility of imposing the same draw for multiple coupling constraints. 
The constraints within a group would be required to have the same number of second-member time series.


#### Type

<span class="param-badge badge-enum">enum</span>
Antares allows to define three categories of binding constraints:

- `hourly` binding constraints, which are applied to instant power (transmitted and/or generated)
- `daily` binding constraints, that are applied to daily energies. 
    This class makes more sense for commercial modeling 
    (say: imports and exports from/to such and such area should be comprised 
    between such and such lower bound and upper bound). 
    Daily binding constraints are also commonly used to model specific facilities,
    such as pumped storage units operated on a daily cycle
- `weekly` binding constraints, that are applied to weekly energies. 
    Like the previous ones, these constraints may be used to model commercial contracts 
    or various phenomena, such as the operation of a pumped storage power plant operated 
    on a weekly cycle.

#### Bounds

<span class="param-badge badge-enum">enum</span>
Define the sign of the constraint to apply between the left and right hand side:

- `=`: equal to 
- `<`: less than
- `>`: greater than
- `< and >`: different to

#### Constraint terms

A linear combination of link or cluster constraint terms.

!!! note
    You can add a time offset to make the constraint on a time step different than the current one.

## Time series

<span class="param-badge badge-matrix">matrix</span>
The right hand side of the constraint at the same time step given by the [Type](#type) parameter.
