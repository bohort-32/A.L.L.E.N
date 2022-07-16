import os
from Classes.Utilisateur import *
from Modules.GestionSAV import *

def initialiser_dossier(USER_NAME, USERInterface, chemin_DATA, chemin_user, data_exist, chemin_user_exist):
    # == Création des dossier si besoin
    if not data_exist:
        os.mkdir(chemin_DATA)
    if not chemin_user_exist:
        os.mkdir(chemin_user)
        # Initialise les informations utilisateur
        initialiser_infos_user(USERInterface, chemin_user)


def initialiser_infos_user(USERInterface, chemin_user):
    nom_user = USERInterface.demande_utilisateur('Comment dois-je vous appeller ?')
    user = Utilisateur(nom_user, 'AZERTY')
    chemin_fichier = f'{chemin_user}/utilisateur.json'
    sauvegarder(chemin_fichier, user.format_SAV())
