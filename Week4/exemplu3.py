# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.nume = nume
#         self.galaxie = galaxie
#
#
#     def __str__(self):
#         return f"{self.nume} in {self.galaxie}"
#
# soare = Star("Soare", "Calea Lactee")
# print(soare)

class Parinte:


    def __init__(self):
        pass


    def __str__(self):
        return f"Numele meu este "

class Copil(Parinte):


    def  __init__(self,name):
        print(name)
        super().__init__()
        self.name = name
        # Parinte.__init__(self, name)


    def __str__(self):
        return f"Prenumele meu este {self.name}"

obiect = Copil("Alexandra")
print(obiect)