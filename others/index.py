#!/bin/python3

import os, json, xmltodict

FILE_NAME=r'C:\\Users\\CS5764\\Desktop\\20190721-002411\\jorf\\global\\conteneur\\JORF\\CONT\\00\\00\\38\\79\\28\\JORFCONT000038792882.xml'
with open(FILE_NAME, 'r', encoding='utf8') as f:
    # Ouverture du fichier en mode lecture
    xmlstring = f.read()
jsonstring = json.dumps(xmltodict.parse(xmlstring, encoding='utf-8'), indent=4)

# indexation dans la base
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
try:
    res = es.index(index="jorf", doc_type='_doc', body=json.loads(jsonstring))
    print(res['result'])
except Exception as exception:
    print(f'Erreur rencontré : {exception} ')
    pass

# Output
fichier = open("output.json", "a")
fichier.write(jsonstring)
fichier.close()