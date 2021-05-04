from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Users/Syl/chromedriver.exe')
driver.get("https://fr.linkedin.com/")


# Localiser la zone de texte
search_field_log = driver.find_element_by_id("session_key")
search_field_log.clear()

# Saisir et confirmer le login
search_field_log.send_keys("Rentrer son login ici")

time.sleep(0.5)

search_field_ps = driver.find_element_by_id("session_password")
search_field_ps.clear()

# Saisir et confirmer le pass
search_field_ps.send_keys("Rentrer son password ici")

# Valider
driver.find_element_by_class_name("sign-in-form__submit-button").click()

time.sleep(2.5)

links = []

# on itère sur les 500 premières offres
 
for i in range(0,500,25):
    url = "https://www.linkedin.com/jobs/search/?f_E=2&f_JT=F%2CC&f_TPR=r2592000&keywords=Data%20analyst&location=France&sortBy=DD&start="+str(i)
    driver.get(url)
    time.sleep(1.5)
    scrolls = 4
    while True:
        scrolls -= 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        if scrolls < 0:
            break
    liste = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "job-card-list__title", " " ))]')
    links.append([elem.get_attribute('href') for elem in liste])
    time.sleep(2.5)

liste_lien =[]
for indice, sub_list in enumerate(links):
    for sub_i, element in enumerate(sub_list):
        liste_lien.append(element[:46])
        

# on crée un df pour ranger tout ça

df_li = pd.DataFrame(columns =["intitule","entreprise","Type Contrat","Niveau Experience","texte"]) # on crée le df


for url in liste_lien : 
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    liste_buffer = [soup.find("h1").string] #on ajoute le titre
    liste_buffer.append(soup.find("span","topcard__flavor").string) #on ajoute l'enreprise
    liste_critere = []
    for i in soup.findAll("span", "job-criteria__text"):
        liste_critere.append(i.string)
    liste_buffer.append(liste_critere[1]) #on ajoute le type de contrat
    liste_buffer.append(liste_critere[0]) #on ajoute l'xp
    texte = []
    for i in soup.find("div", "show-more-less-html__markup").children :
        texte.append(i)
    liste_buffer.append("".join(str(texte)).replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("br />", "").replace("<br/>", u' ').replace('<u>', ' ').replace("</u>", ' ').replace(r"\\"," "))
    df_li.loc[len(df_li)] = liste_buffer
    time.sleep(1.5)

# on sauvegarde les données
    
df_li.to_csv("data_linkedin.csv")