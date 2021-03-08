#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json

def flatten_json(y):
    import os, json
    """Ce programme permet de rendre les fichiers json plat .
    @param : data json
    @return : data json en sortie """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def is_integer(value: str, *, base: int=10) -> bool:
    try:
        int(value, base=base)
        return True
    except ValueError:
        return False

if __name__ == "__main__":

    import json
    
    temporaire = {}

    # STEP 1 : flatting du fichier
    path = "C:\\Users\\CS5764\\Desktop\\codeNapoleon\\func\\exemple.json"
    with open(str(path), mode="r", encoding='utf-8') as jsonFile:
        DATA  = json.load(jsonFile)
        date = flatten_json(DATA)
        with open('tmp', mode="w", encoding='utf-8') as f:
            json.dump(date, f, indent=4, ensure_ascii=False )

    # STEP 2 :
    with open('tmp', mode="r", encoding='utf-8' ) as f:
        d = json.load(f)
        for cle,valeur in d.items():
            tableau_cle = str(cle).split(".")

            # Test si ans le tableau il y'a un entier
            # en string
            for v in tableau_cle:
                if is_integer(v):
                    print(f'{v} : {tableau_cle.index(v)}')
                    # Dupliquer le fichier.
                    # temporaire = { number : v }