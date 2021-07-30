# Introduction
## Observations

**EUPHEMIA, the power market coupling operational algorithm,** implements "de-optimization" rules to define **failure sharing between market areas** when necessary (to ensure a certain equity in failure sharing). This is the *adequacy patch*.

**This algorithm is not currently used in the Projected Supply Estimate (PSE) studies.**

The lack of *adequacy patch* became a visible problem in some Antares studies when the Flow-Based modeling was introduced. This problem could previously be by-passed using a *hurdle costs* mechanism (small costs added to interconnections) limiting the exports from a failing area. Yet, this bypass does not apply to Flow-Based borders. 

What's more, failure sharing rules (even outside of the Flow-Based domain) are not correctly considered by the *hurdle costs* which prioritize failure treatment in countries directly connected to those with margins, at the expense of failure treatment in the furthest countries.

The consequences are the following:

* France can export and artificially put itself in failure with those exports or, on the contrary, import too much from other countries and transmit its failure to them;

* The failure number of hours in France and in the other European countries is not right (a priori under-estimated for France);

* If at least one area is failing, exchanges are distorted. Yet, the interconnections contribution to the capacity mechanism is currently calculated from imports simulated at hours when France is in failure.

**In a context of coal and nuclear power plants decommissioning in France and in Europe, the cases of simultaneous failures tend to increase.** The problem related to the lack of *adequacy patch* is therefore more visible. Thus, in the 2019 exercise and in the most unfavorable configurations, France could export in half of the failure situations encountered.

**In a context where capacity margins are shrinking, the issue of simultaneous failure management in Supply and Demand Balance studies must therefore be addressed.**

## Previous work at RTE/R&D and framework for 2020 

Initial work has already been initiated by RTE/R&D:

* In 2017, a post-processing (R package) of the Antares simulations outputs of the CWE zone countries was developed. This post-processing allowed to "re-distribute" the CWE zone failure (when there is one). This post-processing was not used in the PSE simulations and its functioning has since been questioned (the *adequacy patch* must target all borders and not only the CWE zone).

* A detailed analysis of the functioning of the *curtailment* sharing rules implemented in EUPHEMIA was performed in 2019 (as part of the PSE 19 project). Following this analysis, a first prototype was developed, allowing to reproduce the behavior of EUPHEMIA on a given failure step.

**This work must be taken up and continued by RTE/R&D, in collaboration with the PSE teams. The definition of a specific work program on this subject has made it possible to set achievable objectives in the short and medium term to address this issue.**

To begin with, the prototype will have to be adapted to the processing of PSE simulations: processing of all the failing hours, with determination of the number of failing hours and of the post adequacy patch flows. 

The prototype can then be "industrialized" to optimize its performances and make it easily usable by the operational teams.

If the progress of the work is not compatible with the planning of the PSE 2020, the adequacy patch could be used later for the update of the parameters of the capacity mechanism at the start of 2021 (contribution of the interconnections, cf. Parameter update package) or for the PSE 2021.

**The industrialized version has been realized in the form of a new R package and is described in the following chapters.**
