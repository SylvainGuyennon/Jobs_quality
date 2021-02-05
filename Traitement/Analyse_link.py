# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:26:58 2021

@author: Syl
"""

import pandas as pd
df = pd.read_csv("..\data_extraites\data_linkedin.csv",index_col=0)

# df["texte"] = df['texte'].apply(lambda x: x.replace("'", "").replace("[", "").replace("]", "").replace("–", "").replace("\\","").replace("<ul>","").replace("<li>","").replace('</li>', '').replace("</ul>", ' '))

# #on recherche sir l'annonce est un stage
# df['stage_i'] = 0
# df['stage_i'] = df['intitule'].apply(lambda x: 1 if "Stagiaire" in x or "stagiaire" in x or "STAGIAIRE" in x or "Stage" in x or "STAGE" in x or "stage" in x else 0)

# df['stage_t'] = 0
# df['stage_t'] = df['texte'].apply(lambda x: 1 if "Stagiaire" in x or "stagiaire" in x or "STAGIAIRE" in x or "Stage" in x or "STAGE" in x or "stage" in x else 0)

# len(df.query('stage_t == 1 or stage_i ==1'))

