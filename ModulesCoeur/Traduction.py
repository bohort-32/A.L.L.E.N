"""
Ce fichier comporte toutes les fonctions liées à la traduction d'un string
"""
from deep_translator import GoogleTranslator


DIC_AB_LANGUE = {'français':'fr', 'Français':'fr', 'Anglais':'en', 'anglais':'en'}


# Traduction
def traduction(mot, target='en', source='fr'):
    """Traduit un mot d'une langue vers une autre

    Parameters
    ----------
    mot : str
        Le mot à traduire.
    target : str
        La langue à retourner
    source : str
        La langue à traduire.

    Returns
    -------
    str
        Le mot traduit.
    """
    # Dictionnaire des abréviation des langues
    global DIC_AB_LANGUE
    # Vérification nécessité d'une traduction
    if source != target:
        try:
            # Vérifier existance langue
            if source != DIC_AB_LANGUE[source]:
                source = DIC_AB_LANGUE[source]
        except KeyError:
            source = source
            # Vérifier existance langue
        try:
            if target != DIC_AB_LANGUE[target]:
                target = DIC_AB_LANGUE[target]
        except KeyError:
            target = target
        retour = GoogleTranslator(source=source, target=target).translate(mot)

    else:
        retour = "Aucune traduction n'est requise"

    return retour





def demande_trad_utilisateur(demande, LISTE_LANGUE, LISTE_TRADUCTION):
    demande = demande.replace('en', '')
    demande = demande.replace(':', '')
    langue_detectee = ''

    # Supprime la langue de la traduction
    for langue in LISTE_LANGUE:
        old_demande = demande
        demande = demande.replace(langue, '')
        # Détection de la langue
        if old_demande != demande:
            langue_detectee = langue

    # Supprime mots parazites
    for mot in LISTE_TRADUCTION:
        demande = demande.replace(mot, '')

    if langue != '':
        trad = traduction(demande, langue)
    else:
        trad = traduction(demande)
    return trad