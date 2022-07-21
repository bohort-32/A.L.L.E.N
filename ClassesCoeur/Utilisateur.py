import json

# Gère les interfaces utilisateur


class Utilisateur:
    """
    Une classe représentant l'utilisateur.

    Attributes
    ----------
    nom : str, optional
        Le nom de l'utilisateur.
    clef_maitre : str, optional
        Le mot de passe de l'utilisateur
    win_usr : str, optional
        Le compte local associé.

    Methods
    -------
    formater_sav()
        Formate les données pour la sauvegarde
    sauvegarder()
        Sauvegarde les données de l'utilisateur.
    charger_donnees_utilisateur(nom_fichier)
        Initialise les données utilisateur depuis un fichier.
    set_nom(nom_nv)
        Change le nom de l'utilisateur et sauvegarde les données.
    set_clef_maitre(clef_maitre_nv)
        Change la clef de l'utilisateur et sauvegarde les données.
    set_win_usr(win_usr_nv)
        Change l'emplacement local et sauvegarde les données.
    set_entree_vocal(entree_vocal)
        Change le paramètre d'entrée des informations.
    set_sortie_vocal(sortie_vocal):
        Change le paramètre de sortie des informations.
    """

    def __init__(self, nom='', clef_maitre='', win_usr=''):
        """
        Parameters
        ----------
        nom : str, optional
            Le nom de l'utilisateur.
        clef_maitre : str, optional
            Le mot de passe de l'utilisateur
        win_usr : str, optional
            Le compte local associé.
        """
        # Elements élémentaire
        self.nom = nom
        self.clef_maitre = clef_maitre
        self.win_usr = win_usr
        # Elements Audio
        self.entree_vocal = False
        self.sortie_vocal = False

        if (self.nom and clef_maitre and win_usr) != '':
            self.sauvegarder()



    def formater_sav(self):
        """Formate les données pour la sauvegarde

        Returns
        -------
        sav_user
            Un dictionnaire de retour.
        """
        # Format de la sauvegarde
        sav_user = {
            "nom": self.nom,
            "ClefMaitre": self.clef_maitre,
            "WinUser": self.win_usr,
            "Audio": {
                "Entrée": self.entree_vocal,
                "Sortie": self.sortie_vocal
            }
        }
        # Retourne le format
        return sav_user



    def sauvegarder(self):
        """Sauvegarde les données de l'utilisateur.
        """
        # Définie les données à sauvegarder
        sav_user = self.formater_sav()
        # Ouvre le fichier
        with open(f'./DATA/{self.win_usr}/utilisateur.json', 'w') as outfile:
            # Ecris
            json.dump(sav_user, outfile)




    def charger_donnees_utilisateur(self, nom_fichier):
        """Initialise les données utilisateur depuis un fichier.

        Parameters
        ----------
        nom_fichier : str
            Nom du fichier où il faut charger les données.
        """
        # Ouverture du fichier de chargement
        with open(nom_fichier, 'r') as f:
            données_user = json.load(f)

        # Extraction des données
        self.nom = données_user['nom']
        self.clef_maitre = données_user['ClefMaitre']
        self.win_usr = données_user['WinUser']

        # Extraction des données Audio
        audio = données_user['Audio']
        self.entree_vocal = audio['Entrée']
        self.sortie_vocal = audio['Sortie']

        # Retour des données
        return self

    # Change et sauvegarde le nom

    def set_nom(self, nom_nv):
        """Change le nom de l'utilisateur et sauvegarde les données.

        Parameters
        ----------
        nom_nv : str
            Nouveau nom.
        """
        self.nom = nom_nv
        self.sauvegarder()

    # Change et sauvegarde la clef
    def set_clef_maitre(self, clef_maitre_nv):
        """Change la clef de l'utilisateur et sauvegarde les données.

        Parameters
        ----------
        clef_maitre_nv : str
            Nouvelle clef.
        """
        self.clef_maitre = clef_maitre_nv
        self.sauvegarder()

    # Change et sauvegarde l'id windows
    def set_win_usr(self, win_usr_nv):
        """Change l'emplacement local et sauvegarde les données.

        Parameters
        ----------
        win_usr_nv : str
            Nouvelle emplacement local.
        """
        self.win_usr = win_usr_nv
        self.sauvegarder()

    # Change et sauvegarde les paramètres audio
    def set_entree_vocal(self, entree_vocal):
        """Change le paramètre d'entrée des informations.

        Parameters
        ----------
        entree_vocal : bool
            L'entrée vocal
        """
        self.entree_vocal = entree_vocal
        self.sauvegarder()

    # Change et sauvegarde les paramètres audio
    def set_sortie_vocal(self, sortie_vocal):
        """Change le paramètre de sortie des informations.

        Parameters
        ----------
        entree_vocal : bool
            La sortie vocal
        """
        self.sortie_vocal = sortie_vocal
        self.sauvegarder()
