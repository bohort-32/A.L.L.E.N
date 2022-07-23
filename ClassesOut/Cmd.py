import os

from ClassesCoeur.UserInterface import *
from ClassesCoeur.Utilisateur import *
from ModulesCoeur.Comprendre import *

# class inside the module
class Cmd:
    def Comprendre(USERInterface, User, requete):
        # Liste des mots clefs système
        LISTE_SYS = ['CMD', 'cmd', 'Cmd']
        # Indique si la requete est présente
        if rechercher_mot(requete, LISTE_SYS):
            # Formulation de la commande
            requete = requete.split(' ')
            if len(requete) > 1:
                commande = ''
                for cmd_arg in requete:
                    if cmd_arg != requete[0]:  
                        commande += ' '+cmd_arg
                # Execution de la commande
                res = os.system(commande)
                # Commande avec succès
                if res == 0:
                    USERInterface.informer_utilisateur('Commande exécutée')
                # Erreur arrivée
                else :
                    USERInterface.informer_utilisateur('Erreur commande')
            # Pas de commande donnée
            else:
                USERInterface.informer_utilisateur('Pas de commande donnée')