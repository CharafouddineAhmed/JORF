# Auteur      : Ahmed CHARAFOUDDINE (ahmed.charafouddine@gmail.com)
# Version     : 0.1
# Description :
# """
# """

#!/usr/bin/python
# coding: utf-8
import os, logging
from func.text.convertText import task_texte_version
from func.textStructure.convertTextStruct import task_texte_struct
from func.conteneur.convertConteneur import task_conteneur
from func.section.convertSection import task_section
from func.autres.indexationES import indexationES as task_indexation
from func.autres.removeNull import removeNull
from func.autres.classification import classification_file

if __name__ == "__main__":

    """ Recherche des fichiers XML par categorie [artcile,conteneur, eli, section_ta, text, etc ] """

    # Declaration des variables
    ARTICLE_LISTE = []
    CONTENEUR_LISTE = []
    TEXTE_VERSION_LISTE = []
    TEXTE_STRUCTURE_LISTE = []
    SECTION = []

    # Entrée. 
    # DIR_PATH ='C:\\Users\\CS5764\\Desktop\\codeNapoleon\\assets\\jorf'
    DIR_PATH ='/Users/ahmedcharafouddine/Documents/projets/PROJET_JORF/assets'


    ARTICLE_LISTE, CONTENEUR_LISTE, TEXTE_VERSION_LISTE, TEXTE_STRUCTURE_LISTE, SECTION = classification_file(DIR_PATH)

    for xml_file_name in ARTICLE_LISTE:

        print(xml_file_name)
        # file = task_article(xml_file_name)
        # os.system(f"sed -i -e 's/null/0/g' {file}")
        #task_indexation(file)
        # if os.path.exists(f'{file}'):
        #     os.remove(f'{file}')
    #output =[]
    #for xml_file_name in CONTENEUR_LISTE:
    #    output = task_conteneur(xml_file_name)

    #for valeur in output:
    #    task_indexation(valeur)


# logging.basicConfig(filename='./logs/activity_global.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.info(' Starting program ')
# logging.info(' program finished')

# Concerne les fichiers ARTICLE xml
                        # on converti + indexation
                        # file = task_article(xml_file_name)
                        # os.system(f"sed -i -e 's/null/0/g' {file}")
                        # task_indexation(file)
                        # if os.path.exists(f'{file}'):
                        #     os.remove(f'{file}')


                         #if "conteneur" in xml_file_name:
                    #    try:
                    #        task_conteneur(xml_file_name)
                    #    except Exception as identifier:
                    #        print(identifier)
                    #        pass
                    #    # try:
                    #    #     date = task_conteneur(xml_file_name)
                    #    #     removeNull(date)
                    #    #     # task_indexation(date)
                    #    #     # if os.path.exists(f'{data}'):
                    #    #     #     os.remove(f'{data}')
                    #    # except Exception as identifier:
                    #    #     pass

                    #if "TEXT" in xml_file_name and "version" in xml_file_name:
                    #    # Concerne les fichiers TEXT
                    #    try:
                    #        f = task_texte_version(xml_file_name)
                    #        # task_indexation(f)
                    #        # if os.path.exists(f'{f}'):
                    #        #     os.remove(f'{f}')
                    #    except Exception as error :
                    #        pass

                    #elif "TEXT" in xml_file_name and "struct" in xml_file_name:
                    #    # Concerne les fichier TEXT struct
                    #    try:
                    #        fi = task_texte_struct(xml_file_name)
                    #        task_indexation(fi)
                    #        if os.path.exists(f'{fi}'):
                    #            os.remove(f'{fi}')
                    #    except Exception as identifier:
                    #        print(f'Erreur : {identifier}')

                    #elif "section" in xml_file_name:
                    #    try:
                    #        a = task_section(xml_file_name)
                    #        task_indexation(a)
                    #        if os.path.exists(f'{a}'):
                    #            os.remove(f'{a}')
                    #    except Exception as identifier:
                    #        print(f'Erreur {identifier}')
                    #        pass