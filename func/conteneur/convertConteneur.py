#!/usr/bin/env python
# -*- coding: utf-8 -*-

def task_conteneur(FILE_NAME):
    """"
    Cette fonction permets à partir du fichier XML en parametre de le convertir en JSON puis de l'indexer à la base DB.
    #### Fonction reservée uniquement au fichier TEXTE
    @Param : FILE_NAME - le nom du fichier
    """
    import xmltodict, json, os
    from collections import OrderedDict
    from ..autres.dissociate import dissocite as dissocite

    # STEP 1 : Conversion XML to JSON
    with open(FILE_NAME, encoding='utf-8' ) as f:
        doc = xmltodict.parse(f.read(), encoding='utf-8' )

    datastore = json.loads(json.dumps(dict(OrderedDict(doc)), ensure_ascii=False))

    # STEP 2 : flatting + dissociate
    val = dissocite(datastore)

    f.close()

    # STEP 4 : remove null in file
    # os.system(f'sed -i -e \'s/2/0/g\' C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\conteneur\\{date_time}.json ') 
    return val