import os
from ModulesCoeur.Initialisation import *
from ClassesCoeur.UserInterface import *


def verifierInit(USER_NAME, USERInterface, chemin_DATA, chemin_user):
    # == Vérification présence des dossier
    data_exist = os.path.exists(chemin_DATA)
    chemin_user_exist = os.path.exists(chemin_user)

    if not data_exist or not chemin_user_exist:
        initialiser_dossier(USER_NAME, USERInterface, chemin_DATA, chemin_user, data_exist, chemin_user_exist)
    


def demarrerScript():
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
    print(user.sortie_vocal)
    USERInterface = UserInterface(user.entree_vocal, user.sortie_vocal, user)

    return {'Utilisateur':user, 'USERInterface':USERInterface}