import sys
import os
from Modules.Secret import get_API_KEY_WOLFRAMALPHA
# Import du dossier des Modules
sys.path.insert(1, 'Modules')

# Imports
from Secret import *
from Vocal import *
from Comprendre import *
from Interface_Utilisateur import *


USERInterface = UserInterface()

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

    # Informe utilisateur allumag A.L.L.E.N
    USERInterface.informer_utilisateur(Debut)

    # Tant qu'on demande pas le fin
    while FIN == False:
        # Demande utilisateur
        retour = comprendre(USERInterface.demande_utilisateur('Que puis-je pour vous ?'), API_KEY, USERInterface)

        FIN = retour['FIN']

        if FIN == True :
            # Eteindre A.L.L.E.N
            USERInterface.informer_utilisateur(Au_revoir)
        else:
            # Réponse à l'utilisateur
            USERInterface.informer_utilisateur(retour['Reponse'])