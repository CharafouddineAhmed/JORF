#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Permet de convertir un fichier XML en JSON.
@Param: File_nom: nom du fichier en xml.
@retour: creation du fichier id.json
"""
    
import xmltodict, json, os, logging
from datetime import datetime
from bs4 import BeautifulSoup 

# Package management 

FILE_NAME = "/Users/ahmedcharafouddine/Documents/projets/PROJET_JORF/assets"


logging.basicConfig(filename='./logs/activity.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('[OK] Lancement du programme')
logging.info(f'[OK] Nom du fichier xml : /Users/ahmedcharafouddine/Documents/projets/PROJET_JORF/assets ')

try:
    # Récuperation de l'ID et le CONTENU de l'article
    # Statut : Bonne encoding
    with open(FILE_NAME, encoding="utf-8") as fichier:
        soup = BeautifulSoup(fichier, "lxml-xml" )

        id = str(soup.find('ID')).replace('<ID>', '').replace('</ID>', '')
        contenu = str(soup.find('BLOC_TEXTUEL')).replace('<BLOC_TEXTUEL>', '').replace('</BLOC_TEXTUEL>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        logging.info(f'[Ok] Recuperation de ID et le CONTENU')
except Exception as e:
    # print(f'Message d\'erreur : {e}')
    logging.warning(f'Message d\'erreur : {e}')
    pass

# Conversion XML to JSON
with open(FILE_NAME, encoding="utf-8", mode="r") as f :
    contenu_json = xmltodict.parse(f.read())

# Conversion
with open(f'tmp_{id}.json', mode='w+', encoding="utf8" ) as fi:
    json.dump(contenu_json, fi, indent=4, ensure_ascii=False)

# UPdate du fichier json crée
with open(f'tmp_{id}.json', mode="r", encoding="utf8" ) as jsonFile:
    data = json.load(jsonFile)

data["ARTICLE"]['BLOC_TEXTUEL']['CONTENU'] = contenu

try:
    # Creation du fichier json final dans ./resultat/articles
    with open(f'outputs/articles/{id}.json', mode="w+", encoding="utf-8") as jsonFile:
        json.dump(data, jsonFile, indent=4, ensure_ascii=False)
        logging.info(f'[OK] Creation du fichier resultat : C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\articles\\{id}.json ')
except Exception as e:
    logging.warning(f'[KO] Erreur lors de la creation du fichier resultat | {e} ')
    pass

# Suppression du/des fichier(s) temporaire
try:
    os.system(f'rm -rf tmp_{id}.json')
    logging.info(f'[OK] Suppression du fichier temporaire tmp_{id}.json ')
except Exception as err :
    logging.warning(f'[KO] Erreur lors de la suppression du fichier temporaire tmp_{id}.json | {err} ')
    pass

# Fermeture des fichiers
f.close()
fichier.close()

# date
now = datetime.now() # current date and time
date_time = now.strftime("%Y%d%m%H%M%S")

logging.info(f'[OK] Fin du programme')
# return f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\articles\\{id}.json'


