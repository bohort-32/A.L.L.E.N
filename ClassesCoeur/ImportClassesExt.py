class ImportClassesExt:
    def __init__(self, module_name, class_name):
        # Nom du module
        module = __import__(module_name)
        # Création de la classe
        my_class = getattr(module, class_name)
        my_class.Comprendre()