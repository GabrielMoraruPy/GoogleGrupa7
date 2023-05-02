# def a(d):
#     d[4] = 'd'
#     return d
#
# x = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
#
# y = a(x)
# print(y)


def functie1(lista_cuvinte):
    lista = []
    for n in lista_cuvinte:
        lista.append((len(n), n))
    lista.sort()
    return