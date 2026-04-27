# Adequacy patch

#### <span class="param-badge badge-bool">bool</span> `Enable adequacy patch`

Whether to include the [adequacy patch algorithm](adequacy-patch.md).

#### <span class="param-badge badge-bool">bool</span> `Exclude contribution of flows between physical areas outside and physical areas inside of the adequacy patch domain for DENS reduction`

Whether to exclude the contribution of flows between physical areas outside and physical areas inside of the adequacy patch domain for domestic energy not served reduction.

#### <span class="param-badge badge-enum">enum</span> `Price taking order`

Price taking order:

- `DENS`: domestic energy not served
- `Load`:

#### <span class="param-badge badge-bool">bool</span> `Include redispatching costs`

Whether to include redispatching costs. 

#### <span class="param-badge badge-float">float</span> `Activation threshold` (MW)

Minimum level of the total amount of energy not served "inside" an area of the adq patch domain in order to activate the curtailement sharing rule. 

#### <span class="param-badge badge-float">float</span> `Threshold for counting local matching rule violations` (MWh)

Threshold used to calculate an output indicator ("LMR VIOL.") counting the number of situations where the application of local matching led to residual energy deviations exceeding this threshold (0: no tolerance)

#### <span class="param-badge badge-int">int</span> `Relaxation factor for CSR constraints`

In order to avoid solver issues, lower and upper boundaries of the energy not served variable and lower bound of the spillage variable can be relaxed with this parameter.
