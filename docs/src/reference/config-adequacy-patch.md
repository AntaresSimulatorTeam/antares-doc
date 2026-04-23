# Adequacy patch

#### `Enable adequacy patch`

`bool` Whether to include the [adequacy patch algorithm](adequacy-patch.md).

#### `Exclude contribution of flows between physical areas outside and physical areas inside of the adequacy patch domain for DENS reduction`

`bool` Whether to exclude the contribution of flows between physical areas outside and physical areas inside of the adequacy patch domain for domestic energy not served reduction.

#### `Price taking order`

`enum` Price taking order:

- `DENS`: domestic energy not served
- `Load`:

#### `Include redispatching costs`

`bool` Whether to include redispatching costs. 

#### `Activation threshold` (MW)

`float` Minimum level of the total amount of energy not served "inside" an area of the adq patch domain in order to activate the curtailement sharing rule. 

#### `Threshold for counting local matching rule violations` (MWh)

`float` Threshold used to calculate an output indicator (“LMR VIOL.”) counting the number of situations where the application of local matching led to residual energy deviations exceeding this threshold (0: no tolerance)

#### `Relaxation factor for CSR constraints`

`int` In order to avoid solver issues, lower and upper boundaries of the energy not served variable and lower bound of the spillage variable can be relaxed with this parameter.