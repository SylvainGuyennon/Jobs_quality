# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:35:37 2021

@author: Syl
"""
import pandas as pd

df = pd.DataFrame(columns =['intitule','entreprise','type_contrat','xp','texte','site', 'salaire'])


df_l = pd.read_csv("..\data_extraites\data_linkedin.csv",index_col=0)
df_l['site']="Linkedin"
df_l.columns = ['intitule','entreprise','type_contrat','xp','texte','site']




df_a = pd.read_csv("../data_extraites/data_apec.csv" ,index_col=0)
df_a['texte'] = df_a['texteHtmlProfil'] + df_a['texteHtml'] + df_a['texteHtmlEntreprise']
df_a = df_a.drop(columns=["texteHtmlProfil",'texteHtml','texteHtmlEntreprise'], axis = 1)
df_a['site']="apec"
df_a.columns = ['intitule','entreprise','type_contrat','xp','salaire','texte','site']




df_i = pd.read_csv("..\data_extraites\data_indeed.csv",index_col=0)
df_i['site']="indeed"

def fonction(x):
    result = ""
    if 'Stage' in str(x) : 
        result +='stage '
    if "CDI" in str(x) :
        result +='CDI '
    if "CDD" in str(x) :
        result +='CDD '
    if "Intérim" in str(x) :
        result +='Intérim '
    if "Apprentissage" in str(x) : 
        result += 'Apprentissage '
    if "Freelance / Indépendant" in str(x) : 
        result += 'Freelance '
    if result == "" :
        result = "Non rempli"
    return result

df_i['type']= df_i['Type Contrat'].apply(fonction)

df_i['salaire'] = df_i['Type Contrat'].astype('str')
for i in ["Stage","CDI","CDD","Intérim","Apprentissage","Temps plein","Temps partiel", 'Contrat pro', "Freelance / Indépendant",',',"-"]:
    for j in range(len(df_i)):
        df_i.loc[j,'salaire'] = df_i['salaire'][j].replace(i, '')

df_i = df_i.drop(columns=["Type Contrat"], axis = 1)
       
