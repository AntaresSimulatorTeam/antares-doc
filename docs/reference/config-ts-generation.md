# Time series generation

The generator of time series calculates available capacities for each cluster at every hour:

$$
\text{nominal capacitiy} \times \text{capacitity modulation} \times \text{number of available units}
$$

where $\text{number of available units} = \text{total units} - \text{planned outage} - \text{forced outage}$.

#### Number stochastic TS

<span class="param-badge badge-int">int</span>
The number of stochastic time series to generate.

#### Thermal outage details

<span class="param-badge badge-bool">bool</span>
