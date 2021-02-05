# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:51:36 2021

@author: Syl
"""

import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re 
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
          'referer':'https://www.google.com/'}

liste_id = []


for i in range(0,500,50):
    r = requests.get("https://fr.indeed.com/emplois?q=Data+Analyst&limit=50&start="+str(i), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    scripts = soup.findAll("script")
    for i in range(len(scripts)):
        if "jobmap" in str(scripts[i]):
            jobmap_script = scripts[i]
    clean = str(jobmap_script)
    clean = re.sub(r"[-()\"#/@;<>{}`+~|.!?,]", " ", clean)
    position = [m.start() for m in re.finditer("jk:", clean)]
    for i in position :
        liste_id.append(clean[i+4:i+20])
    time.sleep(0.5)

len(liste_id)

df_in = pd.DataFrame(columns =["intitule","entreprise","Type Contrat","Niveau Experience","texte"]) # on crée le df
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:/Users/Syl/chromedriver.exe')
for i in liste_id:
    url = "https://fr.indeed.com/voir-emploi?&jk="+str(i)
    driver.get(url)
    time.sleep(1.5)
    try : 
        intitule = driver.find_element_by_tag_name('h1').text
        entreprise = driver.find_element_by_css_selector(".icl-u-xs-mr--xs")
        entreprise = entreprise.text
    except NoSuchElementException:
            entreprise = None
    try :
        texte = driver.find_element_by_id('jobDescriptionText').text
        Type = driver.find_element_by_class_name("jobsearch-JobMetadataHeader-item")
        Type = Type.text
        xp = None
    except NoSuchElementException:
        Type = None
    liste_buffer = [intitule, entreprise, Type, xp, texte]
    df_in.loc[len(df_in)] = liste_buffer
    time.sleep(2)
    
    
    
df_in.index = list(range(len(df_in)))


df_in.to_csv("data_indeed.csv")