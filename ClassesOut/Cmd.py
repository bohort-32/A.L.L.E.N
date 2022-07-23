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
                cmd = requete[1]
                print('Demande CMD')
            else:
                print('pas de cmd')