# Create a blank study

Creating a blank study is fairly easy. You need to click on the 
:octicons-plus-circle-16: **Create** button in the top left.
Give it a name and select the study version you want to use. 
This will depend on the list of installed executables on your installation
as the study version corresponds to the version of 
[Antares Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator) used 
to do the core computations.

## Managed vs. on disk studies

In Antares Web, you have the possibility to store your studies either on the disk or in a 
database. The later possibility is called, **managed studies** because it lets Antares Web the
management of the data to optimize the memory efficiency, 
avoid data duplication and increase the responsiveness of the app.

Another advantage of managed studies is the possibility to make variants of a main study. 
It is ideal for evaluating the impact of the variation of a certain parameter. 
**This is not possible with on disk studies.** 

!!! tip

	Given all these advantages, you should use as often as possible managed studies.

As a consequence, you cannot directly access the file tree of the study as you could 
if the study lived locally on your computer. You can still export the study file tree 
to your local machine via the export button in the top right dropdown menu.

!!! note

	Note that when you launch the study via Antares Web, it automatically transfers 
    the corresponding file tree to the simulation executables as this is their input format.
