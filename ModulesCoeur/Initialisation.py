import os
from os import walk
from ClassesCoeur.Utilisateur import *
from ClassesCoeur.ImportClassesExt import *

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


def initialiser_modules_EXT():
    # Cherche tous les fichiers du répertoire
    for (repertoire, sousRepertoires, liste_fichiers) in walk('./ClassesExt/'):
        # Se limite au répertoire des Classes Externes
        if repertoire == './ClassesExt/':
            # Liste les fichiers
            for fichier in liste_fichiers:
                # Suppression de l'extension
                fichier = fichier.replace('.py', '')
                if fichier != 'Comprendre':
                    # Création de l'objet
                    obj = ImportClassesExt(fichier, fichier)
                    print(fichier)
            