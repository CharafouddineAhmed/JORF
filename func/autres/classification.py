#!/usr/bin/python
# coding: utf-8

def classification_file(dir_path):
    """ Permet de classer en different categories les differents fichiers.
    @param : le assert
    @ARTICLE_LISTE,CONTENEUR_LISTE,TEXTE_VERSION_LISTE, TEXTE_STRUCTURE_LISTE,SECTION  """

    import os
    # declaration des variables
    ARTICLE_LISTE = []
    CONTENEUR_LISTE = []
    TEXTE_VERSION_LISTE = []
    TEXTE_STRUCTURE_LISTE = []
    SECTION = []

    for root, dirs, files in os.walk(dir_path):
        try:
            for file in files:
                if file.endswith(".xml"):
                    # On a tout les fichiers
                    xml_file_name = os.path.join(root, file)

                    # Classification des noms des fichiers

                    if "ARTI" in xml_file_name:
                        ARTICLE_LISTE.append(xml_file_name)

                    elif "conteneur" in xml_file_name:
                        CONTENEUR_LISTE.append(xml_file_name)

                    elif "TEXT" in xml_file_name and "version" in xml_file_name:
                        TEXTE_VERSION_LISTE.append(xml_file_name)

                    elif "TEXT" in xml_file_name and "struct" in xml_file_name:
                        TEXTE_STRUCTURE_LISTE.append(xml_file_name)

                    elif "section" in xml_file_name:
                        SECTION.append(xml_file_name)

        except Exception as e:
            print(f'Erreur lors de la recherche des fichier')
            print(f'+ Details: {e}')
            print(f'+ Nom du fichier :{xml_file_name} ')
            pass
    return ARTICLE_LISTE,CONTENEUR_LISTE,TEXTE_VERSION_LISTE,TEXTE_STRUCTURE_LISTE,SECTION
