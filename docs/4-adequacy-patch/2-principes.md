# Principes de l’adéquacy patch et règles associées 

Dans la suite du document, on introduit les variables suivantes :

* ENS : Energy Not Served après échange ;

* Margin : marges disponibles dans la zone après échange ;

* DENS : Domestic Energy Not Served (défaillance qu’aurait la zone sans échange, correspondant au déséquilibre local)

* Dmargin : Domestic Margin (marges disponibles dans la zone avant échange)

Il s’entend que pour une zone donnée à chaque instant les couples de variables (ENS, Margin) et (DENS, DMargin) comportent au moins une variable nulle.

## Indétermination à lever

![adequacy-patch](Figure1.png)

*Figure 1 : Indétermination de la répartition de la défaillance en l’absence d’adéquacy patch*

Dans l’exemple présenté, en l’absence d’adéquacy patch, les 2000 MW de marges disponibles en Espagne avant échange peuvent arbitrairement concourir à réduire tout ou partie de la défaillance locale constatée en France ou au Portugal.  On présente 3 propositions équivalentes économiquement pour Antares (de gauche à droite puis de haut en bas) :

    1. Résorber la défaillance de la France ;
    2. Résorber 50% de la défaillance en France et au Portugal ;
    3. Résorber la défaillance au Portugal.

La solution 2 devrait être celle favorisée par l’adéquacy patch, elle est pénalisante en terme de nombre d’heures de défaillance puisqu‘elle maintient à la fois la France et le Portugal en défaillance.

## Règle de Local Matching
### Cas de frontières NTC

![adequacy-patch](Figure2.png)

*Figure 2 : Prise en compte de la règle de Local Matching sur frontières NTC*

La première règle à respecter par l’adéquacy patch est celle dit du « Local Matching ». Cette règle consiste à imposer à un pays qui est localement déséquilibré (DENS > 0, DMargin = 0) de ne pas accentuer son déséquilibre et donc d’être globalement importateur. Par extension, cette règle conduit à interdire à ce qu’un pays qui n’est pas localement déséquilibré (DENS = 0, DMargin >= 0) ne soit pas mis en défaillance et respecte donc après échange (ENS = 0, Margin >= 0).

Dans l’exemple présenté, si la France exporte 1700 MW vers l’Espagne, et l’Espagne exporte 1700 MW vers le Portugal (graphe du haut) alors la France se mettrait volontairement en défaillance pour résorber en partie la défaillance du Portugal via un transit par l’Espagne. Cet échange n’est pas conforme à la règle et la France ne peut donc exporter que 1500 MW vers l’Espagne, qui à son tour ne peut exporter que 1500 MW vers le Portugal.

Avec des liens NTC (capacité d’échange indépendante pour chaque lien), comme ceux considérés dans l’exemple, les « hurdle costs » (coûts de transit) d’Antares devraient favoriser la prise en compte de cette règle car les solutions des 2 graphes sont équivalentes en termes de défaillance globale (510 MW) mais la première augmente de 200 MW le transit entre la France et l’Espagne et entre l’Espagne et le Portugal, ce qui augmente le coût total du système.

### Cas de frontières Flow-Based

Dans le cas d’un domaine Flow-Based, l’objectif d’Antares qui est de minimiser la défaillance globale sur le domaine, conduira à maximiser les exports des zones disposant de marges, sans nécessairement respecter la règle dite de local matching.

![adequacy-patch](Figure3.png)

