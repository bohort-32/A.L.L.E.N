import sys
import os
# Import du dossier des Modules

# Imports Modules
from Modules.Secret import *
from Modules.Vocal import *
from Modules.Comprendre import *
from Modules.Initialisation import *
from Modules.Demarrage import *
# Imports Classes
from Classes.UserInterface import *

# Constantes
FIN = False



demarrerScript()




""""

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
"""