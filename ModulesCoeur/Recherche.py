import wolframalpha


# Retourne à partir d'une question (string) et d'un clefs la réponse à la question (string)
def rechercher(question, app_id):
    """Recherche sur wolframalpha une question.

    Parameters
    ----------
    question : str
        La question à répondre
    app_id : str
        La clef API

    Returns
    -------
    str
        La réponse trouvée.
    """
    # Tableau compilant les résultats
    resultat = []
    # Connexion à l'API
    client = wolframalpha.Client(app_id)
    # Pose la question en Anglais
    res = client.query(question)
    retour = ''
    for pod in res.pods:
        for sub in pod.subpods:
            # Transformation des résultats en string
            res = str(sub.plaintext)
            # Limitattion de la taille pour la traduction
            if len(res) < 5000:
                # Ajout au tableau des résultats
                if res != 'None':
                    retour = retour + res + '\n'
                resultat.append(res)
    # Retour de la réponse
    return retour