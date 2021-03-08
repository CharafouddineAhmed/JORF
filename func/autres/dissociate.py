import json

def flatten_helper(prefix, list_of_dict):
    res = []
    for i in list_of_dict:
        res_dict={}
        for k, v in i.items():
            res_dict['.'.join([prefix,k])]=v
        res.append(res_dict)
    return res

def flatten(x):
   
    if isinstance(x, list):
        res = []
        for ele in x:
            res = res + flatten(ele)
        return res
    else:
        res = [{}]
        for k, v in x.items():
            if (isinstance(v, dict) or isinstance(v,list)):
                new_res = []
                tempo = flatten(v)
                for r in res:
                    for t in tempo:
                        new_res.append({**r, **t})
                res = flatten_helper(k,new_res)
            else:
                for i, val in enumerate(res):
                    res[i][k]=v
        return res

def dissocite(data_json):
    """ Cette fonction de generer des sous-fichiers tant que le fichier json contient des tableaux.
    @Param : le data json
    @Return : List  creation des outputs.json """

    from datetime import datetime
    import os
    from ..autres.removeNull import removeNull as removeNull

    # date
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y%d%m%H%M%S")

    output_list = []

    res = flatten(data_json)
    for val in res:
        with open(f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\conteneur\\data_{res.index(val)}_{date_time}.json', 'w', encoding='utf-8' ) as tmp_f:
            json.dump(val, tmp_f, indent=4, ensure_ascii=False)
            #r = removeNull(f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\conteneur\\data_{res.index(val)}_{date_time}.json')
        tmp_f.close()
        os.system(f"sed -i -e 's/null/0/g' C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\conteneur\\data_{res.index(val)}_{date_time}.json")
        output_list.append(f'C:\\Users\\CS5764\\Desktop\\codeNapoleon\\Resultats\\conteneur\\data_{res.index(val)}_{date_time}.json')
    
    return output_list