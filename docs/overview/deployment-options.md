# Deployment options

## Choose what fit your needs

Antares comes bundled in different ways depending on your needs and computing power available.

<div class="grid cards" markdown>
-   :octicons-device-desktop-16:{ .lg .middle } __Desktop__

    ---
    Antares executable for universities and first approach

-   :material-server:{ .lg .middle } __Base__

    ---
    For institutions having servers but no high performance clusters

-   :material-speedometer:{ .lg .middle } __Performance__ 

    ---

    <span style="display: inline-block; background-color: #0078d4; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; margin-top: 8px;">
        <a href="https://antares-simulator.org/pages/presentation/12/" style="color: white; text-decoration: none;">Contact RTE-I :octicons-link-external-16:</a>
    </span>
    
    Ideal for institutions having both servers and high performance computing clusters.

-   :material-remote-desktop:{ .lg .middle } __SaaS__

    --- 
    
    <span style="display: inline-block; background-color: #2ea043; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; margin-top: 8px;">
        Coming!
    </span>
    
    A solution offered by RTE-I for remote access to high performance clusters
</div>

## Side-by-side comparison

Here is a comparison of the different Antares deployment options:


|  | Desktop | Base | Performance[^rtei] | SaaS (coming!) | Legacy |
| --- | --- | --- | --- | --- | --- | 
| Operating system | Ubuntu, Windows | Cross platform for users: Linux, Windows, Mac; Server: Ubuntu | Cross platform for users: Linux, Windows, Mac; HPC on Linux | Cross platform: Linux, Windows, Mac | Windows |
| Performance | Low | Medium | High (depending on your cluster) | High | High (depending on your cluster) |
| Multiple users | ❌ | ✅ | ✅ | ✅ | ✅ |
| HPC | ❌ | ❌ | ✅ SLURM | ✅ SLURM | ✅ SLURM |
| GEMS modelling | ✅ (coming!)| ✅ (coming!)| ✅  (coming!)| ✅ (coming!) | ❌ |
| Xpansion | ✅ | ✅ | ✅ | ✅ | ✅ | 
| Study editing | ✅ | ✅ | ✅ | ✅ | ❌ (import/export studies only) |
| Study variants | ✅ | ✅ | ✅ | ✅ | ❌ |

!!! warning

    Historically, Antares user interface was built alongside the simulator as a "rich client".
    This Legacy interface is now unavailable since v10.0 in favour of Antares Web. 

[^rtei]:
    [RTE international](https://www.rte-international.com/) can bring their expertise for the
    installation, use and support of Antares on your infrastructure. More on their
    [website](https://antares-simulator.org/).


