import os
from ModulesCoeur.Initialisation import *
from ClassesCoeur.UserInterface import *
from ModulesCoeur.Comprendre import *
from ModulesCoeur.Logger import *


def verifierInit(USER_NAME, USERInterface, chemin_DATA, chemin_user):
    """Vérifier si le dossier de l'utilisateur est présent.
    Les crées si besoin.

    Parameters
    ----------
    USER_NAME : str
        Le nom de l'utilisateur en local.
    USERInterface : UserInterface
        L'interface avec l'utilisateur.
    chemin_DATA : str
        Le chemin pour accéder au données du logiciel.
    chemin_user : str
        Le chemin pour accéder au données de l'utilisateur.

    """
    # == Vérification présence des dossier
    data_exist = os.path.exists(chemin_DATA)
    chemin_user_exist = os.path.exists(chemin_user)

    if not data_exist or not chemin_user_exist:
        initialiser_dossier(USER_NAME, USERInterface, chemin_DATA, chemin_user, data_exist, chemin_user_exist)
    


def demarrerScript():
    """Lance le démarrage de A.L.L.E.N

    Returns
    -------
    dict
        Contient l'utilisateur, son interface, la liste des modules extérieurs présents.
    """
    # == Initialisation des variables
    USER_NAME = os.environ.get( "USERNAME" )
    USERInterface = UserInterface()
    # Chemin des données utilisateurs
    chemin_DATA = f'./DATA'
    # Chemin des données de l'utilisateur courant
    chemin_user = f'{chemin_DATA}/{USER_NAME}'
    chemin_fic_user = f'{chemin_user}/utilisateur.json'
    # Vérifie qu'un utilisateur existe ou le crée
    verifierInit(USER_NAME, USERInterface, chemin_DATA, chemin_user)
    user = Utilisateur().charger_donnees_utilisateur(chemin_fic_user)
    USERInterface = UserInterface(user.entree_vocal, user.sortie_vocal, user)
    # La liste des modules extérieurs.
    LISTE_MODULES_EXT = initialiser_modules_EXT()
    return {'Utilisateur':user, 'USERInterface':USERInterface, 'LISTE_MODULES_EXT':LISTE_MODULES_EXT}