# Architecture

Antares is very versatile and can be installed on different infrastructure
depending on your need: on a local machine, on a server or even on a high 
performance computing cluster.

In the following, the architecture of Antares on a server with and without
high performance computing is detailed. It explicits also the interaction 
between different librairies, user scripts and the general workflow.

It is not intended as a technical view but more as a general view and its 
capabilities.

## Base version

In the base version, the application backend and core computations are using a server 
that is not specifically build for high performance.  

![](../assets/diagrams/architecture/base.drawio)

## Performance version

The performance version is different notably because of the underlying high performance
computing (HPC) infrastructure. Another optimization comes from the utilization of SLURM 
to distribute the jobs on the different nodes of the cluster. 

![](../assets/diagrams/architecture/performance.drawio)

