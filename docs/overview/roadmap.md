# Roadmap
## We are thinking about

A new [heuristic workflow](../reference/config-advanced-parameters/#unit-commitment-mode) between "accurate" and "fast".

## Is coming

Reserves model (FCR, aFFR, mFRR, RR...).
[Gems](https://gems-energy.readthedocs.io/en/latest/) models use cases :
 - in hybrid studies (using both native hardcoded models and new Gems yml models) ;
 - usable with [Antares Craft](https://antares-craft.readthedocs.io/) and Antares Web.
 
Investment on the objects (and not only on links).
New parameters for thermal modulation ramps.

Qualification of a new open source [solver](../reference/supported-solvers/) to replace our old Sirius.

Output data in [Parquet format file](https://parquet.apache.org/), instead of txt.

## 2026 improvements

[Antares Web](https://antares-web.readthedocs.io/) can now manage several HPC Cluster configurations.

[Antares Web](https://antares-web.readthedocs.io/) : new [variants](../tutorials/create-variant/) management options.
	
## 2025 improvements

[Antares Web](https://antares-web.readthedocs.io/) (light client) replaces the old C++ heavy client.

[Antares Craft](https://antares-craft.readthedocs.io/) : new Python library to interact (reading & writing) with Antares studies.

[Antares Xpansion](../reference/xpansion-intro/) : best usage of RAM to avoid saturation.

Peak Shaving post-processing. 
	
## 2024 improvements

[Short terme storage model](../reference/storages/) (Batteries, Pumped Storage Power Plant...).

[Adequacy Patch](../reference/adequacy-patch/) post-processing.

[Antares Xpansion](../reference/xpansion-intro/) : API creation.

[Antares Xpansion](../reference/xpansion-intro/) : best usage of CPU to avoid saturation.

[Antares Xpansion](../reference/xpansion-intro/) : Option to enforce reliability criterion (upper bound on the number of hours of loss of load per area).
