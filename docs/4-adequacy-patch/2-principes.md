# Principes de l’adéquacy patch et règles associées 

Dans la suite du document, on introduit les variables suivantes :

* ENS : Energy Not Served après échange ;

* Margin : marges disponibles dans la zone après échange ;

* DENS : Domestic Energy Not Served (défaillance qu’aurait la zone sans échange, correspondant au déséquilibre local)

* Dmargin : Domestic Margin (marges disponibles dans la zone avant échange)

Il s’entend que pour une zone donnée à chaque instant les couples de variables (ENS, Margin) et (DENS, DMargin) comportent au moins une variable nulle.

## Indétermination à lever :

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
