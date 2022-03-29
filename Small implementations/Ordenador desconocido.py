# Ordenador intento 3

def swap(lista, inicio, final):
    valor1 = lista[inicio]
    valor2 = lista[final]
    lista[inicio] = valor2
    lista[final] = valor1
    return lista

def particiona(lista, inicio, final):

    x = lista[final]
    i = inicio - 1
    j = inicio
    while(j < final):
        if(lista[j] < x):
            i += 1
            lista = swap(lista, i, j)
        j += 1

    lista = swap(lista, i + 1, final)
    return i + 1


def quick_sort(lista, inicio, final):
    if(inicio < final):
        medio = particiona(lista, inicio, final)
        quick_sort(lista, inicio, medio-1)
        quick_sort(lista, medio+1, final)
    

ejemplo=[48,45,8,4,4,8,15,1,21,54,8,45,12,61,4,8,5,16,54,8]

print(ejemplo)

quick_sort(ejemplo, 0, len(ejemplo)-1)

print(ejemplo)
