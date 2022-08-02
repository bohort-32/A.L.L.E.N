import sys
import os

# Import du dossier des Modules

# Imports Modules
from ModulesCoeur.Secret import *
from ModulesCoeur.Vocal import *
from ModulesCoeur.Comprendre import *
from ModulesCoeur.Initialisation import *
from ModulesCoeur.Demarrage import *
from ModulesCoeur.Logger import *
#from ModulesCoeur.WebSocket import *

# Imports Classes
from ClassesCoeur.UserInterface import *

# Constantes
FIN = False





Retours_demarrage = demarrerScript()
USERInterface = Retours_demarrage['USERInterface']
User = Retours_demarrage['Utilisateur']
LISTE_MODULES_EXT = Retours_demarrage['LISTE_MODULES_EXT']


get_logger(User).info("START LOGGER")

Debut = f'Bonjour {User.nom}'
Au_revoir = 'Au revoir'



# Début du script
if __name__ == '__main__':
    print("=== DEBUT DU SCRIPT ===")
    API_KEY = get_API_KEY_WOLFRAMALPHA()


    # Informe utilisateur allumage A.L.L.E.N
    USERInterface.informer_utilisateur(Debut)

    User.set_websock(True)

    if User.websock:
        print('test')
    else:
        print('pas sock')

    # Tant qu'on demande pas le fin
    while FIN == False:
        # Demande utilisateur
        retour = comprendre(USERInterface.demande_utilisateur('Que puis-je pour vous ?'), API_KEY, USERInterface, LISTE_MODULES_EXT, User)

        FIN = retour['FIN']

        if FIN == True :
            # Eteindre A.L.L.E.N
            USERInterface.informer_utilisateur(Au_revoir)
        else:
            # Réponse à l'utilisateur
            USERInterface.informer_utilisateur(retour['Reponse'])  