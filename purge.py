#!/usr/bin/python
# coding: utf-8
import os, sys
if __name__ == "__main__":
    import os
    DIR_PATH = "C:\\Users\\CS5764\\Downloads\\legi\\global"

    for root, dirs, files in os.walk(DIR_PATH):
        try:
            for file in files:
                if file.endswith(".xml"):
                    xml_file = os.path.join(root, file)
                    if os.path.exists(f'{xml_file}'):
                        os.remove(f'{xml_file}')
                        print(f'{xml_file}')
                        print("Supprimé ! ")

        except Exception as identifier:
            print(identifier)
            pass