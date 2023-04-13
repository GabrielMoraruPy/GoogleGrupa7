numar_initial = int(input("Alegeti un numar: "))
semne = "Alegeti o operatie: +, -, *, / "

semn = ""
continuare = ""
while True:
    print(semne)
    semn = input()
    numar_2 = int(input("Alegeti urmatorul numar: "))
    rezultat = ""
    if semn in semne:
        if semn == "+":
            rezultat = numar_initial + numar_2
            print(rezultat)
        elif semn == "-":
            rezultat = numar_initial - numar_2
            print(rezultat)
        elif semn == "*":
            rezultat = numar_initial * numar_2
            print(rezultat)
        elif semn == "/":
            rezultat = numar_initial / numar_2
            print(rezultat)
    continuare = input("Continuati calculul? ")
    if continuare == "da".casefold():
        numar_initial = 0 + int(rezultat)
    else:
        break