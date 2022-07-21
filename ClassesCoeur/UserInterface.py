from tkinter.messagebox import NO
from ModulesCoeur.Vocal import *
from ClassesCoeur.Utilisateur import *

# Gère les interfaces utilisateur
class UserInterface :
    def __init__(self, entree_vocal=False, sortie_vocal=False, user=None):
        self.entree_vocal = entree_vocal
        self.sortie_vocal = sortie_vocal
        self.user = user


    def set_entree_vocal(self, on_off):
        self.entree_vocal = on_off
        if self.user != None:
            self.user.set_entree_vocal(on_off)


    def set_sortie_vocal(self, on_off):
        self.sortie_vocal = on_off
        if self.user != None:
            self.user.set_sortie_vocal(on_off)

    # Informe l'utilisateur d'un message
    def informer_utilisateur(self, message):
        # Cas : Par voix
        if self.sortie_vocal:
            parler(message)
        # Cas : Par texte
        else:
            print(message)

    # Demande à l'utilisateur une information
    def demande_utilisateur(self, demande):
        retour = None
        # Informe l'utilisateur de la demande
        self.informer_utilisateur(demande)
        # Saisie par vocal
        if self.entree_vocal:
            retour = ecouter()
        # Saisie oral
        else:
            retour = input('Saisie : ')

        # Retour de l'utilisateur
        return retour