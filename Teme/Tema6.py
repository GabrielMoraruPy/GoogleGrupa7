class Clasa1:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip
        self.culoare = None

    def alegere_culoare(self, culoare):
        self.culoare = culoare

    def afisare_culoare(self):
        return self.culoare


class Clasa2(Clasa1):
    def scaune(self, scaune_incalzite):
        self.scaune_incalzite = scaune_incalzite


class Clasa3(Clasa1):
    def adauga_led(self, blocuri_optice_led):
        self.blocuri_optice_led = blocuri_optice_led


masina = Clasa2("ARO", "M461")
masina.scaune("Nu")
masina.alegere_culoare("Rosu")
print(f"Masina marca {masina.marca}, tip {masina.tip}, de culoare {masina.afisare_culoare()}, cu scaune incalzite {masina.scaune_incalzite}")

masinaDacia = Clasa3("Dacia", "1310")
masinaDacia.adauga_led("Nu")
print(f"Masina marca {masinaDacia.marca}, tip {masinaDacia.tip}, de culoare {masinaDacia.afisare_culoare()}, cu led-uri {masinaDacia.blocuri_optice_led}")

masina1 = Clasa1("Opel", "Corsa")
masina1.alegere_culoare("Gri")
print(f"Masina marca {masina1.marca}, tip {masina1.tip}, de culoare {masina1.afisare_culoare()}")

masina2 = Clasa2("Dacia", "SUV")
masina2.alegere_culoare("Rosu")
masina2.scaune("Adevarat")
print(f"Masina marca {masina2.marca}, tip {masina2.tip}, de culoare {masina2.afisare_culoare()}, cu scaune incalzite: {masina2.scaune_incalzite}")

masina3 = Clasa3("Mercedes", "Coupe")
masina3.alegere_culoare("Negru")
masina3.adauga_led("Adevarat")
print(f"Masina marca {masina3.marca}, tip {masina3.tip}, de culoare {masina3.afisare_culoare()}, cu blocuri optice LED: {masina3.blocuri_optice_led}")