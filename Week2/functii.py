# print("String")
# var_1 = 1
# print("string {}".format(var_1))
# input("Adauga o cifra")

# def functie_adunare(param1):
#     print('print')
#     return param1, '-'
#
# functie_adunare(1)

def get_sum(a: int = 1, b: int = 3, c: int = 2, *args, **kwargs) -> (int, int):
    """

    :param a: primul parametru
    :param b: al doile parametru
    :param c:
    :param args:
    :param kwargs:
    :return: suma tuturor parametrilor
    """
    suma = a + b + c
    diferenta = a - b - c
    print(args)
    print(kwargs, type(kwargs))
    for i in kwargs.values():
        suma += i
        diferenta -= i
    return suma, diferenta

var_1, var_2 = get_sum(-3, -4, c = -2, d = 4, e = 5, f = 6)
print(var_1, var_2)