# Explica qué proceso realiza el algorítmo.
# ¿Cuáles son los casos que no se consideran en el algoritmo?
# Completa el código para considerar los casos que no se toman en cuenta.

a = 2
b = 1
c = 3

lista = [a, b, c]

if a >= b and a >= c:
    if b >= c:
        lista = [a, b, c]

    if c >= b:
        lista = [a, c, b]

    print(lista)

elif b >= a and b >= c:
    if a >= c:
        lista = [b,a,c]

    if c >= a:
        lista = [b,c,a]

    print(lista)

elif c >= a and c >= b:
    if a >= b:
        lista = [c,a,b]

    if b >= a:
        lista = [b,c,a]

    print(lista)