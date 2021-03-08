#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json
# from .flatten_json import flatten_json

f = open("exemple.json")
data = json.load(f)

output = []

def recursive(d):
    # if str( type(d)) not in  "<class 'dict'>" and str( type(d)) not in "<class # 'list'>" :
    #     output.append(d)

    if str( type(d)) in "<class 'dict'>":
        for i in d:
            recursive(d[i])
    elif str(type(d)) in "<class 'list'>":
        for valeur in d:
            # Create len(d) json file
            with open(f'data_{d.index(valeur)}.json', 'w') as tmp_f:
                json.dump(valeur, tmp_f)
                # json.dump(output, tmp_f)
            tmp_f.close()


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

# recursive(data)

# Read json file
FILE_NAME = "exemple.json"
with open(str(FILE_NAME), mode="r", encoding='utf-8') as jsonFile:
    DATA  = json.load(jsonFile)
    # print(json.dumps(DATA['SECTION_TA'], indent=4, ensure_ascii=False))

    for cle,valeur in DATA['SECTION_TA'].items():
        print(type(valeur))
        if str(type(valeur)) in "<class 'dict'>":
            data_flatted = flatten_json(DATA['SECTION_TA'][cle] )
            with open('tmp.json', mode="w", encoding="utf-8") as f:
                json.dump(data_flatted, f , indent=4, ensure_ascii=False)
                break
            # print( DATA['SECTION_TA'][cle] )

# print(json.dumps(output, indent=4, ensure_ascii=False))
f.close()