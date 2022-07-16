import os
from Modules.Initialisation import *
from Classes.UserInterface import *


def verifierInit(USER_NAME, USERInterface):
    # Chemin des données utilisateurs
    chemin_DATA = f'./DATA'
    # Chemin des données de l'utilisateur courant
    chemin_user = f'{chemin_DATA}/{USER_NAME}'
    # == Vérification présence des dossier
    data_exist = os.path.exists(chemin_DATA)
    chemin_user_exist = os.path.exists(chemin_user)

    if not data_exist or not chemin_user_exist:
        initialiser_dossier(USER_NAME, USERInterface, chemin_DATA, chemin_user, data_exist, chemin_user_exist)


def demarrerScript():
    USER_NAME = os.environ.get( "USERNAME" )
    USERInterface = UserInterface()
    verifierInit(USER_NAME, USERInterface)