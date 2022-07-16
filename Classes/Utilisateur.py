import json

# Gère les interfaces utilisateur
class Utilisateur:
    def __init__(self, nom='', clef_maitre='', win_usr=''):
        self.nom = nom
        self.clef_maitre = clef_maitre
        self.win_usr = win_usr
        if (self.nom and clef_maitre and win_usr) != '':
            self.sauvegarder()

    def sauvegarder(self):
        # Définie les données à sauvegarder
        sav_user = {"nom": self.nom, "ClefMaitre": self.clef_maitre, "WinUser":self.win_usr}
        # Ouvre le fichier
        with open(f'./DATA/{self.win_usr}/utilisateur.json', 'w') as outfile:
            # Ecris
            json.dump(sav_user, outfile)


    def charger_donnees_utilisateur(self, nom_fichier):
        # Ouverture du fichier de chargement
        with open(nom_fichier, 'r') as f:
            données_user = json.load(f)
        
        # Extraction des données
        self.nom = données_user['nom']
        self.clef_maitre = données_user['ClefMaitre']
        self.win_usr = données_user['WinUser']

        # Retour des données
        return self
        

    # Change et sauvegarde le nom
    def set_nom(self, nom_nv):
        self.nom = nom_nv
        self.sauvegarder()

    # Change et sauvegarde la clef
    def set_clef_maitre(self, clef_maitre_nv):
        self.clef_maitre_nv = clef_maitre_nv
        self.sauvegarder()

    # Change et sauvegarde l'id windows
    def set_win_usr(self, win_usr_nv):
        self.win_usr = win_usr_nv
        self.sauvegarder()    