"""
r -> citim, nu adaugam, vine default, daca fisierul nu exista apare eroare
w -> scriem, daca fisierul nu exista il adauga, daca exista ceva scris in fisier rescrie
a -> append, daca exista ceva scris in fisier, il adauga pe urmatorul rand, nu rescrie,
    nu apare eroare daca fisierul nu exista
r+ -> scriere, citire, daca fisierul nu exista, apare eroare
"""
# file = open('data2.txt', "r+")
# file.write("Hello2")
# file.close()

# file = open('data1.txt', "r+")
# try:
#     file.write('hello')
# exc
# finally:
#     file.close()

# with open('data.txt', 'w') as file:
#     file.write('hello\n')
#     file.write('hello1\n')
#     file.write('hello2')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     print(list(file))
#     # for line in list(file):
#     #     print(line)

with open('data.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)