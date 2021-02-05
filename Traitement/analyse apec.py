# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:15:08 2021

@author: Syl
"""

import pandas as pd
df = pd.read_csv("../data_extraites/data_apec.csv" ,index_col=0)

def cleaning(x):
    balises = ["<p>","</p>","<strong>","</strong>","<li>","<ul>","</li>","</ul>","<br />","<div>" , "</div>"]
    for i in balises : 
        x = x.replace(i,"")
    x = x.replace(u'\xa0', u' ')
    return x

df['texteHtmlProfil'] = df['texteHtmlProfil'].apply(cleaning)
df['texteHtml'] = df['texteHtml'].apply(cleaning)
df['texteHtmlEntreprise'] = df['texteHtmlEntreprise'].apply(cleaning)
        
df_t = df
df_t['texte'] = df_t['texteHtmlProfil'] + df_t['texteHtml'] + df_t['texteHtmlEntreprise']
df_t = df_t.drop(columns=["texteHtmlProfil",'texteHtml','texteHtmlEntreprise'], axis = 1)