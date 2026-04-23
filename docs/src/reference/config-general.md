# General configuration

#### `Mode`

`enum` Simulation mode for the computation:

- `Economy`: Antares simulator will try to ensure balance between load and generation, while minimizing the economical cost of the grid's operation (more on this here). Economy simulations make a full use of Antares optimization capabilities. They require economic as well as technical input data and may demand a lot of computer resources.
- `Adequacy`: In this mode, all power plant operational costs are considered zero. Antares' only objective is to ensure balance between load and generation. Adequacy simulations are faster and require only technical input data. Their results are limited to adequacy indicators.
- `Economy (linear relaxation)`: Antares simulator will optimize the investments on the grid, minimizing both investments and operational costs.

#### `First day`

`int` Index of first day to include in the study in [1, 365] or [1, 366] for leap years.

#### `Last day`

`int` Index of last day to include in the study in [1, 365] or [1, 366] for leap years.

#### `Horizon`

`string` The horizon year of the study (static tag, not used in the calculations).

#### `Year`

`enum` Allow to set the first month of the year.  

#### `Week`

`enum` Allow to set the first day of the week.

#### `1st January`

`string` Indicate the day of the week for january 1st of the given year.

#### `Leap year`

`bool` Whether the year is a leap year.

#### `Number`

`int` Number of Monte-Carlo (MC) years that should be prepared for the simulation (not always the same as the MC years actually simulated, which are defined by user-playlist and playlist parameters).

#### `Building mode`

`enum`

- `Automatic`: All time-series will be drawn at random.
- `Custom`: The simulation will be carried out on a mix of deterministic and probabilistic conditions, with some time-series randomly drawn and others set to user-defined values. This option allows setting up detailed "what if" simulations that may help to understand the phenomena at work and quantify various kinds of risk indicators. To set up the simulation profile, use the [scenario builder](../tutorials/build-scenario.md).
- `Derated`: All time-series will be replaced by their general average and the number of MC years set to 1. If the TS are ready-made or Antares-generated but are not to be stored in the INPUT folder, no time-series will be written over the original ones (if any). If the time-series are built by Antares and if it is specified that they should be stored in the INPUT, a single average-out time series will be stored instead of the whole set.

#### `Selection mode`

`enum`

- `Automatic`
- `Custom` 

#### `Simulation synthesis`

`bool`

#### `Year-by-year`

`bool`

#### `MC scenario`

`bool`