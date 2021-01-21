# Resolution of the optimisation problem

This sections aim to describe how the optimisation problem is solved
by __Antares_Simulator__.
The starting point is the problem formulated in the modeling [section](modeling.md).

## The objective 
The _objective_ of the optimisation \\( \Omega\\) is defined as the total cost of the dispatch, 
is the sum of several terms as follow 
$$ \Omega = \Omega_{\mathrm{transmission}} + \Omega_{\mathrm{hydro}} + \Omega_{\mathrm{thermal}} + \Omega_{\mathrm{unsupplied}} + \Omega_{\mathrm{spillage}}$$

The optimal dispatch, however, depends not only on continuous variables (like the power output of a unit,
or the flux through a link) but also on the (integer) number of running units on each thermal cluster \\(M_{\theta}\\).
The solution is hence found by minimising the _objective_ "first" with respect to \\(M_{\theta}\\) then with respect to the other variables.
other variables.

A possible formulation then reads as
$$\min_{\mathrm{flux, thermal power, etc.}}\left( \min_{M_{\theta}} \left(\Omega\right)\right)$$

A different formulation allows to separate the problem in two parts "Unit Commitment" and "Optmal Dispatch".


that goes in further details
is hence found by of on The optimum is defined by minimising \\( \Omega_{\mathrm{dispatch}}\\) by considering the  
$$M_{\theta}$$

$$\min_{flux, prod. thermique, etc} \min_{nombre de palliers allumés} \Omega$$

$$ \Omega_{\mathrm{dispatch}} = \Omega_{\mathrm{transmission}} + \Omega_{\mathrm{hydro}} + \Omega_{\mathrm{thermal}} + \Omega_{\mathrm{unsupplied}} + \Omega_{\mathrm{spillage}}$$
