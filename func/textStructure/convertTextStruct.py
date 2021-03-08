#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Extrait Texte structure .
def task_texte_struct(FILE_NAME):
    import xmltodict, json, os
    from collections import OrderedDict
    """"
    Cette fonction permets à partir du fichier XML en parametre de le convertir en JSON puis de l'indexer à la base DB.
    #### Fonction reservée uniquement au fichier TEXTE
    @Param : FILE_NAME - le nom du fichier
    """

    # STEP 1 : Conversion XML to JSON
    with open(FILE_NAME, encoding='utf-8' ) as f:
        doc = xmltodict.parse(f.read(), encoding='utf-8' )

    datastore = json.loads(json.dumps(dict(OrderedDict(doc)), ensure_ascii=False))

    # Creation du fichier final
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y%d%m%H%M%S")

    with open(f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\texte_structure\\{date_time}.json', mode="w+", encoding="utf-8") as fichier:
        json.dump(datastore,fichier, indent=4, ensure_ascii=False)

    fichier.close()
    f.close()
    return f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\texte_structure\\{date_time}.json'