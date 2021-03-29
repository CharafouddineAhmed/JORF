#!/usr/bin/python
# coding: utf-8

""" Recherche des fichiers XML par categorie [artcile,conteneur, eli, section_ta, text, etc ] 
Output : fichiers crées dans le repertoire /tmp """

import os, logging
from func.autres.classification import classification_file

DIR_PATH ='/Users/ahmedcharafouddine/Documents/projets/PROJET_JORF/assets'
LOG_PATH = './logs/activity.log'

logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='[%(asctime)s][%(levelname)s][%(name)s][%(message)s]')
logging.info('appel de la fonction classification ')

classification_file(DIR_PATH, LOG_PATH )


print("done!")