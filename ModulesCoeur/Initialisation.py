import os
from ClassesCoeur.Utilisateur import *

def initialiser_dossier(USER_NAME, USERInterface, chemin_DATA, chemin_user, data_exist, chemin_user_exist):
    # == Création des dossier si besoin
    if not data_exist:
        os.mkdir(chemin_DATA)
    if not chemin_user_exist:
        os.mkdir(chemin_user)
        # Initialise les informations utilisateur
        initialiser_infos_user(USERInterface, USER_NAME)


def initialiser_infos_user(USERInterface, USER_NAME):
    nom_user = USERInterface.demande_utilisateur('Comment dois-je vous appeller ?')
    user = Utilisateur(nom_user, 'AZERTY', USER_NAME)
    USERInterface.informer_utilisateur('Félicitations, votre compte est initialisé !')
