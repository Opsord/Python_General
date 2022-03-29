from typing import final


def ordenador_2(lista):
#Funcion que ordena los elementos de una lista de menor a mayor
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
    #El retorno es la lista ordenada    
    return(lista)

def busqueda_binaria(lista, elemto_buscado):
    #Esta funcion busca un elemento en especifico en una lista x
    #devolviendo el indice de la posocion en la que se encuentra
    #La lista tiene que estar ordenada de menor a mayor
    #El proceso utilizado es busqueda binaria
    inicio_lista=0
    final_lista=len(lista)-1
    while inicio_lista<=final_lista:
        punto_medio=(inicio_lista+final_lista)//2
        valor_medio=lista[punto_medio]
        if valor_medio==elemto_buscado:
            return punto_medio
        if elemto_buscado<valor_medio:
            final_lista=(punto_medio-1)
        if elemto_buscado>valor_medio:
            inicio_lista=(punto_medio+1)
    return "El elemento no seuentra en la lista"

ejemplo=[2,3,4,5,6,7,8,8,9,10,11,12]
x=4
print(busqueda_binaria(ejemplo, x))
