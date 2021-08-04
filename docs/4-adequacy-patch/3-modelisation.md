# Mathematical modeling

## Approximations

The first quantity necessary to apply the Adequacy Patch is the algebraic domestic energy available for a country, corresponding to the DMRG when it is positive and to the \\( DENS \\) when it is negative. It represents the energy that we want to re-distribute or, on the contrary, that we want to supply to each country. So, we can write the term:

$$
    DMRG - DENS = Production + DTG. MRG – Demand
$$

It is simply a matter of energy that remains available or, on the contrary, lacking after the local supply/demand balance, when accounting for special treatment for the \\( DTG. MRG \\). In Antares, this term reflects a non-activated production capacity. Although, in theory, it is a production term which can be used to trade with other countries, using this term would mean changing the production plans and thus considering dynamic constraints such as linking time steps, which were previously ignored, to one another. This would imply reintroducing additional complexity that we are trying to avoid in a post-processing patch.

The second term is the failure ratio defined for countries that rely on imports to fill their local demand. We will use this term to balance every country in failure, reflecting the equitable sharing of the failure as defined by the curtailment sharing rule.

Failure ratio, in EUPHEMIA, is the ratio of all-price offers accepted by the country to the demand for all-price offers issued (all-price offers are the offers at the maximal market price, which is 3000€/MWh). We do not have access to these values in Antares output, meaning it is necessary to approximate them. Thus, the all-price offers correspond to \\( DENS \\) , since a higher demand would be absurd (the country would have an energy excess which it will only be able to sell at a lower price). Lower demand means that a country could potentially accept a slight failure rather than paying the maximum price for energy it lacks. An additional difficulty is that we need to account for the \\( DTG. MRG \\) , the all-price offers demand approximation becomes \\( DENS + DTG. MRG \\). Indeed, without it, we could impose some failure in the patch output to any country where local failure could be compensated by its potential local production ( \\( DTG. MRG \\) ). Although we do not always allow ourselves to change production plans, it would be absurd to impose a failure on a country with the production means to avoid it. In the same way, we approach the all-price offers accepted by the total imports of the country. We finally get:

$$
    \begin{array}{cc}
        \textrm{Failure ratio} &= \frac{\textrm{All-price offers accepted}}{\textrm{Demand for all-price offers}}
\\
\\
        &\sim 1-\frac{ENS}{(DENS+DTG.MRG)}
    \end{array}
$$

### Objectives and constraints function

A simplified version of the social well-being maximization problem solved by Antares is that of minimizing the total amount of failures, respecting the coupling of Flow-Based specific constraints:

$$
    min ∑ENS
$$ $$
    net~positions∈flowbased
$$

We can then re-write the problem to show the failure ratios:

$$
    min ∑(DENS+DTG.MRG)×\left[ \frac{ENS}{(DENS+DTG.MRG)} \right]
$$

$$
    net~positions∈flowbased
$$

With this new version, the objective function can be reinterpreted as the failure ratios average weighted by the local failure. The adequacy patch then amounts to adding the local matching constraint and
slightly modifying the previous equation, with a quadratic average. Indeed, it tends to penalize the extreme values and so to homogenize the failure ratios.

$$
    min ∑(DENS+DTG.MRG)×\left[ \frac{ENS}{(DENS+DTG.MRG)} \right]^2
$$

$$
    net~position≤DMRG 
$$

$$
    net~positions∈flowbased
$$
