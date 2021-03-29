#!/usr/bin/python
# coding: utf-8

def classification_file(dir_path, log_path):
    """ Permet de classer en different categories les differents fichiers. """
    import os
    import logging
    from datetime import datetime

    logging.basicConfig(filename=log_path, level=logging.INFO, format='[%(asctime)s][%(levelname)s][%(name)s][%(message)s]')
    logging.info('function classification was started .. ')

    count_article = 0
    count_conteneur = 0
    count_version = 0
    count_struct = 0
    count_section = 0

    for root, dirs, files in os.walk(dir_path):
        try:
            for file in files:
                if file.endswith(".xml"):
                    # On a tout les fichiers
                    xml_file_name = os.path.join(root, file)

                    if "ARTI" in xml_file_name: 
                        try: 
                            now = str(datetime.now().strftime("%m%d%Y"))
                            f = open(f"./tmp/tmp_liste_article_{now}.txt", "a")
                            f.write(xml_file_name + "\n")
                            count_article+=1
                            f.close()

                        except Exception as e: 
                            logging.info('Erreur sur l\'ecriture dans le fichier : {} '.format(str(e)) )
                            pass

                    elif "conteneur" in xml_file_name:

                        try: 
                            now = str(datetime.now().strftime("%m%d%Y"))
                            f = open(f"./tmp/tmp_liste_conteneur_{now}.txt", "a")
                            f.write(xml_file_name + "\n")
                            count_conteneur+=1
                            f.close()
                            
                        except Exception as e: 
                            logging.info('Erreur sur l\'ecriture dans le fichier : {} '.format(str(e)) )
                            pass


                    elif "TEXT" in xml_file_name and "version" in xml_file_name:

                        try: 
                            now = str(datetime.now().strftime("%m%d%Y"))
                            f = open(f"./tmp/tmp_liste_text_version_{now}.txt", "a")
                            f.write(xml_file_name + "\n")
                            count_version+=1
                            f.close()

                        except Exception as e: 
                            logging.info('Erreur sur l\'ecriture dans le fichier : {} '.format(str(e)) )
                            pass

                    elif "TEXT" in xml_file_name and "struct" in xml_file_name:

                        try: 
                            now = str(datetime.now().strftime("%m%d%Y"))
                            f = open(f"./tmp/tmp_liste_text_struct_{now}.txt", "a")
                            f.write(xml_file_name + "\n")
                            count_struct+=1
                            f.close()

                        except Exception as e: 
                            logging.info('Erreur sur l\'ecriture dans le fichier : {} '.format(str(e)) )
                            pass

                    elif "section" in xml_file_name:
                        try: 
                            now = str(datetime.now().strftime("%m%d%Y"))
                            f = open(f"./tmp/tmp_liste_section_{now}.txt", "a")
                            f.write(xml_file_name + "\n")
                            count_section+=1
                            f.close()

                        except Exception as e: 
                            logging.info('Erreur sur l\'ecriture dans le fichier : {} '.format(str(e)) )
                            pass
                        
        except Exception as e:
            logging.info('Erreur lors de la recherche des fichier')
            logging.info(f'+ Details: {e}')
            logging.info(f'+ Nom du fichier :{xml_file_name} ')
            pass
 
    logging.info(f'{count_article} xml files type article was found')
    logging.info(f'{count_conteneur} xml files type conteneur was found')
    logging.info(f'{count_section} xml files type section was found')
    logging.info(f'{count_struct} xml files type struct was found')
    logging.info(f'{count_version} xml files type version was found')
    logging.info('function has been terminated')