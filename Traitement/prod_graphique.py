# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:37:04 2021

@author: Syl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_csv("df_agg.csv", index_col=0)

df.index = range(0, len(df))

# sample_size = len(df)
# originals = len(df.drop_duplicates(ignore_index = True))
                
# duplicates = sample_size - originals
# labels = ["Annonces", "duplicatas"]
# data = [originals,duplicates]

# def make_autopct(values):
#     def my_autopct(pct):
#         total = sum(values)
#         val = int(round(pct*total/100.0))
#         return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
#     return my_autopct
# plt.figure(figsize =(10,8))
# plt.pie([originals,duplicates], explode = (0 ,0.1), labels = labels, shadow =True, autopct=make_autopct(data))



df = df.drop_duplicates(ignore_index = True)

dico_type = {"101888": "CDI" , "101887": "CDD" , "101889": "Interim", '597137' : 'Alternance', '597138': 'contrat_pro'}
dico_xp = {"200269": "non_rempli", '597152':'confirmé','597153':'confirmé','597151':'Entry level','597150':'Entry level'}

df['xp'].replace(dico_xp, inplace = True)
df['type_contrat'].replace(dico_type, inplace = True)