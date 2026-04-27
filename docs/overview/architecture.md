# Architecture

## Base version

In the base version, the application backend and core computations are using a server 
that is not specifically build for high performance.  

![](../assets/diagrams/architecture/base.drawio)

## Performance version

The performance version is different notably because of the underlying high performance
computing (HPC) infrastructure. Another optimization comes from the utilization of SLURM 
to distribute the jobs on the different nodes of the cluster. 

![](../assets/diagrams/architecture/performance.drawio)

