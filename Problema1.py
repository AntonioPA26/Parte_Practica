import random

def AlmAleatorios():
    Lista1 = []
    count = 0
    while count < 10:
        Valor = random.randint(1, 20)
        if Valor not in Lista1:
            Lista1.append(Valor)
            count = count + 1
    return Lista1


Lista2 = AlmAleatorios()
print(Lista2)

Lista2.sort()
print(Lista2)

Lista2.sort(reverse=True)
print(Lista2)

ValorMax = max(Lista2)
print(ValorMax)
