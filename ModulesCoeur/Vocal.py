import pyttsx3
import speech_recognition as sr


"""
Ce fichier comporte toutes les fonctions liées à la compréhension et à l'expression orale
"""


# Parle à partir d'un string
def parler(phrase):
    """Sort en vocal une phrase.

    Parameters
    ----------
    phrase : str
        La phrase à parler
    """
    # Ouverture de la machine
    engine = pyttsx3.init()
    engine.say(phrase)
    # Fermeture de la machine
    engine.runAndWait()



# Ecouter l'utilisateur et retranscrit en string sa compréhension
def ecouter():
    """Ecoute l'utilisateur.

    Returns
    -------
    str
        Le texte entendu.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ecoute : ")
        audio = r.listen(source)
    # tentative d'écoute
    try:
        text = r.recognize_google(audio, language="fr-FR")
    # Erreur de compréhension
    except sr.UnknownValueError:
        text = "L'audio n'as pas été compris"
    # Aucun serfice disponible
    except sr.RequestError as e:
        text = "Le service Google Speech API ne fonctionne plus" + format(e)
    # retour de la compréhension
    return text

