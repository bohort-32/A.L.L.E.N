class ImportClassesExt:
    """
    Une classe pour importer des classes/modules extérieurs.

    ...

    Attributes
    ----------
    module_name : str
        Le nom du module à intégrer
    class_name : str
        Le nom de la classe à intégrer

    Methods
    -------
    integrer(self, USERInterface, User)
        Lance le module de compréhension.
    """

    def __init__(self, module_name, class_name):
        """
        Parameters
        ----------
        module_name : str
            Le nom du module à intégrer
        class_name : str
            Le nom de la classe à intégrer
        """
        # Nom du module
        module = __import__(module_name)
        # Création de la classe
        my_class = getattr(module, class_name)
        self.module = my_class

    def integrer(self, USERInterface, User):
        """Lance le module de comprhénsion.

        Parameters
        ----------
        USERInterface : UserInterface
            Le module d'interface avec l'utilisateur

        User : Utilisateur
            L'utilisateur courant.
        """
        # Lancement du module de compréhension
        self.module.Comprendre(USERInterface, User)
