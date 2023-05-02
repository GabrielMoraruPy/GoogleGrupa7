class Exemplu1:
    # pass

    counter = 1


    # def name(self):
    #     return "Maria"

class Exemplu2(Exemplu1):

    counter = 2

    # def name(self):
    #     return "Alexandra"

class Exemplu3(Exemplu1,Exemplu2):
    pass


obiect1 = Exemplu3()
print(obiect1.counter)