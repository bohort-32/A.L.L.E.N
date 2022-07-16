from Modules.Vocal import *

# Gère les interfaces utilisateur
class UserInterface :
    def __init__(self, entree_vocal=False, sortie_vocal=False):
        self.entree_vocal = entree_vocal
        self.sortie_vocal = sortie_vocal


    def set_entree_vocal(self, on_off):
        self.entree_vocal = on_off


    def set_sortie_vocal(self, on_off):
        self.sortie_vocal = on_off


    def eteindre_vocal(self):
        self.set_entree_vocal(False)
        self.set_sortie_vocal(False)


    def allumer_vocal(self):
        self.set_entree_vocal(True)
        self.set_sortie_vocal(True)


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

    def toString(self):
        print(f'Voix : {self.sortie_vocal} | Entrée : {self.entree_vocal}')