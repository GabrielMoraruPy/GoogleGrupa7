a = input("Alegeti o valoare: ")
try:
    print(int(a))
    print(variabila_nedefinita)
except ValueError:
    print("S-a intalnit o eroare")
    a = input("Gasiti alta valoare: ")
except NameError:
    variabila_nedefinita = None
    print("Name error")
except Exception as e:
    print(e)
else:
    print("S-a executat cu succes")
finally:
    print("Se executa oricum")
print("A trecut de blocul try except", variabila_nedefinita)