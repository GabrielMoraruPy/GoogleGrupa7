import datetime

print("Format CNP S-AA-LL-ZZ-JJ-NNN-C")
cnp = input("Tastati CNP-ul: ")

S = int(cnp[0:1])
AA = int(cnp[1:3])
LL = int(cnp[3:5])
ZZ = int(cnp[5:7])
JJ = int(cnp[7:9])
NNN = int(cnp[9:12])
C = cnp[12:13]

suma = 0
produs = 0
c = 0
rest = 0
for x in "279146358279":
    produs = int(x) * int(cnp[c])
    c += 1
    suma = suma + produs
rest = suma % 11
if rest == 10:
    C = 1
# print(rest)

while len(cnp) != 13:
    print("CNP invalid")

    cnp = input("Tastati din nou")

if len(cnp) == 13:
    valid = True
    if S not in range(1, 9):
        print("CNP invalid")
        valid = False
    # if AA not in range(0, 100):
    #     print("CNP invalid")
    #     valid = False
    # if LL not in range(1, 13):
    #     print("CNP invalid")
    #     valid = False
    # if ZZ not in range(1, 32):
    #     print("CNP invalid")
    #     valid = False
    try:
        datetime.datetime(int(AA), int(LL), int(ZZ))
    except ValueError:
        valid = False
    if JJ not in range(1, 47) and JJ not in range(51, 53):
        print("CNP invalid")
        valid = False
    if NNN not in range(1, 1000):
        print("CNP invalid")
        valid = False
    if C != str(rest) and C != 1:
        print("CNP invalid")
        valid = False
    if valid:
        print("CNP Valid")

sex = ['Masculin', 'Feminin']

luni = ('Ianuarie', 'Februarie', 'Martie',
                'Aprilie', 'Mai', 'Iunie',
                'Iulie', 'August', 'Septembrie',
                'Octombrie', 'Noiembrie', 'Decembrie')

if S == 1 or S == 2:
    mesaj_1 = "Persoana de sex {} nascuta in anul 19{}, luna {} si ziua {}, ".format(sex[S - 1], AA, luni[LL - 1], ZZ)
if S == 5 or S == 6:
    mesaj_1 = "Persoana de sex {} nascuta in anul 20{}, luna {} si ziua {}, ".format(sex[S - 5], AA, luni[LL - 1], ZZ)
if S == 3 or S == 4:
    mesaj_1 = "Persoana de sex {} nascuta in anul 18{}, luna {} si ziua {}, ".format(sex[S - 5], AA, luni[LL - 1], ZZ)
if S == 7 or S == 8:
    mesaj_1 = "CNP pentru persoana straina rezidenta in Romania, persoana de sex {} nascuta in anul 19{}, luna {} si ziua {}, ".format(sex[S - 5], AA, luni[LL - 1], ZZ)
if S == 9:
    mesaj_1 = "Persoana de sex {} nascuta in anul 19{}, luna {} si ziua {}, ".format(sex[S - 5], AA, luni[LL - 1], ZZ)

judete={"Alba": "01", "Arad": "02", "Arges": "03", "Bacau": "04", "Bihor": "05",
        "Bistrita-Nasaud": "06", "Botosani": "07", "Brasov": "08", "Braila": "09", "Buzau": "10",
        "Caras-Severin": "11", "Cluj": "12", "Constanta": "13", "Covasna": "14", "Dambovita": "15",
        "Dolj": "16", "Galati": "17", "Gorj": "18", "Harghita": "19", "Hunedoara": "20",
        "Ialomita": "21", "Iasi": "22", "Ilfov": "23", "Maramures": "24", "Mehedinti": "25",
        "Mures": "26", "Neamt": "27", "Olt": "28", "Prahova": "29", "Satu Mare": "30",
        "Salaj": "31", "Sibiu": "32", "Suceava": "33", "Teleorman": "34", "Timis": "35",
        "Tulcea": "36", "Vaslui": "37", "Valcea": "38", "Vrancea": "39", "Bucuresti": "40",
        "Bucuresti S.1": "41", "Bucuresti S.2": "42", "Bucuresti S.3": "43", "Bucuresti S.4": "44",
        "Bucuresti S.5": "45","Bucuresti S.6": "46", "Calarasi": "51", "Giurgiu": "52"}

for numar, judet in enumerate(judete):
    if JJ == numar + 1:
        mesaj_2 = mesaj_1 + ("in judetul {}, avand numarul de evidenta {} si cifra de control {}.".format(judet, NNN, C))

if valid:
    print(mesaj_2)

#
# an = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# luni = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#
# luni_dictionar = {"01": 'Ianuarie',
#                   "02": 'Februarie',
#                   "03": 'Martie',
#                   "04": 'Aprilie',
#                   "05": 'Mai',
#                   "06": 'Iunie',
#                   "07": 'Iulie',
#                   "08": 'August',
#                   "09": 'Septembrie',
#                   "10": 'Octombrie',
#                   "11": 'Noiembrie',
#                   "12": "Decembrie"
#                   }
#
# zi = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
#       '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
#       '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
#       '31']
#






# if cnp_lista[0] == '3' or cnp_lista[0] == '4':
#     if cnp_lista[1] and cnp_lista[2] in an:
#         print("Anul nasterii este 18{}".format(cnp_lista[1]+cnp_lista[2]))
#
# if cnp_lista[0] == '5' or cnp_lista[0] == '6':
#     if cnp_lista[1] and cnp_lista[2] in an:
#         print("Anul nasterii este 20{}".format(cnp_lista[1]+cnp_lista[2]))
#
# if cnp_lista[0] == '7' or cnp_lista[0] == '8':
#     if cnp_lista[1] and cnp_lista[2] in an:
#         print("Anul nasterii este 19{}".format(cnp_lista[1] + cnp_lista[2]))


# if cnp_lista[1] and cnp_lista[2] in [0,1,2,3,4,5,6,7,8,9]:
#     print("Anul nasterii este: {}")
