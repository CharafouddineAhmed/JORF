#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Extrait article.
def task_article(FILE_NAME): 
    """"
    Cette fonction permets à partir du fichier XML en parametre de le convertir en JSON puis de l'indexer à la base DB.
    #### Fonction reservée uniquement au fichier ARTICLE
    @Param : FILE_NAME - le nom du fichier
    """

    #  STEP 1 : Récuperation de l'ID et le contenu de l'article
    with open(FILE_NAME, encoding='utf-8') as fichier:
        soup = BeautifulSoup(fichier, "lxml-xml" )

        id = str(soup.find('ID')).replace('<ID>', '').replace('</ID>', '')
        contenu = str(soup.find('BLOC_TEXTUEL')).replace('<BLOC_TEXTUEL>', '').replace('</BLOC_TEXTUEL>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')


    # STEP 2 : Conversion XML to JSON
    with open(FILE_NAME, encoding='utf-8' ) as f:
        doc = xmltodict.parse(f.read(), encoding='utf-8' )

    datastore = json.loads(json.dumps(dict(OrderedDict(doc)), ensure_ascii=False))

    # STEP 3 : update la valeur du champs : contenu
    datastore["ARTICLE"]['BLOC_TEXTUEL']['CONTENU'] = contenu

    # STEP 4 : Ecriture dans un fichier JSON
    # with open(f'{id}.json', mode='w+', encoding='utf-8') as fichier_json:
    #     json.dump( datastore, fichier_json, indent=4, ensure_ascii=False)

    # STEP 4 bis : autre choix : indexation dans la base db
    from datetime import datetime
    from elasticsearch import Elasticsearch
    es = Elasticsearch()

    try:
        resultat = es.index(index="jorf", doc_type='_doc', body=datastore)
        print(json.dumps(resultat, indent=4))
    except Exception as exception:
        print(f'Erreur lors de l\'indexation \n Details : {exception}')
        pass

    # Fermeture des fichiers
    f.close()
    fichier.close()

# Extrait article.
def task_texte(FILE_NAME):
    
    """"
    Cette fonction permets à partir du fichier XML en parametre de le convertir en JSON puis de l'indexer à la base DB.
    #### Fonction reservée uniquement au fichier TEXTE
    @Param : FILE_NAME - le nom du fichier
    """

    #  STEP 1 : Récuperation de l'ID et le contenu.
    with open(FILE_NAME, encoding='utf-8') as fichier:
        soup = BeautifulSoup(fichier, "lxml-xml" )

        id = str(soup.find('ID')).replace('<ID>', '').replace('</ID>', '')
        VISAS = str(soup.find('VISAS')).replace('<VISAS>', '').replace('</VISAS>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        SIGNATAIRES = str(soup.find('SIGNATAIRES')).replace('<SIGNATAIRES>', '').replace('</SIGNATAIRES>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        NOTICE = str(soup.find('NOTICE')).replace('<NOTICE>', '').replace('</NOTICE>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        TP = str(soup.find('TP')).replace('<TP>', '').replace('</TP>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        ABRO = str(soup.find('ABRO')).replace('<ABRO>', '').replace('</ABRO>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        RECT = str(soup.find('RECT')).replace('<RECT>', '').replace('</RECT>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')
        SM = str(soup.find('SM')).replace('<SM>', '').replace('</SM>', '').replace('<CONTENU>', '').replace('</CONTENU>', '').replace('\n', '')

    # STEP 2 : Conversion XML to JSON
    with open(FILE_NAME, encoding='utf-8' ) as f:
        doc = xmltodict.parse(f.read(), encoding='utf-8' )

    datastore = json.loads(json.dumps(dict(OrderedDict(doc)), ensure_ascii=False))

    # STEP 3 : update la valeur du champs : contenu
    datastore["TEXTE_VERSION"]['VISAS']['CONTENU'] = VISAS
    datastore["TEXTE_VERSION"]['SIGNATAIRES']['CONTENU'] = SIGNATAIRES
    datastore["TEXTE_VERSION"]['NOTICE']['CONTENU'] = NOTICE
    datastore["TEXTE_VERSION"]['TP']['CONTENU'] = TP
    datastore["TEXTE_VERSION"]['ABRO']['CONTENU'] = ABRO
    datastore["TEXTE_VERSION"]['RECT']['CONTENU'] = RECT
    datastore["TEXTE_VERSION"]['SM']['CONTENU'] = SM

    print(json.dumps(datastore, indent=4))

    # print(id)
    # print(VISAS)
    # print(SIGNATAIRES)
    # print(NOTICE)
    # print(TP)
    # print(ABRO)
    # print(RECT)
    # print(SM)

    # STEP 4 bis : autre choix : indexation dans la base db
    #from datetime import datetime
    #from elasticsearch import Elasticsearch
    #es = Elasticsearch()
#
    #try:
    #    resultat = es.index(index="jorf-v2", doc_type='_doc', body=datastore)
    #    print(json.dumps(resultat, indent=4))
    #except Exception as exception:
    #    print(f'Erreur lors de l\'indexation \n Details : {exception}')
    #    pass

    # STEP 5 : Fermeture des fichiers
    f.close()
    fichier.close()

if __name__ == "__main__":

    import xmltodict, json, os
    from bs4 import BeautifulSoup
    from collections import OrderedDict
    #  PATH='C:\\Users\\CS5764\\Desktop\\20190721-002411\\jorf\\global\\article\\JORF\\ARTI'
    #  for root, dirs, files in os.walk(PATH):
    #      try:
    #          for file in files:
    #              if file.endswith(".xml"):
    #                  # On a tout les fichiers
    #                  fichier = os.path.join(root, file)
    #                  task_article(str(fichier)) # Appel de la fonction task2 en lui attribuant le file name en xml
    #      except Exception as e:
    #          print(f'Erreur lors de la recherche des fichier.\nDetails: {e} ')
    #          pass


    PATH='C:\\Users\\CS5764\\Desktop\\20190721-002411\\jorf\\global\\texte\\version\\JORF\\TEXT'
    for root, dirs, files in os.walk(PATH):
        try:
            for file in files:
                if file.endswith(".xml"):
                    # On a tout les fichiers
                    fichier = os.path.join(root, file)
                    task_texte(str(fichier)) # Appel de la fonction task2 en lui attribuant le file name en xml
        except Exception as e:
            print(f'Erreur lors de la recherche des fichier.\nDetails: {e} ')
            pass
