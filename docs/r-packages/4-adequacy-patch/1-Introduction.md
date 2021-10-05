# Introduction
## Constats

**L’algorithme opérationnel du couplage des marchés Euphémia** implémente des règles de « dés-optimisation » permettant de définir **le partage de la défaillance entre les zones de marché** lorsqu’il y en a (de telle sorte d’assurer une certaine équité dans le partage de la défaillance) : il s’agit de l'*adequacy patch*.

**Actuellement, cet algorithme n’est pas reproduit dans les études du Bilan prévisionnel.**

Le problème lié à l’absence d’*adequacy patch* dans les études Antares est devenu visible avec l’introduction de la modélisation Flow-Based. Auparavant, ce problème était contourné par le biais d’un mécanisme de *hurdle costs* (petits coûts sur les interconnexions) limitant les exports à partir d’une zone défaillante. Or ce contournement ne s’applique pas sur les frontières Flow-Based. 

Qui plus est les règles de partage de la défaillance, même en dehors du domaine Flow-Based ne sont pas correctement pris en compte par les *hurdle costs* qui priorise le traitement de la défaillance dans les pays directement connectés aux pays disposant de marges, au détriment du traitement de la défaillance dans les pays plus éloignés.

Les conséquences sont les suivantes :

* La France peut exporter et se mettre en défaillance de manière artificielle par ses exports ou au contraire importer de façon trop importante d’autres pays et leur transmettre sa défaillance ;

* Le nombre d’heures de défaillance, en France et dans les autres pays européens, n’est pas juste (a priori sous-estimé pour la France) ;  

* Si une zone au moins est en défaillance, les échanges sont faussés. Or la contribution des interconnexions au mécanisme de capacité est aujourd’hui calculée à partir des imports simulés aux heures où la France est en défaillance.

**Dans un contexte de déclassement des parcs charbon et nucléaires en France et en Europe, les cas de défaillance simultanées tendent à augmenter.** Le problème lié à l’absence d’*adequacy patch* est en conséquence plus visible. Ainsi, dans l’exercice 2019 et pour les configurations les plus défavorables, la France pouvait exporter dans la moitié des situations de défaillance rencontrées.

**Dans un contexte où les marges de de capacité se réduisent, la question de la gestion de la défaillance simultanée dans les études EOD doit donc être instruite.**

## Travaux réalisés antérieurement à RTE/R&D et cadrage pour 2020 

Des premiers travaux ont déjà été initiés par RTE/R&D :

* En 2017, un post-traitement (package R) des sorties des simulations Antares des pays de la zone CWE a été développé. Ce post-traitement permettait de « re-répartir » la défaillance de la zone CWE (lorsqu’il y en a). Ce post traitement n’a pas été utilisé dans le cadre des simulations du BP et son fonctionnement a depuis été remis en cause (l’*adequacy patch* doit cibler toutes les frontières et non uniquement la zone CWE).

* Une analyse détaillée du fonctionnement des règles de partage du *curtailment* implémentées dans EUPHEMIA a été réalisée en 2019 (dans le cadre du projet BP 19). Suite à cette analyse, un premier prototype a été développé, permettant de reproduire le comportement d’Euphemia sur un pas défaillant donné.

**Ces travaux doivent être repris et poursuivis par RTE/R&D, en collaboration avec les équipes BP. La définition d’un programme de travail spécifique à ce sujet a permis de fixer des objectifs atteignables à court et moyen terme pour instruire cette question.**

Pour commencer, le prototype devra être adapté au traitement des simulations BP : traitement de l’ensemble des heures défaillantes, avec détermination du nombre d’heures de défaillance et des flux post adequacy patch. 

Le prototype pourra ensuite être « industrialisé » pour optimiser ses performances et le rendre facilement utilisables par les équipes opérationnelles.

Si l’avancement des travaux n’était pas compatible avec le planning du BP 2020, l’adequacy patch pourrait être utilisé plus tard, pour la mise à jour des paramètres du mécanisme de capacité début 2021 (contribution des interconnexions, cf. lot Mise à jour des paramètres) ou le BP 2021.

**C'est la version industrialisée sous forme d'un nouveau package R qui a été réalisée et décrite dans les chapitres suivants.**
