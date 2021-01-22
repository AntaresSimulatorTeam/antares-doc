# Resolution of the optimisation problem

This sections aim to describe how the optimisation problem is solved
by __Antares_Simulator__.
The starting point is the problem formulated in the modeling [section](modeling.md).

## The objective 
The _objective_ of the optimisation \\( \Omega\\) is the total cost of the dispatch and is
the sum of several terms: 
$$ \Omega = \Omega_{\mathrm{transmission}} + \Omega_{\mathrm{hydro}} + \Omega_{\mathrm{thermal}} + \Omega_{\mathrm{unsupplied}} + \Omega_{\mathrm{spillage}}$$

The optimal dispatch, however, depends not only on continuous variables (like the power output of a unit,
or the flux through a link) but also on the integer numbers of the running units on each thermal cluster \\(M_{\theta}\\).
The solution is hence found by minimising the _objective_ "first" with respect to \\(M_{\theta}\\) then with respect to the other variables.
other variables. A possible formulation then reads as
$$\min_{\mathrm{flux, thermal power, etc.}}\left( \min_{M_{\theta}} \left(\Omega\right)\right)$$

A different formulation allows to separate the problem in two parts "Unit Commitment" and "Optmal Dispatch"
with their respective objectives.

$$\min_{M_{\theta}\mathrm{arg\,min}\left(\Omega_{\mathrm{unit.com.}}\right)}\left(\Omega_{\mathrm{dispatch}}\right)$$
The two \\(\Omega_{\mathrm{unit.com.}}\\) and \\(\Omega_{\mathrm{dispatch}}\\) are very similar and differs
only with respect to the state of the thermal units, and consequently the form of its cost
$$\Omega_{\mathrm{thermal}} = \sum_{n\in N}\sum_{\theta\in \Theta_n}\left( \chi_\theta P_\theta + \sigma_\theta^+ M_\theta^+ + \tau_\theta M_\theta\right)$$ 



that goes in further details
is hence found by of on The optimum is defined by minimising \\( \Omega_{\mathrm{dispatch}}\\) by considering the  
$$M_{\theta}$$

$$\min_{flux, prod. thermique, etc} \min_{nombre de palliers allumés} \Omega$$

$$ \Omega_{\mathrm{dispatch}} = \Omega_{\mathrm{transmission}} + \Omega_{\mathrm{hydro}} + \Omega_{\mathrm{thermal}} + \Omega_{\mathrm{unsupplied}} + \Omega_{\mathrm{spillage}}$$

Hello test \\( \bar{F} \mathbb{R}\\) \\(\bar{C}\\) 
