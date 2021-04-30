# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:37:04 2021

@author: Syl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text).replace(u'\xa0', u' ').replace('deux', "2").replace('trois',"3").replace('quatre',"4").replace('cinq', '5')

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


### On transcrit les types de contrats ###

dico_type = {"101888": "CDI " , "101887": "CDD " , "101889": "Intérim ", '597137' : 'Alternance', '597138': 'contrat_pro'}
dico_xp = {"200269": "non_rempli", '597152':2,'597153':3,'597151':1,'597150':0}

df['xp'].replace(dico_xp, inplace = True)
df['type_contrat'].replace(dico_type, inplace = True)

for i in range(len(df)):
    if "stage" in df['type_contrat'][i]:
        df['type_contrat'][i] = 'Stage '
    if "Alternance" in df['type_contrat'][i] or "Apprentissage" in df['type_contrat'][i]:
        df['type_contrat'][i] = 'Apprentissage '

df['texte'] = df['texte'].apply(remove_html_tags)

df['type_reel'] = None




def is_stage(x) :
    if "stagiaire" in x.lower() or"stage" in x.lower() or " internship" in x.lower() :
        return "stage"
    
df['type_reel'] = df['intitule'].apply(is_stage)
i=0
for i in range(len(df)):
    if "stage" in df['type_contrat'][i].lower():
        df['type_reel'][i] = 'stage'
    if df['type_reel'][i] == None :
        df['type_reel'][i] = df['type_contrat'][i]  

for i in range(len(df)):
    if "stage" in df['intitule'][i].lower():
        df['type_reel'][i] = 'stage'
    if "alternance" in df['intitule'][i].lower() or "apprentissage" in df['intitule'][i].lower():
        df['type_reel'][i] = 'Apprentissage '
    if "cdd" in df['intitule'][i].lower():
        df['type_reel'][i] = 'CDD '
    if "cdi" in df['intitule'][i].lower():
        df['type_reel'][i] = 'CDI '
    if "cdd" in df['texte'][i].lower():
        df['type_reel'][i] = 'CDD '
    if "cdi" in df['texte'][i].lower():
        df['type_reel'][i] = 'CDI '
    if "freelance" in df['intitule'][i].lower():
        df['type_reel'][i] = 'Freelance '


# df['typei'] = df['intitule'].apply(is_stage)
# df['typet'] = df['texte'].apply(is_stage)

# sns.countplot(x = df['xp'] , data=df)
# plt.show()
# sns.countplot(x = df['type_contrat'] , data=df)
# plt.show()
# sns.countplot(x = df['type_reel'] , data=df)
# plt.show()
# sns.countplot(x = df['salaire'] , data=df)
# plt.show()
#df['ex'] = df['texte'].apply( lambda x : "expérience" in x.lower() or "experience" in x.lower())

# df_plus = df.loc[(df['type_contrat'] == "Full-time") |(df['type_contrat'] == "Non rempli")]
# df_plus = df_plus.loc[(df['type_reel'] != "stage")]
# df_plus = df_plus.loc[(df['type_reel'] != "CDI ")]
# df_plus = df_plus.loc[(df['type_reel'] != "Apprentissage ")]
# df_plus = df_plus.loc[(df['type_reel'] != "CDD ")]
# df_plus = df_plus.loc[(df['type_reel'] != "Freelance ")]

# df['erreur_type'] = None

# for i in range(len(df)):
#     df['erreur_type'][i] = (df['type_contrat'][i].lower()  == df['type_reel'][i].lower()) 


### Recherche années d'xp ###

def remove_bacs(text):
    """remove les bac+x"""
    clean = re.compile('\+\d')
    return re.sub(clean, '', text)

df['texte'] = df['texte'].apply(remove_bacs)

def split(x) : 
    return x.split('.')

df['texte_s'] = df['texte'].apply(split)


i=0
def isol(case) :
    result = ''
    for i in case :        
        if ('expérience' in i.lower())| ('experience' in i.lower()) :
            result += i
    return result
       

df['texte_xp'] = df['texte_s'].apply(isol)


n_deb=0
n_es = 0
n_prem = 0

def annee_xp(s) :
    if s == None:
        return "none"
    elif "débutant" in s.lower() : 
        global n_deb
        n_deb +=1
        return [0]
    elif 'expérience significative' in s.lower():
        global n_es
        n_es +=1
        return [2]
    elif 'expériences significatives' in s.lower() : 
        return [4]
    elif ('première expérience' in s.lower()) | ('1ère expérience' in s.lower()):
        global n_prem
        n_prem +=1
        return [2]
    elif "expérience confirmée" in s.lower() : 
        return [5]
    elif re.findall(r'\d+', s) != [] : 
       temp = re.findall(r'\d+', s)
       return [number for number in list(map(int, temp)) if number < 13]
    if "justifiez" in s.lower():
       return [2]


def scan(text):
    index = 0
    l = []
    result = ""
    if 'expérience' in text.lower():
        while index < len(text):
            index = text.lower().find("expérience", index)
            if index == -1:
                break
            l.append(index)
            index += len("expérience")
        for ind in l :
            x = ind-30
            y = ind+70
            if x < 0 :
                x=0
            if y > len(text) :
                y=-1                   
            result += (" "+(text[x:y]))
        return result
    elif 'experience' in text.lower() :
        while index < len(text):
            index = text.lower().find('experience', index)
            if index == -1:
                break
            l.append(index)
            index += len('experience')
        for ind in l :
            x = ind-30
            y = ind+70
            if x < 0 :
                x=0
            if y > len(text) :
                y=-1
            result += (" "+(text[x:y]))

        return result

  

df['split_t'] = df['texte'].apply(scan)
df['xp_reel'] = df['split_t'].apply(annee_xp)

print("nb debutant =", n_deb)
print("nb xp_significative = ", n_es)
print("nb première xp = ", n_prem)

## faire marcher ce masque la ###


def formatage(x):
    if x == 'première' : 
        return 2
    elif x == []:
        return np.nan
    elif type(x) is list : 
        return max(x)

df['xp_reel'] = df['xp_reel'].apply(formatage)    

for i in range(len(df)):
    if (np.isnan(df["xp_reel"][i])) & (type(df["xp"][i]) == int):
        df.loc[i,'xp_reel'] = df.loc[i,'xp']
        
for i in range(len(df)):
    if (df["type_reel"][i].lower() in ["stage","apprentissage "] ) & (np.isnan(df['xp_reel'][i])):
        df.loc[i,'xp_reel']= 0


for i in range(len(df)):
    if df.loc[i,'xp_reel'] >= 7 : 
        df.loc[i,'xp_reel'] = 7
      
dat = df['xp_reel'].value_counts(normalize=True).mul(100).sort_index()
ax = dat.plot(kind='line', title= "Expérience réele demandée", )
ax.set_ylabel('Pourcentage')
ax.set_xlabel('Années')

#le remplissage à la main :'( 

df.loc[7, 'xp_reel'] = 0
df.loc[19, 'xp_reel'] = 1
df.loc[23, 'xp_reel'] = 3
df.loc[38, 'xp_reel'] = 2
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3
df.loc[23, 'xp_reel'] = 3

df_compte = df.xp_reel.value_counts().sort_index()
a = pd.Series([df.xp_reel.isna().sum()])
df_compte = df_compte.append(a)
df_compte.index = ["0","1","2","3","4","5","6","7 et +", "Non Spécifié"]

df_compte.plot(kind="pie")

df_none = df.loc[df['xp_reel'].isna()].drop(labels =["salaire","site", "entreprise"], axis = 1)
