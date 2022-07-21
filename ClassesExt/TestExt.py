import imp
from ClassesCoeur.UserInterface import *
from ClassesCoeur.Utilisateur import *

# class inside the module
class TestExt:
    def Comprendre(USERInterface, User):
        USERInterface.informer_utilisateur('Salut')
        print('Salut je suis le test')