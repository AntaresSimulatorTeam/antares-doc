# Reserves

!!! info
    This feature is available before v10.2 of Antares Simulator.

<span class="param-badge badge-matrix">matrix</span>
This window is used to handle all input data regarding reserves 
and the potential of *smart* load management (when not modeled using *fake* thermal dispatchable plants). On picking any area in the primary list, 
the user gets direct access to all data regarding the area, which amount to four ready-made 
8760-hour time series (expressed in MW). Those reserves are available in either adequacy or economy simulations:

- `Primary reserve`
- `Strategic reserve`
- `Day-ahead reserve`: power accounted for in setting up the optimal unit-commitment and schedule of the following day(s),
which must consider possible forecasting errors or last-minute incidents. If the optimization range is of one day, 
the reserve will be actually seen as "day-ahead". If the optimization range is of one week, 
the need for reserve will be interpreted as "week-ahead".
- `DSM`: power (decrease or increase) to add to the load. A negative value is a load decrease, a positive value is a load increase. Note that an efficient demand side management scheme may result in a negative overall sum (All simulation modes).


!!! info
    This feature is available since v10.2 of Antares Simulator.
    
Reserves refer to the power margins available to the grid operator to maintain the balance between generation and consumption at all times. 
Reserves therefore serve to: 
•	handle fluctuations in consumption (rapid changes in demand), 
•	compensate for generation fluctuations (power plant outages, drops in wind or solar output), 
•	ensure grid stability (frequency, voltage, cross-border exchanges).

## General
### Global parameters
#### Reference activation duration up (h)
<span class="param-badge badge-float">int</span>
Reference activation duration (in hours) for UP reserves. A value of 0 disables the constraints specific to the stock energy level for this reserve.

#### Power Activation Ratio up
<span class="param-badge badge-float">float</span>
A parameter between 0 and 1.

#### Reference activation duration down (h)
<span class="param-badge badge-float">int</span>
Reference activation duration (in hours) for DOWN reserves. A value of 0 disables the constraints specific to the stock energy level for this reserve.

#### Power Activation Ratio down
<span class="param-badge badge-float">float</span>
A parameter between 0 and 1.


### Specific parameters
#### Name
<span class="param-badge badge-string">string</span>
User defined name of the reserve.

#### Type
<span class="param-badge badge-string">string</span>
Type of reserve.

- `Up`
- `Down`

#### Failure cost (€/MWh)
<span class="param-badge badge-float">float</span>
Failure cost.

#### Spillage cost (€/MWh)
<span class="param-badge badge-float">float</span>
Spillage cost.

#### Reference activation duration (h)
<span class="param-badge badge-float">int</span>
Reference activation duration (in hours). A value of 0 disables the constraints specific to the stock energy level for this reserve.

#### Power Activation Ratio
<span class="param-badge badge-float">float</span>
A parameter between 0 and 1.

#### Energy Activation Ratio
<span class="param-badge badge-float">float</span>
A parameter between 0 and 1.

## Needs
<span class="param-badge badge-matrix">matrix</span>
This window allows the user to:

- `View a reserve's demand profiles`
- `Modify a reserve's demand profiles`
- `Import demand time series`
- `Create scenarios for a reserve's demand profiles`


## Certification
#### Name
<span class="param-badge badge-string">string</span>
User defined name of the reserve.

#### Enabled
<span class="param-badge badge-bool">bool</span>
Whether to enable this cluster for production.

#### Participation cost (€/MW)
<span class="param-badge badge-float">float</span>
Cost (in €/MW) of the cluster's participation in each reserve.

#### Participation cost off (€/MW)
<span class="param-badge badge-float">float</span>
Cost (in €/MW) of the cluster's participation in each reserve for units that are shut down.

#### Max power (MW)
<span class="param-badge badge-float">float</span>
Maximum cluster participation (in MW).

#### Max power off (MW)
<span class="param-badge badge-float">float</span>
Maximum contribution of shut-down units (in MW).

## Symmetry
<span class="param-badge badge-matrix">matrix</span>
This window allows you to define symmetry groups in order to :

- `Declare symmetrical behaviors with respect to several reserves`
- `share behaviors`
- `avoid redundant configurations`
- `ensure consistency between reserves`