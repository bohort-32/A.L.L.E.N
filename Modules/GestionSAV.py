import json

def sauvegarder(fichier, donnee_json):
    with open(fichier, 'w') as outfile:
        json.dump(donnee_json, outfile)