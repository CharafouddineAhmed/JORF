#!/bin/python
# coding: utf-8
import xmltodict
from bs4 import BeautifulSoup
import json

# Conversion XML to JSON 
FILE_NAME=r'C:\\Users\\CS5764\\Desktop\\20190721-002411\\jorf\\global\\article\\JORF\\ARTI\\00\\00\\38\\79\\29\\JORFARTI000038792912.xml'
with open(FILE_NAME, 'r', encoding='utf8') as f:
    # Ouverture du fichier en mode lecture
    xmlstring = f.read()
jsonstring = json.dumps(xmltodict.parse(xmlstring, encoding='utf-8'), indent=4)

# Extraction du contenu avec les balises HTML
# Update  du fichier JSON.

with open('C:\\Users\\CS5764\\Desktop\\20190721-002411\\jorf\\global\\article\\JORF\\ARTI\\00\\00\\38\\79\\29\\JORFARTI000038792912.xml', 'r') as fichier : 
    soup = BeautifulSoup(fichier.read(), "lxml-xml")
id = str(soup.find('ID')).replace('<ID>', '').replace('</ID>', '')
id_eli = str(soup.find('ID_ELI')).replace('<ID_ELI>', '').replace('</ID_ELI>', '')
id_eli_alias = str(soup.find('ID_ELI_ALIAS')).replace('<ID_ELI_ALIAS>', '').replace('</ID_ELI_ALIAS>', '')
ancien_id = str(soup.find('ANCIEN_ID')).replace('<ANCIEN_ID>', '').replace('</ANCIEN_ID>', '')
origine = str(soup.find('ORIGINE')).replace('<ORIGINE>', '').replace('</ORIGINE>', '')
url = str(soup.find('URL')).replace('<URL>', '').replace('</URL>', '')
nature = str(soup.find('NATURE')).replace('<NATURE>', '').replace('</NATURE>', '')
num = str(soup.find('NUM')).replace('<NUM>', '').replace('</NUM>', '')
type = str(soup.find('TYPE')).replace('<TYPE>', '').replace('</TYPE>', '')
contexte = str(soup.find('CONTEXTE')).replace('<CONTEXTE>', '').replace('</CONTEXTE>', '').replace('\n', '')
versions = str(soup.find('VERSIONS')).replace('<VERSIONS>', '').replace('</VERSIONS>', '').replace('\n', '')
contenu = str(soup.find('BLOC_TEXTUEL')).replace('<BLOC_TEXTUEL>', '').replace('</BLOC_TEXTUEL>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')

modele_article = {
    'ID': id,
    'ID_ELI': id_eli,
    'ID_ELI_ALIAS': id_eli_alias,
    'ANCIEN_ID': ancien_id,
    'ORIGINE': origine,
    'URL': url,
    'NATURE': nature,
    'NUM': num,
    'TYPE': type,
    'CONTEXTE': contexte,
    'VERSIONS': versions,
    'CONTENU': contenu
}

with open(f'{id}.json', 'w') as json_file:
    json.dump(modele_article, json_file, indent=4)

jsonFile = open(f'{id}.json', "r+")
data = json.load(jsonFile)


tmp = data["CONTENU"]
data["CONTENU"] = "NewPath"

jsonFile.write(json.dumps(data, indent=4))