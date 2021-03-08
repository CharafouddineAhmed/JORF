#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Extrait Section .
def task_section(FILE_NAME):

    """"Cette fonction permets à partir du fichier XML en parametre de le convertir en JSON puis de l'indexer à la base DB.
    #### Fonction reservée uniquement au fichier TEXTE
    @Param : FILE_NAME - le nom du fichier
    """

    import xmltodict, json, os
    from collections import OrderedDict
    from datetime import datetime

    # STEP 1 : Conversion XML to JSON
    with open(FILE_NAME,  mode="r", encoding="utf8" ) as f:
        doc = xmltodict.parse(f.read(), encoding="utf-8" )

    datastore = json.loads(json.dumps(dict(OrderedDict(doc)), ensure_ascii=False))

     # Creation du fichier final
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y%d%m%H%M%S")

    with open(f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\section\\{date_time}.json', mode="w+", encoding="utf-8") as fichier:
        json.dump(datastore,fichier, indent=4, ensure_ascii=False)

    fichier.close()
    f.close()
    return f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\section\\{date_time}.json'