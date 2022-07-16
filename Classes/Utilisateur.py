import json

# Gère les interfaces utilisateur
class Utilisateur :
    def __init__(self, nom, clef_maitre):
        self.nom = nom
        self.clef_maitre = clef_maitre

    def format_SAV(self) :
        sav_user = {"name": self.nom, "ClefMaitre": self.clef_maitre}
        return json.dumps(sav_user)