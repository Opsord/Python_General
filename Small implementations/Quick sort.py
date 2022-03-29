# Ordenador intento 1
#QuickSort

def ordenador_1(lista):
    largo=len(lista)
    i=0
    if largo<=1:
        return(lista)
    else:
        pivote=lista[-1]
        numeros_mayores=[]
        numeros_menores=[]
        while i<len(lista)-1:
            if lista[i]>pivote:
                numeros_mayores.append(lista[i])
            else:
                numeros_menores.append(lista[i])
            i=i+1
        return ordenador_1(numeros_menores)+[pivote]+ordenador_1(numeros_mayores)

ejemplo=[2,5,3,6,8,9,0,3,1,0,1,3,1,4]

ejem_ordenado=ordenador_1(ejemplo)

print(ejem_ordenado)