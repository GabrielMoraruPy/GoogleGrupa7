class Catalog:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f"Catalog pentru elevul {self.nume} {self.prenume}. Numarul de absente: {self.absente}"

    def adauga_absenta(self, numar):
        for i in range(numar):
            self.absente += 1

    def sterge_absente(self, nr_absente):
        if self.absente >= nr_absente:
            self.absente -= nr_absente
        else:
            print("Nu se pot sterge atatea absente.")


class Extensie1(Catalog):
    def adauga_materie(self, materia, note):
        if not all(isinstance(nota, (int, float)) for nota in note):
            print("Nu toate notele sunt numere.")
            return

        self.materii[materia] = note

    def afiseaza_materii(self):
        print("Materiile pentru elevul {0} {1} sunt:".format(self.nume, self.prenume))
        for materia in self.materii:
            print(materia)

    def afiseaza_medii(self):
        print("Mediile pentru elevul {0} {1} sunt:".format(self.nume, self.prenume))
        for materia, note in self.materii.items():
            if all(isinstance(nota, (int, float)) for nota in note):
                media = sum(note) / len(note)
                print(f"{materia}: {media:.2f}")

student1 = Catalog('Ion', 'Roata')

student1.adauga_absenta(3)

student1.sterge_absente(2)

student2 = Catalog('George', 'Cerc')

student2.adauga_absenta(4)

student2.sterge_absente(2)

print(student1.absente)
print(student2.absente)

student1 = Extensie1('Ion', 'Roata')
student2 = Extensie1('George', 'Cerc')
student1.adauga_materie('python', [6, 7, 8], )
student2.adauga_materie('python', [8, 9, 10])

student2.adauga_materie('Matematica', [8, 8, 9])
student1.adauga_materie('Romana', [10, 10, 7])

print(student1.afiseaza_materii())
print(student1.afiseaza_medii())

print(student2.afiseaza_materii())
print(student2.afiseaza_medii())