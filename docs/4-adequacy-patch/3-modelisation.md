# Modélisation mathématique
## Approximations

La première quantité nécessaire à l’application de l’Adequacy Patch est l’énergie domestique algébrique disponible pour un pays, correspondant à la DMRG si elle est positive, et à la  \\( DENS \\)  si elle est négative. Elle représente l’énergie qu’on va chercher à redistribuer ou au contraire à combler dans chaque pays. On peut donc écrire ce terme :


$$
	DMRG - DENS = Production + DTG. MRG – Demande
$$

Il s’agit simplement de l’énergie qui reste disponible ou au contraire qui manque après l’équilibre offre/demande local, en prenant en compte un traitement particulier pour la  \\( DTG. MRG \\)  : dans Antares, ce terme traduit une capacité de production non activée. Bien qu’en théorie, ce soit bien un terme de production, dans lequel on peut donc tirer pour échanger avec d’autres pays, utiliser ce terme reviendrait à changer les plans de production, et donc à prendre en compte des contraintes dynamiques, liant les pas de temps les uns aux autres, que l’on avait jusque-là ignorer. Cela impliquerait de réintroduire une complexité supplémentaire que l’on cherche justement à éviter dans un patch de post-traitement.


Le deuxième terme est le ratio de défaillance défini pour les pays dépendants d’imports pour combler leur demande local. C’est lui qu’on cherchera à équilibrer pour tous les pays en défaillance, traduisant le partage équitable de la défaillance tel que défini par la règle de curtailment sharing.

Dans l’Euphémia, il est défini comme le rapport des offres à tous prix acceptées par le pays sur la demande d’offres à tous prix émises (les offres à tous prix étant définies comme les offres aux prix maximal du marché, soit 3000€/MWh). Nous n’avons pas accès à ces grandeurs en sortie d’Antares, et il est donc nécessaire d’en faire des approximations.
Ainsi, la demande d’offres à tous prix correspond environ à la  \\( DENS \\) , étant donné qu’une demande plus importante serait absurde (le pays aurait alors un surplus d’énergie qu’il ne pourrait revendre qu’à un prix inférieur) et qu’une demande inférieure correspond au fait que le pays pourrait potentiellement accepter une légère défaillance plutôt que de payer l’énergie qu’il lui manque au prix maximal.
Une difficulté supplémentaire et qu’il faut ici prendre en compte la  \\( DTG. MRG \\) , l’approximation de la demande d’offres à tous prix devenant  \\( DENS + DTG. MRG \\) . En effet, sans celui-ci, on pourrait imposer de la défaillance en sortie du patch à un pays dont la défaillance local pourrait être comensée par sa production locale potentielle ( \\( DTG. MRG \\) ). Bien qu’on ne s’autorise toujours par à changer les plans de production, il serait absurde d’imposer de la défaillance à un pays qui a les moyens de production pour l’éviter.
De la même manière, on approche les offres à tous prix acceptées par les imports totaux du pays.
On obtient finalement :
$$
	\begin{array}{cc}
		\textrm{Ratio de defaillance} &= \frac{\textrm{Offres a tous prix acceptees}}{\textrm{Demande d offres a tous prix}}
\\
\\
		&\sim 1-\frac{ENS}{(DENS+DTG.MRG)}
	\end{array}
$$


###Fonction objectif et contraintes

Une écriture simplifiée du problème de maximisation du bien-être social résolu par Antares est celui de minimisation du volume total de défaillance, en respectant les contraintes couplantes spécifiques au flow-based :
$$
	min ∑ENS
$$
$$
	net~positions∈flowbased
$$

On peut alors réécrire ce problème pour faire apparaître les ratios de défaillance :
$$
	min ∑(DENS+DTG.MRG)×\left[ \frac{ENS}{(DENS+DTG.MRG)} \right]
$$
$$
	net~positions∈flowbased
$$

Dans cette nouvelle écriture, on peut réinterpréter la fonction objectif comme la moyenne des ratios défaillance pondérée par la défaillance locale.
L’Adequacy patch revient alors à rajouter la contrainte de local matching et à modifier légèrement l’objectif précédent, en en faisant la moyenne quadratique. En effet, celle-ci tend à pénaliser les valeurs extrêmes et donc à homogénéiser les ratios de défaillance.
$$
	min ∑(DENS+DTG.MRG)×\left[ \frac{ENS}{(DENS+DTG.MRG)} \right]^2
$$
$$
	net~position≤DMRG 
$$
$$
	net~positions∈flowbased
$$
