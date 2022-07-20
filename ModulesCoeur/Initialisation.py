import os
from os import walk
import shutil
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
    LISTE_MODULES_EXT = []
    # Cherche tous les fichiers du répertoire
    for (repertoire, sousRepertoires, liste_fichiers) in walk('./ClassesExt/'):
        # Se limite au répertoire des Classes Externes
        if repertoire == './ClassesExt/':
            # Liste les fichiers
            for fichier in liste_fichiers:
                # Suppression de l'extension
                fichier = fichier.replace('.py', '')
                if fichier != 'Comprendre':
                    # === Définition des chemins à prendre
                    chemin_main = f"{os.getcwd()}/{fichier}.py"
                    os.chdir('./ClassesExt')
                    chemin_init = f"{os.getcwd()}/{fichier}.py"
                    # Bouge le fichier pour exécution du main
                    shutil.move(chemin_init, chemin_main)
                    # Création de l'objet
                    classe_ext = ImportClassesExt(fichier, fichier)
                    LISTE_MODULES_EXT.append(classe_ext)
                    # Rangement du fichier
                    shutil.move(chemin_main, chemin_init)
        return LISTE_MODULES_EXT