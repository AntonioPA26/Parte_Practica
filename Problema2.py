import random
from funciones import *

Tamanio = int(input('La lista será del tamaño: '))
lista1 = []

for i in range(0,Tamanio):
    num = random.randint(1,20)
    lista1.append(num)

primera = funcion1("notas.txt",lista1)
segunda = funcion2("notas2.txt",lista1)