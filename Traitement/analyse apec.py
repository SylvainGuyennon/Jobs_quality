# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:15:08 2021

@author: Syl
"""

import pandas as pd
df = pd.read_csv("C:/Users/Syl/Data/Cours/format/data_apec.csv" ,index_col=0)

def cleaning(x):
    balises = ["<p>","</p>","<strong>","</strong>","<li>","<ul>","</li>","</ul>","<br />"]
    for i in balises : 
        x = x.replace(i,"")
    x = x.replace(u'\xa0', u' ')
    return x

df['texteHtmlProfil'] = df['texteHtmlProfil'].apply(cleaning)
df['texteHtml'] = df['texteHtml'].apply(cleaning)
df['texteHtmlEntreprise'] = df['texteHtmlEntreprise'].apply(cleaning)

df["annéeTxt"]=""
for i in range(216):
    try:
        df.loc[i,"annéeTxt"] = df['texteHtmlProfil'][i][df['texteHtmlProfil'][i].index(" an")-1]
    except : 
        df["annéeTxt"][i]=None
