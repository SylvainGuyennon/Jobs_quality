# Jobs_quality

### Une enquête sur la qualité des annonces d'emploi en France


1 Scraping de 3 sites d'annonces d'emploi
2 tri et nettoyage
3 Analyse graphique

Le marché de l'emploi semble etre dans un mauvais état. Mais qu'en dit les données ?

## Phase de Scrapping

J'ai décidé de récupérer les données de trois sites d'emploi sur internet : 
 - Indeed
 - Linkedin
 - APEC

Chacun des sites présente une façon différente de ranger ses annonces, et donc un challenge different à surmonter :  

Indeed n'a besoin que de navigation avec l'utilisation de selenium pour récupérer les données.

Linkedin présente l'inconvéniant de passer un logwall. Il est cependant possible de le passer avec un navigateur automatisé.

L'APEC est le plus simple puisqu'il suffit d'utiliser la librairie requests pour requeter des pages pour recevoir ce qu'elle contiennent sans passer par naviguateur.

Une fois une quantité relativement correctes d'item collectés (environ 300 par site). On peut jeter un oeil aux données.


## Tri et nettoyage

Sachant qu'ils viennent de sites différents, la premiere chose à faire est d'uniformiser les données.

J'ai décidé de partir sur une liste de catégorisation qui me semble plutot exaustive : 
- L'intitule du poste
- L'entreprise
- Le type de contrat 
- L'experience demandée
- Le texte de l'annonce
- Le site
- Le salaire proposé

Après un nettoyage et une normalisation, on aggrège toutes les donnéese en un seul dataframe que l'on va pouvoir analyser.

## Analyse

Spontanément, on peut se poser plusieurs questions : 

Quels sont les types d'emploi proposés ? 

Quelle est l'expérience moyenne demandée ? 

Quel est le taux d'erreur dans les annonces ? (par exemple une annonce indéxée en CDI qui est en fait un stage, ou un entry job avec 3 ans d'expérience demandé)

Après une analyse de texte, on arrive à determiner avec une précision relative (l'important est l'ordre de grandeur) la réalité des offres.






 
 
 
 