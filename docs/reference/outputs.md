# Outputs

At the end of an Antares simulation, the outputs are time series.
These results are indicators grouped [by area](#by-area) and [by link](#by-link).
There is also the possibility to have a synthesis of all the results.

Moreover, users can view these results at a preferred temporality:

- hourly
- daily
- weekly
- monthly
- annual

??? note "Adequacy vs. economy simulations"

    **In adequacy simulations,** all dispatchable thermal units are given the 
    [`must-run`](./thermals.md#must-run) status 
    (hence, they will generate at maximum power, regardless of the demand). 
    As a consequence the only variables that are actually meaningful are the adequacy indicators 
    (unsupplied energy, LOLD, LOLP), that may depend on assumptions made regarding the economic values 
    of unsupplied and spilled energies, and on hurdle costs on interconnections.
    In the specific case where binding constraints are present in the study, 
    **all thermal clusters will consequently be de-activated from the binding constraints**. 
    This can lead to incorrect adequacy indicators in Antares studies containing binding constraints 
    in adequacy simulations.

    As a consequence, both adequacy and economy simulations yield the same values 
    for the adequacy indicators under the following conditions: 
    if hurdle costs on interconnections are higher than the difference between the maximum and
    minimum unsupplied energy cost (or VOLL) assigned to the different areas of the system, 
    and if no binding constraint is altered due to the fact that they contain clusters in must-run.

## By area

#### OV.COST

The overall cost corresponds to the sum of the operating cost, unsupplied cost, spilled cost,
and hydro cost.

#### OV. COST CSR

Same as the [overall cost](#ovcost), but with CSR (curtailment sharing rule)
unsupplied cost version[^adqp]

#### OP.COST

The operating cost corresponds to the sum of proportional costs and non-proportional costs.

#### MRG. PRICE

Locational marginal price corresponding to the overall economic effect of a local 1MW load increase.

#### MRG. PRICE CSR

<!-- TODO -->

#### DTG by plant

Dispatchable thermal generation for any active thermal cluster that is to say its production.

#### MIN DTG by plant

For any active thermal cluster, minimum between:

- the cluster production
- the product of the minimum generation modulation, the number of units
  and the nominal capacity associated to the cluster

#### RES generation by plant

For any active renewable cluster, its production (necessarily must-run).
Only when using clustered renewable generation modeling.

#### CO2, NH3, SO2... EMIS.

Amount emitted by all dispatchable thermal plants for polluants:
CO2, SO2, NH3, NOX, PM2_5, PM5, PM10, NMVOC, OP1, OP2, OP3, OP4, OP5 EMIS.

#### BALANCE

Overall import/export balance of the area (positive value: export).

#### ROW BAL

Rest of the worl balance, that is to say import/export with areas outside the modeled system
(positive value: import)[^12].

#### PSP

User-defined settings for pumping and subsequent generating.

#### MISC. NDG

Miscellaneous non-dispatchable generation.

#### LOAD

Demand (including DSM potential if relevant).

#### RES LOAD

Residual load, formula:

```
RES LOAD = load - allMustRunGeneration
         = load - (wind + solar + miscGen + ROR + mustRunSum) 
```

where `mustRunSum = total production of thermal clusters must-run and enabled`.

#### H.ROR

Hydro generation, Run-of-river share.

#### WIND

Wind generation (only when using aggregated Renewable generation modeling).

#### SOLAR

Solar generation (thermal and PV)
(only when using aggregated Renewable generation modeling).

#### WIND OFFSHORE

Wind offshore generation
(only when using clustered Renewable generation modeling)

#### DISPATCH. GEN.

Dispatchable generation for thermal clusters

#### RENEWABLE GEN.

Renewable generation
(only when using clustered Renewable generation modeling).

#### H.STOR

Power generated from energy storage units (typically: Hydro reservoir).

#### H.PUMP

Power absorbed by energy storage units (typically: PSP pumps consumption).

#### H.LEV

Energy level remaining in storage units
(percentage of reservoir size).

#### H.INFL

External input to the energy storage units (typically: natural inflows).

#### H.OVFL

Wasted natural inflow overflowing from an already full energy storage unit.

#### H.VAL

Marginal value of stored energy (typically: shadow water value).

#### H.COST

Expenses/Income brought by energy storage actions (H.STOR, H.PUMP).

#### <STS **group**\>_injection

Injection of energy from the area into each short-term storage group.

#### <STS **group**\>_withdrawal

Withdrawal of energy from each short-term storage group into the area.

#### <STS **group**\>_level

Average level of each short-term storage group.

#### <STS\>,P-injection

Injection of energy from the area into the short-term storage

#### <STS\>,P-withdrawal

Withdrawal of energy from the short-term storage into the area

#### UNSP. ENRG

Unsupplied energy: adequacy indicator (Expected Energy Not Served–EENS).

#### UNSP. ENRG. CSR

Unsupplied energy after CSR (demand that cannot be satisfied)[^adqp].

#### DENS

Domestic Energy Not Supplied:
the difference between the local production capabilities of an area and its local load[^adqp].

#### LMR. VIOL

Local Matching Rule Violation after the Antares Simulation
as defined by the adequacy patch[^adqp].

#### SPIL. ENRG

Spilled energy (energy produced that cannot be used and has to be wasted).

#### LOLD

Loss of load duration: adequacy indicator (length of shortfalls).

#### LOLD CSR

Loss of load duration, CSR (Curtailment Sharing) version:
same as above, but based on unsupplied energy CSR (see **UNSP. ENRG. CSR**)
rather than **UNSP. ENRG**[^adqp]

#### LOLP

The loss of load probability is an adequacy indicator corresponding to the 
probability of at least one hour of shortfall within the considered period,
without normalization by the duration of the considered period.

#### LOLP CSR

Loss of Load probability, CSR (Curtailment Sharing) version:
same as above, but based on unsupplied energy CSR (see [**UNSP. ENRG. CSR**](#unsp-enrg-csr))
rather than [**UNSP. ENRG**](#unsp-enrg)[^adqp].

#### AVL DTG

Available dispatchable thermal generation (sum of available power over all plants).

#### DTG MRG

Disp. Ther. Gen. (AVL DTG – sum of all dispatched thermal generation)

#### MAX. MRG

Maximum margin: operational margin obtained if the hydro storage energy
of the week were used to maximise margins instead of minimizing costs

#### DTG MRG CSR

DTG MRG after CSR[^adqp]

#### NP COST

Non-proportional costs of the dispatchable plants (start-up and fixed costs)

#### NP Cost by plant

Same as above, but by dispatchable plant

#### NODU

Number of Dispatched Units.

!!! note
    NODU and NP Cost do not appear in "Adequacy" results since these variables 
    are irrelevant in that context.

#### Profit

Net profit of the cluster in euros[^15]:

```
(MRG. PRICE - marginal cost of the cluster) × (dispatchable production of the cluster)
```

!!! note
    In `economy` simulations, all variables have a techno-economic meaning.
    In `adequacy` simulation, only the adequacy indicators are: UNSP. ENRG, LOLD and LOLP.

!!! note
    The net profit is computed on full precision values for MRG. PRICE. 
    The user may obtain slightly different results applying the given formula because MRG. 
    PRICE values are rounded to 10^-2.

## By link

#### FLOW LIN.

Flow (signed + from upstream to downstream) assessed by the linear optimization. 
These flows follow Kirchhoff's law only if these laws have been explicitly enforced 
by suitable binding constraints.

#### UCAP

Used capacity: absolute value of FLOW LIN. This indicator may be of interest to differentiate 
the behavior of interconnectors showing low average flows: in some cases, 
this may indicate that the line is little used, while in others, 
this may be the outcome of high symmetric flows.

#### LOOP FLOW

Flow circulating through the grid when all areas have a zero import/export balance. 
This flow, due to the simplification of the real grid, 
is not subject to hurdle costs during the optimization.

#### FLOW QUAD.

Flow computed anew, starting from the linear optimum,
by minimizing a quadratic function equivalent to an amount of Joule losses,
while staying within the transmission capacity limits.
This calculation uses the impedances found in the "Links" input data.
If congestions occur on the grid, these results are not equivalent to those of a DC load flow.

#### CONG. FEE ALG

Algebraic congestion rent = linear flow × (downstream price – upstream price).

#### MARG. COST

Decrease of the system's overall cost that would be brought by the optimal use
of an additional 1 MW transmission capacity (in both directions).

#### CONG PROB +

Up>Dwn Congestion probability = (NC+) / (total number of MC years) with:
NC+ = number of years during which the interconnection was congested in the Up>Dwn way
for **any** length of time within the time frame relevant to the file.

#### CONG PROB -

Dwn>Up Congestion probability = (NC-) / (total number of MC years) with:
NC- = number of years during which the interconnection was congested in the Dwn>Up way
for **any** length of time within the time frame relevant to the file.

#### HURD. COST

Contribution of the flows to the overall economic function through the "hurdle costs" component.
For each hour:

```
if (FLOW LIN. – LOOP FLOW) > 0`
    HURD. COST = (hourly direct hurdle cost) × (FLOW LIN.)
    else HURD. COST = (hourly indirect hurdle cost) × (-1) × (FLOW LIN.)
```

## Economy and Adequacy, other results

Depending on the options chosen in the main simulation window, 
the output folders may also include either, both or none of the following sections:

| `output/<simu_id>/ts-numbers/` |                     |                      |
|--------------------------------|---------------------|----------------------|
|                                | `/load`             | `/<area_names>/...`  |
|                                | `/thermal`          | `/<area_names>/...`  |
|                                | `/hydro`            | `/<area_names>/...`  |
|                                | `/wind`[^agg]       | `/<area_names>/...`  |
|                                | `/solar`[^agg]      | `/<area_names>/...`  |
|                                | `/renewables`[^ren] | `/<area_names>/...`  |
|                                | `/ntc`              | `/<area_names>/...`  |

These files contain, for each kind of time-series, the number drawn (randomly or not) 
in each Monte-Carlo year (files are present if "output profile / MC scenarios" was set to "true").

| `output/<simu_id>/ts-generator/` |                |                                |
|----------------------------------|----------------|--------------------------------|
|                                  | `/load`        | `/batch_number/area_names/...` |
|                                  | `/hydro`       | `/batch_number/area_names/...` |
|                                  | `/wind`[^agg]  | `/batch_number/area_names/...` |
|                                  | `/solar`[^agg] | `/batch_number/area_names/...` |


These files contain, for each kind of Antares-generated time-series, 
copies of the whole set of time-series generated.

## Miscellaneous

Alike Input data, output results can be filtered so as to include only items 
that are associated with Areas and Links defined as "visible" in the current map. 
In addition, the output filtering dialog box makes it possible to filter according to 
two special categories (**Districts** and **Unknown**) that are not related to standard maps:

- **Districts** displays only results obtained for spatial aggregates
- **Unknown** displays only results attached to Areas or Links that no longer exist 
  in the Input dataset (i.e. study has changed since the last simulation)

### Dynamic Aggregation for Sets of Areas (Districts)
#### Overview

- **Thermal groups**: dispatchable production of the group
- **Renewable groups**: production of the group
- **Short-term storage groups**: level, injection and withdrawal of the group

#### Where these columns appear

These dynamic aggregation columns appear in:

- `areas/name/values-*.txt` (hourly, daily, etc.) files in mc-all synthesis reports 
  (Data Level: `setOfAreas`)
- `areas/name/values-*.txt` (hourly, daily, etc.) files in mc-ind/year_number year-by-year reports 
  (Data Level: `setOfAreas`)

#### Column Naming Convention

For each thermal group, renewable group, or short-term storage group, the columns follow this pattern:

- **Single-year reports** (`mc-ind`): `<group>_TH_PROD`, `<group>_RES_PROD`, `<group>_INJECTION`, 
  `<group>_WITHDRAWAL`, `<group>_LEVEL`
- **Synthesis reports** (`mc-all`): `<group>_TH_PROD`, `<group>_RES_PROD`, `<group>_INJECTION`, 
  `<group>_WITHDRAWAL`, `<group>_LEVEL`

The suffixes indicate:

- `_TH_PROD`: Thermal production (total)
- `_RES_PROD`: Renewable production (total)
- `_INJECTION`: Short-term storage injection (total)
- `_WITHDRAWAL`: Short-term storage withdrawal (total)
- `_LEVEL`: Short-term storage level (average)

#### Available Variables

The following group types can be used for dynamic aggregation:

| Variable type      | Description | Column pattern (per group)                                                                        |
|--------------------|-------------|---------------------------------------------------------------------------------------------------|
| Thermal clusters   | Production  | `<group>_TH_PROD`, `<group>_RES_PROD`, `<group>_INJECTION`, `<group>_WITHDRAWAL`, `<group>_LEVEL` |
| Renewable clusters | Injection   | `<group>_INJECTION`, `<group>_WITHDRAWAL`, `<group>_LEVEL`                                        |
| Short-term storage | Injection   | `<group>_INJECTION`, `<group>_WITHDRAWAL`, `<group>_LEVEL`                                        |

#### Dynamic vs Static Groups

| Aspect | Static Groups | Dynamic Groups |
|--------|-----------------------------|-----------------------|
| Definition | Defined once in study input | Defined dynamically based on plant `group` attribute |
| Column count | Limited to available groups | Can scale with number of districts |

#### Notes

- Dynamic district variables are handled differently from other variables for technical reasons
  - They cannot be enabled/disabled with thematic trimming
  - They cannot be enabled/disabled with geographic trimming

- For short-term storage `LEVEL` columns, values represent **averages** (not hourly values) 
  computed over the period of time (day, week, month or year)
- The number of columns generated scales with the number of districts and groups defined in your study
- To enable dynamic aggregation, define sets of areas in your study input


[^12]: Value identical to that defined under the same name in the "Misc Gen" input section.

[^adqp]: Please note that this output variable is only available in the economy mode, if adequacy patch is activated and the area the output variable belongs to is inside the adequacy patch domain (see [Adequacy Patch](adequacy-patch.md))

[^agg]: This output is only available if the parameter "renewable generation modelling" is set to "cluster" in the input of the simulation

[^ren]: This output is only available if the parameter "renewable generation modelling" is set to "aggregated" in the input of the simulation

[^15]: dispatchable production = power generation above min gen = (power generation) - (min gen modulation)*units*capacity

### The Annual System Cost Output file

In addition to the general output files, the Output folder of each economic or adequacy simulation includes, at its root, a file "Annual\_System\_Cost.txt" It presents the metrics of a global Monte-Carlo variable further denoted ASC.

The value of ASC for any given simulated year is defined as the sum, over all areas and links, of the annual values of the area-variable "OV.COST" and of the link-variable "HURD. COST".

The metrics displayed in the "Annual system cost" file take the form of four values:

- Expectation `EASC`
- Standard deviation `SASC`
- Minimum `LASC`
- Maximum `UASC`

As with all other random variables displayed in the Antares Output section, the computed standard deviation of the variable can be used to give a measure of the confidence interval attached to the estimate of the expectation. For a number of Monte-Carlo years N, the law of large numbers states for instance that there is a 95 % probability for the actual expectation of ASC to lie within the interval:

$$
\texttt{EASC} \pm 1.96 \dfrac{\texttt{SASC}}{\sqrt{N}}
$$

There is also a 99.8 % probability that it lies within the interval:

$$
\texttt{EASC} \pm 3 \dfrac{\texttt{SASC}}{\sqrt{N}}
$$

### Changelog

The following table contains a list of new output variables in recent versions.

| Version | Variable(s) introduced | Files                     | Enabled by default |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------|
| 8.0     | none                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                           |                    |
| 8.1     | WIND OFFSHORE, WIND ONSHORE, SOLAR CONCRT., SOLAR PV, SOLAR ROOFT, RENW. 1, RENW. 2, RENW. 3, RENW. 4                                                                                                                                                                                                                                                                                                                                                                                             | values-*.txt              | yes                |
| 8.1     | MISC. DTG 2, MISC. DTG 3, MISC. DTG 4                                                                                                                                                                                                                                                                                                                                                                                                                                                             | values-*.txt              | yes                |
| 8.2     | none                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                           |                    |
| 8.3     | DENS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | values-*.txt              | no                 |
| 8.3     | Profit by plant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | details-*.txt             | yes                |
| 8.4     | BC. MARG. COST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | binding-constraints-*.txt | no                 |
| 8.5     | LMR VIOL., SPIL. ENRG. CSR, DTG MRG CSR                                                                                                                                                                                                                                                                                                                                                                                                                                                           | values-*.txt              | no                 |
| 8.6     | PSP_open_injection, PSP_open_withdrawal, PSP_open_level, PSP_closed_injection, PSP_closed_withdrawal, PSP_closed_level, Pondage_injection, Pondage_withdrawal, Pondage_level, Battery_injection, Battery_withdrawal, Battery_level, Other1_injection, Other1_withdrawal, Other1_level, Other2_injection, Other2_withdrawal, Other2_level, Other3_injection, Other3_withdrawal, Other3_level, Other4_injection, Other4_withdrawal, Other4_level, Other5_injection, Other5_withdrawal, Other5_level | values-*.txt              | yes                |
| 8.6     | STS inj by plant, STS withdrawal by plant, STS lvl by plant                                                                                                                                                                                                                                                                                                                                                                                                                                       | details-STstorage-*.txt   | yes                |
| 8.6     | CO2 EMIS., NH3 EMIS., SO2 EMIS., NOX EMIS., PM2_5 EMIS., PM5 EMIS., PM10 EMIS., NMVOC EMIS., OP1 EMIS., OP2 EMIS., OP3 EMIS., OP4 EMIS., OP5 EMIS.                                                                                                                                                                                                                                                                                                                                                | values-*.txt              | yes                |
| 8.8 | PriceCSR[^16] | values-*.txt | yes |
| 8.8 | UNSP. ENRG CSR[^16] | values-*.txt | yes |
| 8.8 | LOLD_CSR, LOLP_CSR[^16] | values-*.txt | yes |
| 8.8 | MAX MRG CSR[^16] | values-*.txt | yes |
| 8.8 | OV. COST CSR[^16] | values-*.txt | yes |
| 9.1 | **Short-term storage** - dynamic groups instead of static groups. For any group :<br>\<STS group\>_injection <br> \<STS group\>_withdrawal <br> \<STS group\>_level| values-*.txt | yes |
| 9.2.0 | MIN DTG by plant | details-\*.txt | yes |
| 9.2.1, 9.3.0 | NPCAP HOURS | values-\*.txt | yes |
| 9.3 | Use dynamic groups for thermal dispatchable generation and renewable generation, instead of static groups. 


[^16] : this output variable was introduced both in **8.8** and **9.2**, meaning that **9.0** and **9.1** don't have it.