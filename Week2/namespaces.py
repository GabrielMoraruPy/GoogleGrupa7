from functii2 import functie2
variabila1 = 2
a = 3
b = 2
msg = 3


def functie_1(a, b):
    variabila1 = a + b
    global msg
    msg = "hello"
    print(variabila1, 'rand 6')
    return variabila1

print(msg, 'rand 12')
suma = functie_1(1, 2)
print(msg, 'rand 16')
print(suma)

functie2(4,5)
