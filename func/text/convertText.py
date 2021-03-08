#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Extrait article.
def task_texte_version(FILE_NAME):
    import xmltodict, json, os
    from bs4 import BeautifulSoup
    from collections import OrderedDict
    from datetime import datetime
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

    # Creation du fichier final
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y%d%m%H%M%S")

    with open(f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\texte_version\\{date_time}.json', mode="w+", encoding="utf-8") as fichier:
        json.dump(datastore,fichier, indent=4, ensure_ascii=False)

    fichier.close()
    f.close()
    return f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\texte_version\\{date_time}.json'