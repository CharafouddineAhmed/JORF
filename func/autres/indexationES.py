#!/usr/bin/env python
# -*- coding: utf-8 -*-

def indexationES(FILE_NAME):
    """
    Indexation des documents dans la base elasticsearch.
    @Param : le nom du fichier json.
    """
    # indexation dans la base
    from datetime import datetime
    import json, os, time
    from elasticsearch import Elasticsearch
    # es = Elasticsearch(sniff_on_start=True)
    es = Elasticsearch()

    # VARIBALE
    INDEX_NAME = "jorf-v2"
    TYPE_DOCUMENT = "_doc"

    with open(str(FILE_NAME), mode="r", encoding="utf8" ) as jsonFile:
        DATA  = json.load(jsonFile)
        try:
            # Action 1
            # Test de vie (ES)

            # Action 2
            # Requete d'indexation
            resultat = es.index(
                index=INDEX_NAME,
                doc_type=TYPE_DOCUMENT,
                body= DATA
                )
            # Show the response
            print(json.dumps(resultat, indent=4))

            # Action 3
            # Refresh index ES + Show the response
            res = es.indices.refresh(index=INDEX_NAME)
            print(json.dumps(res, indent=4))

            # time.sleep(1)
            # os.system(f'rm -rf ')

        except Exception as exception:
            print(f'Erreur rencontré : {exception} ')