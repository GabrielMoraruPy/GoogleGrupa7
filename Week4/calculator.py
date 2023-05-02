class Calculator:

    def __init__(self):
        self.first_op = float(input("Alege primul numar"))
        self.second_op = float(input("Alege al doilea numar"))
        self.op = input("Alege operatia")
        if(self.op == '-'):
            print(self.Scadere())
        elif(self.op == '+'):
            print(self.Adunare())
        elif (self.op == '*'):
            print(self.Inmultire())
        elif (self.op == '/'):
            print(self.Impartire())

    def Adunare(self):
        return (self.first_op + self.second_op)

    def Scadere(self):
        return (self.first_op - self.second_op)

    def Inmultire(self):
        return (self.first_op * self.second_op)

    def Impartire(self):
        if(self.second_op != 0):
            return (self.first_op / self.second_op)
        else:
            return("Nu functioneaza")

    def __str__(self):
        if (self.op == '-'):
            return (self.Scadere())
        elif (self.op == '+'):
            return (self.Adunare())
        elif (self.op == '*'):
            return (self.Inmultire())
        elif (self.op == '/'):
            return (self.Impartire())

obiect1 = Calculator()
obiect2 = Calculator()
obiect3 = Calculator()
obiect4 = Calculator()