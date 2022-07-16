from Traduction import *
from Recherche import *

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
LISTE_PERSONNE = ['toi', 'Toi', 'Système', 'système', 'Systeme', 'systeme', 'Tu', 'te', 'Sys', 'sys']
LISTE_TRADUCTION = ['Traduire', 'traduire', 'Traduction', 'traduction']
LISTE_TRANSITION = ['en', 'En', 'vers', 'Vers', 'a', 'à']
LISTE_LANGUE = ['Français', 'français', 'Anglais','anglais']



def comprendre(requete, ENTREE_VOCAL, SORTIE_VOCAL, FIN, API_KEY):
    retour = ''

    # Demande allumer
    if (rechercher_mot(requete, LISTE_ENTREE) or rechercher_mot(requete, LISTE_ALLUMER)) == True:
        # Entrée
        if rechercher_mot(requete, LISTE_ENTREE) == True:
            ENTREE_VOCAL = True
        # Sortie
        if rechercher_mot(requete, LISTE_SORTIE) == True:
            SORTIE_VOCAL = True

    # Demande éteindre
    elif rechercher_mot(requete, LISTE_FIN) == True:
        # Système
        if len(requete.split(' ')) == 1 or rechercher_mot(requete, LISTE_PERSONNE) == True:
            FIN = True
        else:
            # Entrée
            if rechercher_mot(requete, LISTE_ENTREE) == True:
                ENTREE_VOCAL = False
            # Sortie
            if rechercher_mot(requete, LISTE_SORTIE) == True:
                SORTIE_VOCAL = False

    # Statut
    if rechercher_mot(requete, LISTE_STATUT) == True:
        # Système
        if len(requete.split(' ')) == 1 or rechercher_mot(requete, LISTE_PERSONNE) == True:
            retour = f"ENTREE_VOCAL : {ENTREE_VOCAL}, SORTIE_VOCAL : {SORTIE_VOCAL}, FIN : {FIN}"


    # Traduction
    if rechercher_mot(requete, LISTE_TRADUCTION) == True or (rechercher_mot(requete, LISTE_LANGUE) and rechercher_mot(requete, LISTE_TRANSITION) == True):
        retour = demande_trad_utilisateur(requete, LISTE_LANGUE, LISTE_TRADUCTION)

    else:
        retour = traduction(rechercher(traduction(requete, 'en', 'fr'), API_KEY), 'fr', 'en')

    return {'Reponse': retour, 'ENTREE_VOCAL': ENTREE_VOCAL, 'SORTIE_VOCAL': SORTIE_VOCAL, 'FIN': FIN}






def rechercher_mot(mot_recherche, liste_mots):
    Trouve = False
    for mot in liste_mots:
        if mot in mot_recherche and Trouve == False:
            Trouve = True
    return Trouve