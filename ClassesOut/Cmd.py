import os

from ClassesCoeur.UserInterface import *
from ClassesCoeur.Utilisateur import *
from ModulesCoeur.Comprendre import *

# class inside the module
class Cmd:
    def Comprendre(USERInterface, User, requete):
        LISTE_SYS = ['CMD', 'cmd', 'Cmd']
        if rechercher_mot(requete, LISTE_SYS):
            requete = requete.split(' ')
            if len(requete) > 1:
                commande = ''
                for cmd_arg in requete:
                    if cmd_arg != requete[0]:  
                        commande += ' '+cmd_arg
                res = os.system(commande)

                if res == 0:
                    USERInterface.informer_utilisateur('Commande exécutée')
                else :
                    USERInterface.informer_utilisateur('Commande inconnue')
            else:
                USERInterface.informer_utilisateur('Pas de commande donnée')