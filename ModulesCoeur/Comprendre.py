from ModulesCoeur.Traduction import *
from ModulesCoeur.Recherche import *
from ClassesCoeur.ImportClassesExt import *


"""
Ce fichier comporte toutes les fonctions liées à la compréhension écrite et orale d'une demande
"""



# Listes de mots à comprendre
LISTE_FIN = ['fin', 'fermeture', 'Fermeture', 'Fermer', 'fermer', 'éteindre', 'Eteindre', 'Off', 'off', 'Eteinds', 'éteinds', 'eteinds', 'Eteind', 'éteind', 'eteind']
LISTE_PARLER = ['parle', 'parler', 'Parle', 'Parler']
LISTE_ALLUMER = ['allumer', 'on', 'Allumer', 'On']
LISTE_ENTREE = ['Entrée', 'entrée', 'Entree', 'entrée', 'Input', 'input']
LISTE_SORTIE = ['Sortie', 'sortie', 'Output', 'output']
LISTE_STATUT = ['Statut', 'statut']
LISTE_ALLEN = ['toi', 'Toi', 'Système', 'système', 'Systeme', 'systeme', 'Tu', 'Sys', 'sys']
LISTE_TRADUCTION = ['Traduire', 'traduire', 'Traduction', 'traduction']
LISTE_TRANSITION = ['en', 'En', 'vers', 'Vers', 'a', 'à']
LISTE_LANGUE = ['Français', 'français', 'Anglais','anglais']




def comprendre(requete, API_KEY, USERInterface, LISTE_MODULES_EXT, User):
    """Etudie la requete de l'utilisateur et retourne une réponse.

    Parameters
    ----------
    requete : str
        La demande de l'utilisateur.
    API_KEY : int
        La clef API wolframalpha.
    USERInterface : UserInterface
        L'interface avec l'utilisateur.
    LISTE_MODULES_EXT : list
        La liste d'objet des modules externes.
    User : Utilisateur
        L'utilisateur courant

    Returns
    -------
    list
        La réponse du système avec l'état du système.
    """
    retour = ''
    FIN = False
    # A corriger dans la partie vérification entrées
    if LISTE_MODULES_EXT != None:
        for classe_ext in LISTE_MODULES_EXT:
            classe_ext.integrer(USERInterface, User)
    


    recherche_entree = rechercher_mot(requete, LISTE_ENTREE)
    recherche_sortie = rechercher_mot(requete, LISTE_SORTIE)
    recherche_allumer = rechercher_mot(requete, LISTE_ALLUMER)
    recherche_eteindre = rechercher_mot(requete, LISTE_FIN)
    recherche_ALLEN = rechercher_mot(requete, LISTE_ALLEN)

    # Demande allumer
    if (recherche_allumer) == True:
        # Entrée
        if recherche_entree == True:
            USERInterface.set_entree_vocal(True)
        # Sortie
        if recherche_sortie:
            USERInterface.set_sortie_vocal(True)

    # Demande éteindre
    elif recherche_eteindre:
        # Système
        if len(requete.split(' ')) == 1 or recherche_ALLEN == True:
            FIN = True
        else:
            # Entrée
            if recherche_entree:
                USERInterface.set_entree_vocal(False)
            # Sortie
            if recherche_sortie:
                USERInterface.set_sortie_vocal(False)


    # Traduction
    elif rechercher_mot(requete, LISTE_TRADUCTION) == True or (rechercher_mot(requete, LISTE_LANGUE) and rechercher_mot(requete, LISTE_TRANSITION) == True):
        retour = demande_trad_utilisateur(requete, LISTE_LANGUE, LISTE_TRADUCTION)

    # Recherche
    else:
        retour = traduction(rechercher(traduction(requete, 'en', 'fr'), API_KEY), 'fr', 'en')




    return {'Reponse': retour, 'FIN': FIN}






def rechercher_mot(mot_recherche, liste_mots):
    """Recherche si un mot est présent dans une liste

    Parameters
    ----------
    mot_recherche : str
        Le mot recherché
    liste_mots : list
        La liste où il faut chercher.

    Returns
    -------
    bool
        True si le mot est présent, False sinon.
    """
    Trouve = False
    for mot in liste_mots:
        if mot in mot_recherche and Trouve == False:
            Trouve = True
    return Trouve

