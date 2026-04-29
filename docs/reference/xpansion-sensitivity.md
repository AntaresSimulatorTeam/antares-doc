# Launch the sensitivity analysis

## Sensitivity input file creation

In order to run the sensitivity analysis, the user must create a JSON file named `sensitivity_in.json` that is stored in the `user/expansion/senstivity` directory of the Antares study.

```
antares-study
└─── input
└─── layers
└─── logs
└─── output
└─── settings
└─── user
│   └───expansion
│       │   candidates.ini
│       │   settings.ini
│       │   ...
|       └───sensitivity
|           | sensitivity_in.json
```

The file `sensitivity_in.json` contains 3 fields:

- `epsilon` (float) : Defines the maximum gap with the optimal solution that is allowed.
- `capex` (bool) : If `true`, the CAPEX sensitivity problems are solved (minimization and maximization), otherwise they are not solved.
- `projection` (list of strings) : List of candidate names for which the projection of the set of $\varepsilon$-optimal solutions is computed. For each candidate, two problems are solved: minimization and maximization of the invested capacity.

An sample `sensitivity_in.json` is given below:
```json
{
    "epsilon" : 1e4,
    "capex": false,
    "projection": ["peak", "semibase"]
}
```

## Run the sensitivity analysis

The sensitivity analysis can be launched from the command line as follows:

```
antares-xpansion-launcher.exe -i examples\SmallTestFiveCandidates --step sensitivity  --simulationName mySimulation.zip
```

- The `-i` parameter specifies the Antares study folder path.
- The `--step` parameter specifies that we launch a sensitivity analysis.
- The `--simulationName` parameter (optional) is the name of the Antares Xpansion output archive on which we wish to
  perform the sensitivity analysis. If `--simulationName` is not specified, the most recently modified output of the
  Antares study folder will be used. The output used by the sensitivity analysis **must contain the results of an
  Antares Xpansion optimization**.

The problems solved during the sensitivity analysis use the same solver settings and integrality constraints on the candidates as those used beforehand to perform the corresponding Antares Xpansion optimization.

## Output of the sensitivity analysis

The sensitivity analysis module creates a JSON file `sensitvity_out.json` that is stored in the directory `output/simulation-name/sensitivity` of the Antares study folder.

A sample output file is given below:

```json
{
	"antares" : 
	{
		"version" : "8.1.0"
	},
	"antares_xpansion" : 
	{
		"version" : "0.6.0"
	},
	"best benders cost" : 178836183.38241878,
	"epsilon" : 10000,
	"sensitivity solutions" : 
	[
		{
			"candidates" : 
			[
				{
					"invest" : 948.01436354994814,
					"name" : "peak"
				},
				{
					"invest" : 0,
					"name" : "semibase"
				}
			],
			"objective" : 56880861.812996887,
			"optimization direction" : "min",
			"problem type" : "capex",
			"status" : 0,
			"system cost" : 178846183.38241878
		},
		{
			"candidates" : 
			[
				{
					"invest" : 1201.3053164764756,
					"name" : "peak"
				},
				{
					"invest" : 400,
					"name" : "semibase"
				}
			],
			"objective" : 108078318.98858854,
			"optimization direction" : "max",
			"problem type" : "capex",
			"status" : 0,
			"system cost" : 178846183.38241878
		},
		{
			"candidates" : 
			[
				{
					"invest" : 584.99719014093932,
					"name" : "peak"
				},
				{
					"invest" : 400,
					"name" : "semibase"
				}
			],
			"objective" : 584.99719014093932,
			"optimization direction" : "min",
			"problem type" : "projection peak",
			"status" : 0,
			"system cost" : 178846183.38241875
		},
		{
			"candidates" : 
			[
				{
					"invest" : 1759.8724009014643,
					"name" : "peak"
				},
				{
					"invest" : 0,
					"name" : "semibase"
				}
			],
			"objective" : 1759.8724009014643,
			"optimization direction" : "max",
			"problem type" : "projection peak",
			"status" : 0,
			"system cost" : 178846183.38241875
		},
	]
}
```

In this example, we have performed the sensitivity analysis with the following input file:
```json
{
    "epsilon" : 1e4,
    "capex": false,
    "projection": ["peak"]
}
```

The output file gathers the following data:

- The version of Antares and Antares Xpansion that is used,
- `best benders cost`: Best upper bound, that is the optimal overall cost, found in the Antares Xpansion optimization that was executed beforehand,
- `epsilon`: Maximum gap with the optimal solution that is allowed,
- `sensitivity solutions`: An array containing data for each sensitivity problem that is solved:

    - `objective`: Value of the objective of the sensitivity problem:
    
        - For a CAPEX minimization (resp. maximization) problem, this the value of the mimimum (resp. maximum) CAPEX that is found over the $\varepsilon$-optimal solutions. 
        - For the minimization (resp. maximization) projection problem of candidate $i$, this is the minimum (resp. maximum) invested capacity of candidate $i$ over the $\varepsilon$-optimal solutions.
    
    - `optimization direction`: The direction of the sensitivity problem i.e. minimization or maximization,
    - `problem type`: The type of sensitivity problem that is solved,
    - `status`: Optimization status

        - 0: optimal,
        - 1: infeasible,
        - 2: unbounded.

    - `candidates` : An array describing an $\varepsilon$-optimal investment combination that satisfies the bound found in the sensitivity problem:
        - For a CAPEX minimization (resp. maximization) problem, this is an $\varepsilon$-optimal investment combination that minimizes (resp. maximizes) the CAPEX.
        - For the minimization (resp. maximization) projection problem of candidate $i$, this is an $\varepsilon$-optimal investment combination that minimizes (resp. maximizes) the capacity of candidate $i$.

    - `system cost`: Value of the overall system cost obtained with the investment combination given in `candidates`.

!!! note 
    - For the projection problem on candidate $i$, we logically retrieve that the `objective` is equal to the invested capacity in candiate $i$ from the `candidates` section.
    - For all sensitivity problems, we must have `system cost <= best benders cost + epsilon` as this is the constraint that is enforced. As the solutions of a linear program are on the boundary of the domain, it is often the case (but not always) that this constraint is saturated for the sensitivity solutions, so that we have `system cost = best benders cost + epsilon`.
    