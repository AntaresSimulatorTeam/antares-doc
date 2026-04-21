# The solver at glance

!!! note

    This pages gives a summary of the whole simulation process followed by Antares in Economy simulations. Adequacy simulations use a simplified variant of it.

The solver 

1. Load or generate time-series of every kind for all system areas. For each Monte-Carlo year, pick up at random or not one time-series of each kind for each area/link. See time-series generation and scenario builder.
 
2. For each Monte-Carlo year :

    1. Apply the hydro heuristic for each area that requires it. The heuristic determines storage energy amount to use for each week/each day depending on simplex-range parameter.
 
    2. For each week/day of the year, run a 168/24-hour optimization process. The aim of this cycle is to minimize the costs throughout the optimization period (one week or one day). This sum may include regular proportional fuel costs, start-up costs and fixed costs, unsupplied and spilled energy costs and hurdle costs on links. The solution has to respect minimum and maximum limits on the power output of each plant, minimum up and down durations, as well as interconnection capacity limits and "binding constraints" at large (which may be technical – e.g. DC flow rules – or commercial – e.g. contracts). Note that the formulation of the problem includes integer variables (because of dynamic constraints on thermal units). The method to deal with this integer variables depends on the unit commitment parameter. If it is set on milp (for versions higher to 8.8), the problem is solved directly with a mixed integer linear programming solver. To reduce computing time, thermal heuristics (fast or accurate heuristic) can be used. With both heuristics, the general optimization sequence is as follows :
    
        1. Minimization of the overall system cost by solving the linear relaxation of the problem. Prior to the optimization, an 8760-hourly vector of operating reserve R3 (see next section) may be added to the load vector solely in this step. This will lead in the next step to start up more thermal units to satisfy reserve requirements than without this operating reserve.
    
        2. Search for integer values of the on/off variables for thermal units that satisfy the dynamic constraints with the smallest possible cost and such that the production found in the previous step is possible regarding Pmin and Pmax constraints.

        3. Take into account the integer values found in the previous step and solve again the schedule problem.
 
3. Apply post-processing such that the annual smoothing algorithm for thermal units and curtailment sharing. 
