# Jobs_quality
### Une enquête sur la qualité des annonces d'emploi en France

Le marché de l'emploi semble être dans un mauvais état. 88 % des demandeurs d'emploi utilisent Internet pour effectuer des démarches effectives de recherche, selon une enquête Ifop pour Pôle emploi de 2017.
En effet les sites d'annonces semblent être une véritable mine, indispensable de nos jours pour trouver du travail.

Cependant, après de nombreuses heures passées à envoyer des CV et autres lettres de motivation sans succès, et face à l'apparente inexactitude de nombreuses annonces, j'ai eu l'idée de faire une analyse plus poussée des annonces dans mon domaine (la data analyse).

## Phase de Scrapping

J'ai décidé de récupérer les données de trois sites d'emploi sur internet : 
 - Indeed
 - Linkedin
 - APEC

Chacun des sites présente une façon différente de ranger ses annonces, et donc un challenge différent à surmonter :  

Indeed n'a besoin que de navigation avec l'utilisation de sélénium pour récupérer les données.

Linkedin présente l'inconvénient de passer un logwall. Il est cependant possible de le passer avec un navigateur automatisé.

L'APEC est le plus simple puisqu'il suffit d'utiliser la librairie request pour requêter des pages, et ainsi recevoir ce qu'elle contient sans passer par le navigateur.

Une fois une quantité relativement correcte d'item collectés (environ 300 par site). On peut jeter un œil aux données.


## Tri et nettoyage

Sachant qu'ils viennent de sites différents, la première chose à faire est d'uniformiser les données.

J'ai décidé de partir sur une liste de catégorisation qui me semble plutôt exhaustive : 
- L'intitulé du poste
- L'entreprise
- Le type de contrat 
- L'expérience demandée
- Le texte de l'annonce
- Le site
- Le salaire proposé

Après un nettoyage et une normalisation, on agrège toutes les données en un seul dataframe que l'on va pouvoir analyser.

## Analyse

Spontanément, on peut se poser plusieurs questions : 

Quels sont les types d'emploi proposés ? 

Quelle est l'expérience moyenne demandée ? 

Quel est le taux d'erreur dans les annonces ? (par exemple une annonce indexée en CDI qui est en fait un stage, ou un entry job avec 3 ans d'expérience demandé)

Après une analyse de texte, on arrive à déterminer avec une précision relative (l'important est l'ordre de grandeur) la réalité des offres.


### Note: les duplicatas

Il s'agit simplement d'annonces postées plusieurs fois.

![Graphique dupli](./Traitement/Images/Duplicata.png)


On peut voir que plus de 20% des annonces sont postés plus d'une fois, les raisons peuvent être multiples : 

- Repost après qu'une salve de candidats ne soit pas pris,
- Repost par des bots, qui polluent les site avec des annonces qui ne sont plus à jour,
- Fausses annonces qui consistent à sonder le marché de l'emploi

Un écriture plus soignée des annonces en premier lieu pourrait permettre de réduire cette part.


### Quels sont les types d'emploi proposés ? 

Premier point délicat, les types d'emploi encodés dans les annonces ne sont pas forcément les véritables types. Un travail de recherche s'est imposé.

Certains sites ne répertorient pas de types de contrats, ou juste "temps plein", ce qui ne donne que trop peu d'indications.

Un exemple graphique : 

![Graphique types](./Traitement/Images/Tx_types.png)

On peut voir naturellement une forte propension aux CDI.


### Quelle est l'expérience moyenne demandée ? 

* à finir

 
### Quel est le taux d'erreur dans les annonces ?

Il s'agit ici de comparer les informations du texte des annonces avec les informations encodées au sein des sites. Chaque site propose son système.

On va déjà comparer avec l'expérience demandée

![Graphique types](./Traitement/Images/Fautes_xp.png)

Note = Indeed ne permet pas d'encoder de niveau d'expérience. Je ne peux donc pas comparer :(


On peut remarquer un score mauvais pour Linkedin (Plus de 50%!).
Il peut être expliqué par le fait qu'il s'agit du site le plus important, et donc le plus enclin aux erreurs. Je ne m'attendais cependant pas à un tel niveau.

L'APEC propose un système d'encodage plus fin, les erreurs viennent souvent du fait qu'il existe un encodage "tout niveaux acceptés", alors que ce n'est pas du tout le cas.

Linkedin propose un encodage "Débutant", qui demandent la plupart du temps une expérience d'au moins 2-3 ans

Mes quelques pistes de l'origine de ces erreurs sont :
- Des bots mal programés
- Des rédacteurs d'annonces qui ne prennent pas la peine de choisir des cases, soit par erreur, soit par manque de réalisme dans leurs attentes.


# Conclusion
 

