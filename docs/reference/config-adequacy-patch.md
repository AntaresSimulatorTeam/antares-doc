# Adequacy patch

#### Enable adequacy patch

<span class="param-badge badge-bool">bool</span>
Whether to include the [adequacy patch algorithm](adequacy-patch.md).

#### Exclude contribution of flows between physical areas outside and physical areas inside of the adequacy patch domain for DENS reduction

<span class="param-badge badge-bool">bool</span>
Whether to exclude the contribution of flows between physical areas
outside and physical areas inside of the adequacy patch domain for domestic
energy not served reduction.

#### Price taking order

<span class="param-badge badge-enum">enum</span>
Price taking order:

- `DENS`: domestic energy not served
- `Load`:

#### Include redispatching costs

<span class="param-badge badge-bool">bool</span>
Whether to include redispatching costs.

#### Activation threshold (MW)

<span class="param-badge badge-float">float</span>
Minimum level of the total amount of energy not served "inside" an area of
the adequacy patch domain in order to activate the curtailment sharing rule.

#### Threshold for counting local matching rule violations (MWh)

<span class="param-badge badge-float">float</span>
Threshold used to calculate an output indicator ("LMR VIOL.") counting the
number of situations where the application of local matching led to residual
energy deviations exceeding this threshold (0: no tolerance)

#### Relaxation factor for CSR constraints

<span class="param-badge badge-int">int</span>
In order to avoid solver issues, lower and upper boundaries of the energy
not served variable and lower bound of the spillage variable can be relaxed
with this parameter.

#### Redispatch

<span class="param-badge badge-bool">bool</span>
