# Prueba importacion 1

import math

lista_1= [10,33,9,14,18,14,12,21,50,55,60]

def ordenador_2(lista):
    largo=(len(lista))
    n=0
    while n<largo:
        i=0
        while i<largo-1:
            a=0
            b=0
            if lista[i]>lista[i+1]:
                a=lista[i]
                b=lista[i+1]
                lista[i]=b
                lista[i+1]=a
            i=i+1
        n=n+1
    return(lista)

ordenador_2(lista_1)
print(lista_1)

def recorredor_de_listas(lista):
    largo=(len(lista)-1)
    i=0
    while i<=largo:
        #reemplazar operacion en linea de abajo
        lista[i]=(round(math.sqrt(lista[i]),4))
        i=i+1

    return lista
recorredor_de_listas(lista_1)

print(lista_1)



