# General configuration

#### <span class="param-badge badge-enum">enum</span> `Mode`

Simulation mode for the computation:

- `Economy`: Antares simulator will try to ensure balance between load and generation, while minimizing the economical cost of the grid's operation (more on this here). Economy simulations make a full use of Antares optimization capabilities. They require economic as well as technical input data and may demand a lot of computer resources.
- `Adequacy`: In this mode, all power plant operational costs are considered zero. Antares' only objective is to ensure balance between load and generation. Adequacy simulations are faster and require only technical input data. Their results are limited to adequacy indicators.
- `Economy (linear relaxation)`: Antares simulator will optimize the investments on the grid, minimizing both investments and operational costs.

#### <span class="param-badge badge-int">int</span> `First day`

Index of first day to include in the study in [1, 365] or [1, 366] for leap years.

#### <span class="param-badge badge-int">int</span> `Last day`

Index of last day to include in the study in [1, 365] or [1, 366] for leap years.

#### <span class="param-badge badge-string">string</span> `Horizon`

The horizon year of the study (static tag, not used in the calculations).

#### <span class="param-badge badge-enum">enum</span> `Year`

Allow to set the first month of the year.  

#### <span class="param-badge badge-enum">enum</span> `Week`

Allow to set the first day of the week.

#### <span class="param-badge badge-string">string</span> `1st January`

Indicate the day of the week for january 1st of the given year.

#### <span class="param-badge badge-bool">bool</span> `Leap year`

Whether the year is a leap year.

#### <span class="param-badge badge-int">int</span> `Number`

Number of Monte-Carlo (MC) years that should be prepared for the simulation (not always the same as the MC years actually simulated, which are defined by user-playlist and playlist parameters).

#### <span class="param-badge badge-enum">enum</span> `Building mode`

- `Automatic`: All time-series will be drawn at random.
- `Custom`: The simulation will be carried out on a mix of deterministic and probabilistic conditions, with some time-series randomly drawn and others set to user-defined values. This option allows setting up detailed "what if" simulations that may help to understand the phenomena at work and quantify various kinds of risk indicators. To set up the simulation profile, use the [scenario builder](../tutorials/build-scenario.md).
- `Derated`: All time-series will be replaced by their general average and the number of MC years set to 1. If the TS are ready-made or Antares-generated but are not to be stored in the INPUT folder, no time-series will be written over the original ones (if any). If the time-series are built by Antares and if it is specified that they should be stored in the INPUT, a single average-out time series will be stored instead of the whole set.

#### <span class="param-badge badge-enum">enum</span> `Selection mode`

- `Automatic`
- `Custom` 

#### <span class="param-badge badge-bool">bool</span> `Simulation synthesis`


#### <span class="param-badge badge-bool">bool</span> `Year-by-year`


#### <span class="param-badge badge-bool">bool</span> `MC scenario`
