class ImportClassesExt:
    def __init__(self, module_name, class_name):
        # Nom du module
        module = __import__(module_name)
        # Création de la classe
        my_class = getattr(module, class_name)
        self.module = my_class
    
    def lancer(self):
        self.module.Comprendre()