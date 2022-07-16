import json

# Gère les interfaces utilisateur
class Utilisateur:
    def __init__(self, nom, clef_maitre, win_usr=''):
        self.nom = nom
        self.clef_maitre = clef_maitre
        self.win_usr = win_usr
        self.sauvegarder()

    def sauvegarder(self):
        sav_user = {"name": self.nom, "ClefMaitre": self.clef_maitre, "WinUser":self.win_usr}
        with open(f'./DATA/{self.win_usr}/utilisateur.json', 'w') as outfile:
            json.dump(json.dumps(sav_user), outfile)


    def set_nom(self, nom_nv):
        self.nom = nom_nv
        self.sauvegarder()


    def set_clef_maitre(self, clef_maitre_nv):
        self.clef_maitre_nv = clef_maitre_nv
        self.sauvegarder()


    def set_win_usr(self, win_usr_nv):
        self.win_usr = win_usr_nv
        self.sauvegarder()    