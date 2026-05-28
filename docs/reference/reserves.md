# Reserves

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