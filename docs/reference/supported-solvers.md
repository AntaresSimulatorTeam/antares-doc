# Supported solvers for Antares

Antares Simulator currently supports multiple solvers and plans to support others.
The use of [OR-Tools](https://developers.google.com/optimization) allows to model the problem
so that multiple solvers can be used. 

## Open source solvers

### Sirius

Originally developped for the needs of Antares by [RTE](https://www.rte-france.com/), 
[sirius solver](https://github.com/AntaresSimulatorTeam/sirius-solver) 
has not been updated since years. However, it still performs really well compared to other 
commercial and open source solvers.

### HiGHS

**Support coming!** This [other open source solver](https://highs.dev/) would replace Sirius 
in the long term. 


## Commercial solvers


### FICO&reg; Xpress

This [commercial solution](https://www.fico.com/en/products/fico-xpress-optimization) 
allows for 0-40% gains in performance depending on parameters compared to Sirius. 

### Gurobi 

**Support coming!** [Gurobi](https://www.gurobi.com/) is another commercial solution that 
could be used by transmission system operator throughout the world.



