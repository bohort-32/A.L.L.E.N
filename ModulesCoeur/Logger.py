import imp
import logging
from logging.handlers import RotatingFileHandler
import os.path
from ClassesCoeur.Utilisateur import *


def get_logger(utilisateur, nom_fic='logfile', format="%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) : %(message)s"):
    """Retourne le logger

    Parameters
    ----------
    utilisateur : Utilisateur
        L'utilisateur en cours.
    nom_fic : str, optionnal
        Nom du fichier pour sauvegarder les logs
    format : str, optionnal
        Format du log

    Returns
    -------
    app_log
        Le logger.
    """

    # == Initialisation du chemin et du fichier
    chemin = f"./DATA/{utilisateur.win_usr}/Logs"
    nom_fic = f"{chemin}/{nom_fic}"
    # Le chemin existe
    existe = os.path.isdir(chemin)

    # Si le dossier des logs existe
    if not existe:
        # Création du dossier
        os.mkdir(chemin)

    # Formatage du log
    log_formatter = logging.Formatter(format)
    # ==== Gestion de la taille du fichier
    my_handler = RotatingFileHandler(nom_fic, mode='a', maxBytes=5*1024*1024, backupCount=5, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)
    # === Création du logger
    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)
    app_log.addHandler(my_handler)

    # Retour du logger
    return app_log