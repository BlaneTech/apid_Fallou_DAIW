from view.menu import descRequest
from controller.controller import *
from subprocess import call



class View:

    def __init__(self):
        self.controller = Controller()
        self.call = call

    def cleanConsol(self):
        return self.call('clear')

    def menu(self):
        self.exi = 1
        self.i = 1
        while self.exi > 0:
            print("\n\t\t---------MENU---------\n")
            for key in descRequest.keys():
                print(f"{key} : {descRequest[key]}")
                print()
            try:
                self.n = input("Fites un choix dans le menu\n")
                print()
                if self.n.isnumeric():
                    self.choice = int(self.n)
                    data = self.controller.displays(self.choice)
                    self.cleanConsol()
                    print(f"\n\tvous avez choix l'option {key}\n")
                    print()
                    for i in data:
                        print(list(i),"\n")
                    
                else:
                    self.cleanConsol()
                    print(".....ByE.....")
                    self.exi = -1
            except KeyError:
                print("Choix invalide, réessayer please")
