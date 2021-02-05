# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pandas as pd
import requests
import time

#on check le nombre max d'annonces

url = 'https://www.apec.fr/cms/webservices/rechercheOffre'
myjson = {"lieux":[],"fonctions":[],
          "statutPoste":[],
          "typesContrat":[],"typesConvention":[],
          "niveauxExperience":["101881"],
          "idsEtablissement":[],"secteursActivite":[],
          "idNomZonesDeplacement":[],
          "positionNumbersExcluded":[],
          "typeClient":"CADRE","sorts":[{"type":"SCORE","direction":"DESCENDING"}],
          "pagination":{"range":20,"startIndex":20},"activeFiltre":True,
          "pointGeolocDeReference":{"distance":0},
          "motsCles":"data analyst"}
x = requests.post(url, json = myjson)
y = x.text


liste_totale =[]

#on isole le nombre max 
nb_job_total = int(y[-4:-1])

for i in range((nb_job_total//100)+1):
    myjson_total = {"lieux":[],
                "fonctions":[],
                "statutPoste":[],
                "typesContrat":[],
                "typesConvention":[],
                "niveauxExperience":["101881"], #coorespond à junior
                "idsEtablissement":[],
                "secteursActivite":[],
                "idNomZonesDeplacement":[],
                "positionNumbersExcluded":[],
                "typeClient":"CADRE","sorts":[{"type":"SCORE","direction":"DESCENDING"}],
                "pagination":{"range":100,"startIndex":i*100},"activeFiltre":True,
                "pointGeolocDeReference":{"distance":0},"motsCles":"data analyst"}
    x = requests.post(url, json = myjson_total)
    split = x.headers["X-Search-Results"].split()
    liste_totale += split

    

df = pd.DataFrame(columns =['intitule','nomCompteEtablissement','idNomTypeContrat','idNomNiveauExperience','texteHtmlProfil','texteHtmlEntreprise','texteHtml','salaireTexte'])

liste_lien =[]

for i in liste_totale:
    data_offre = "https://www.apec.fr/cms/webservices/offre/public?numeroOffre="+i
    liste_lien.append(data_offre)

for i in liste_lien:
    data = requests.get(i,).json()
    item_offre=[]
    time.sleep(0.5)
    for j in ['intitule','nomCompteEtablissement','idNomTypeContrat','idNomNiveauExperience','texteHtmlProfil','texteHtmlEntreprise','texteHtml','salaireTexte']:
        try:
            item_offre.append(data[j])
        except KeyError:
            item_offre.append("None")
        
    df.loc[len(df)] = item_offre
    
    
df.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer')