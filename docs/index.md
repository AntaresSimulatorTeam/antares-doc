<figure markdown="span">
    ![logo](assets/logos/antares.png)
</figure>
<h1 style="text-align:center">Comprehensive electrical grid modelling </h1>

Antares is an open source software suite designed to simulate electrical power systems. Its goal are to:

- Provide insight into the evolution trajectories of electricity mix
- Identify key levers to ensure security of supply
- Highlight necessary grid developments to support transformations in the electricity system

Thus, Antares is used for [medium and long-term studies](src/overview/use-cases.md#reports-using-antares).

## Key features

Backed by the french transmission system operator (TSO) RTE, Antares is an industry grade software.

<div class="grid cards" markdown>

-   :material-monitor-dashboard:{ .lg .middle } **Intuitive interface**

    ---

    Modern UI for checking and visualizing studies.

-   :material-lightning-bolt:{ .lg .middle } **Blazing-fast C++ simulation engine**

    ---

    Built for performance and 30 years long studies.

-   :material-console:{ .lg .middle } **Scriptable Python automation**

    ---

    Automation framework to fit your own workflow and to automate tasks.

-   :material-vector-link:{ .lg .middle } **Open, interoperable energy models**

    ---

    Support for generic models for integrating energy transition easily and interoperable between different simulation software

</div>

This software is already used by multiple TSO, companies and universities including :

<div class="logo-grid">
  <div class="logo-item">
    <img src="assets/logos/elia-logo.svg" alt="Elia group" />
  </div>
  <div class="logo-item">
    <img src="assets/logos/apg.png" alt="APG" />
  </div>
  <div class="logo-item">
    <img src="assets/logos/entsoe.svg" alt="entsoe" />
  </div>
  <div class="logo-item">
    <img src="assets/logos/natran.svg" alt="NaTran" />
  </div>
  <div class="logo-item">
    <img src="assets/logos/cea.jpg" alt="CEA" />
  </div>
  <div class="logo-item">
    <img src="assets/logos/rte-light.svg" alt="RTE" /> 
  </div>
  <div class="logo-item">
    <img src="assets/logos/mines-paris-tech-light.png" alt="Mines Paris Tech" />
  </div>
  <div class="logo-item">
    <img src="assets/logos/mepso.svg" alt="Mepso" />
  </div>
</div>

<style>
.logo-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem 3rem;
  margin: 0rem 0;
  align-items: center;
}

.logo-item {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-item img {
  height: 50px;
  width: auto;
  max-width: 120px;
  object-fit: contain;
}

@media (max-width: 600px) {
  .logo-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

## Open source

We believe that open source software is essential in achieving the transformation of tomorrow's energy challenges, transparently and collaboratively. 

Therefore, all Antares technical components are licensed under [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/) apart from [Antares Web](https://github.com/AntaresSimulatorTeam/AntaREST) licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Antares will remain open source for the years to come. We would love to hear from you! Feedback, issues and contributions are welcomed on GitHub or by email.

[Roadmap :octicons-goal-24:](src/overview/roadmap.md){ .md-button }