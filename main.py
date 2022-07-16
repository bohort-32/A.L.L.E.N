import sys
import os
from Modules.Secret import get_API_KEY_WOLFRAMALPHA
# Import du dossier des Modules
sys.path.insert(1, 'Modules')

# Imports
from Secrets import *
from Vocal import *
from Comprendre import *



# Constantes
ENTREE_VOCAL = False
SORTIE_VOCAL = False
FIN = False

USER_NAME = os.environ.get( "USERNAME" )
Debut = f'Bonjour {USER_NAME}'
Au_revoir = 'Au revoir'


# Début du script
if __name__ == '__main__':
    print("=== DEBUT DU SCRIPT ===")
    API_KEY = get_API_KEY_WOLFRAMALPHA()

    # Tant qu'on demande pas le fin

    # Sortie vocale
    if SORTIE_VOCAL == True:
        parler(Debut)

    # Sortie clavier
    else:
        print(Debut)

    while FIN == False:

        # Entrée vocale
        if ENTREE_VOCAL == True:
            # Ecoute
            retour = comprendre(ecouter(), ENTREE_VOCAL, SORTIE_VOCAL, FIN, API_KEY)
        # Entrée clavier
        else:
            # Input
            retour = comprendre(input("Demande : "), ENTREE_VOCAL, SORTIE_VOCAL, FIN, API_KEY)


        ENTREE_VOCAL = retour['ENTREE_VOCAL']
        SORTIE_VOCAL = retour['SORTIE_VOCAL']
        FIN = retour['FIN']

        if FIN == True :
            # Entrée vocale
            if SORTIE_VOCAL == True:
                parler(Au_revoir)

            # Entrée clavier
            else:
                print(Au_revoir)

        else:
            # Sortie vocale
            if SORTIE_VOCAL == True:
                parler(retour['Reponse'])

            # Sortie clavier
            else:
                print(retour['Reponse'])