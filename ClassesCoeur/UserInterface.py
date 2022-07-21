from tkinter.messagebox import NO
from ModulesCoeur.Vocal import *
from ClassesCoeur.Utilisateur import *

# Gère les interfaces utilisateur


class UserInterface:
    """
    Une classe pour gérer l'interface avec l'utilisateur (audio ou cmd)

    Attributes
    ----------
    entree_vocal : bool, optional
        Indique si l'entrée se fait par l'oral
    sortie_vocal : bool, optional
        Indique si la sortie se fait par l'oral
    user : Utilisateur, optional
        L'utilisateur courant

    Methods
    -------
    integrer(self, USERInterface, User)
        Lance le module de compréhension.
    """

    def __init__(self, entree_vocal=False, sortie_vocal=False, user=None):
        """
        Parameters
        ----------
        entree_vocal : bool, optional
            Indique si l'entrée se fait par l'oral
        sortie_vocal : bool, optional
            Indique si la sortie se fait par l'oral
        user : Utilisateur, optional
            L'utilisateur courant
        """
        self.entree_vocal = entree_vocal
        self.sortie_vocal = sortie_vocal
        self.user = user

    def set_entree_vocal(self, on_off):
        """Change le paramètre de l'entrée

        Parameters
        ----------
        on_off : bool
            Indique si l'entrée se fait par l'oral
        """
        self.entree_vocal = on_off
        if self.user != None:
            self.user.set_entree_vocal(on_off)

    def set_sortie_vocal(self, on_off):
        """Change le paramètre de sortie

        Parameters
        ----------
        on_off : bool
            Indique si la sortie se fait par l'oral
        """
        self.sortie_vocal = on_off
        if self.user != None:
            self.user.set_sortie_vocal(on_off)

    # Informe l'utilisateur d'un message
    def informer_utilisateur(self, message):
        """Informe l'utilisateur d'un message.

        Parameters
        ----------
        message : str
            Le message à indiquer.
        """
        # Cas : Par voix
        if self.sortie_vocal:
            parler(message)
        # Cas : Par texte
        else:
            print(message)

    # Demande à l'utilisateur une information
    def demande_utilisateur(self, demande):
        """Informe l'utilisateur d'une demande et retour son retour

        Parameters
        ----------
        demande : str
            La demander à demander.

        Returns
        -------
        retour
            Un texte de son retour.
        """
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
