#!/usr/bin/python
# coding: utf-8
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
