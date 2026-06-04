# Roadmap

This roadmap aims to provide visibility into the upcoming developments of our applications. It is indicative and non-binding: our priorities may evolve over time depending on needs, constraints, and opportunities.

We nevertheless share this information to help you anticipate and better envision possible future changes.

## We are working on:

Reserves model (FCR, aFFR, mFRR, RR...).

[Gems](https://gems-energy.readthedocs.io/en/latest/) models use cases:

- in hybrid studies (using both native hardcoded models and new Gems yml models);
- usable with [Antares Craft](https://antares-craft.readthedocs.io/) and Antares Web.
 
Investment on the objects (and not only on links).
New parameters for thermal modulation ramps.

Qualification of a new open source [solver](../reference/supported-solvers.md) to replace our old Sirius.

Output data in [Parquet format file](https://parquet.apache.org), instead of txt.

## We are thinking about:

A new [heuristic workflow](../reference/config-advanced-parameters.md#unit-commitment-mode) between "accurate" and "fast".

## Already delivered

[Complete changelogs](../overview/changelogs.md)

### 2026 improvements

[Antares Web](https://antares-web.readthedocs.io/) can now manage several HPC Cluster configurations.

[Antares Web](https://antares-web.readthedocs.io/) : new [variants](../tutorials/create-variant.md) management options.
	
### 2025 improvements

[Antares Web](https://antares-web.readthedocs.io/) (light client) replaces the old C++ heavy client.

[Antares Craft](https://antares-craft.readthedocs.io/) : new Python library to interact (reading & writing) with Antares studies.

[Antares Xpansion](../reference/xpansion-intro.md) : best usage of RAM to avoid saturation.

Peak Shaving post-processing. 
	
### 2024 improvements

[Short terme storage model](../reference/storages.md) (Batteries, Pumped Storage Power Plant...).

[Adequacy Patch](../reference/adequacy-patch.md) post-processing.

[Antares Xpansion](../reference/xpansion-intro.md) : API creation.

[Antares Xpansion](../reference/xpansion-intro.md) : best usage of CPU to avoid saturation.

[Antares Xpansion](../reference/xpansion-intro.md) : Option to enforce reliability criterion (upper bound on the number of hours of loss of load per area).
