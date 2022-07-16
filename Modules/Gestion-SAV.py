import os

def initialiser_donnees(USER_NAME):
    # Chemin des données utilisateurs
    chemin_DATA = f'../DATA/'
    # Chemin des données de l'utilisateur courant
    chemin_user = f'{chemin_DATA}/{USER_NAME}'
    # == Vérification présence des dossier
    data_exist = os.path.exists(chemin_DATA)
    chemin_user_exist = os.path.exists(chemin_user)
    # == Création des dossier si besoin
    if not data_exist:
        os.mkdir(chemin_DATA)
    if not chemin_user_exist:
        os.mkdir(chemin_user)