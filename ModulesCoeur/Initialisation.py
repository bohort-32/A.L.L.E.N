import os
from os import walk
import shutil
from ClassesCoeur.Utilisateur import *
from ClassesCoeur.ImportClassesExt import *


def initialiser_dossier(USER_NAME, USERInterface, chemin_DATA, chemin_user, data_exist, chemin_user_exist):
    """Crée le dossier des données de l'utilisateur.

    Parameters
    ----------
    USER_NAME : str
        Nom local de l'utilisateur
    USERInterface : UserInterface
        L'interface utilisateur.
    chemin_DATA : str
        Chemin des données logiciel.
    chemin_user : str
        Chemin des données utilisateur.
    data_exist : bool
        Indique si les données logiciels sont présentes.
    chemin_user_exist : bool
        Indique si les données utilisateurs sont présentes.

    """
    # == Création des dossier si besoin
    if not data_exist:
        os.mkdir(chemin_DATA)
    if not chemin_user_exist:
        os.mkdir(chemin_user)
        # Initialise les informations utilisateur
        initialiser_infos_user(USERInterface, USER_NAME)


def initialiser_infos_user(USERInterface, USER_NAME):
    """Initialise les données de l'utilisateur

    Parameters
    ----------
    USERInterface : UserInterface
        L'interface utilisateur.
    USER_NAME : str
        Le nom de l'utilisateur en local.
    """
    nom_user = USERInterface.demande_utilisateur('Comment dois-je vous appeller ?')
    user = Utilisateur(nom_user, 'AZERTY', USER_NAME)
    USERInterface.informer_utilisateur('Félicitations, votre compte est initialisé !')
    
    


def initialiser_modules_EXT():
    """Charge l'ensemble des modules extérieurs présents.

    Returns
    -------
    list
        Liste de modules extérieurs.
    """
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