def bauble_sort(lista):
#Funcion que ordena los elementos de una lista de menor a mayor
#Ordenamiento burbuja
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
#Ejemplo con una lista cualquiera
ejemplo=[1,2,4,3,6,5,7,8,10,9,12,11,13,15,14]
ejemplo=bauble_sort(ejemplo)
print(bauble_sort(ejemplo))

def subconjuntos(lista,intervalo):
    lista_nueva=[]
    intervalo=intervalo + 1
    i=0
    contenedor=[]
    while i<len(lista):
        contenedor.append(lista[i])
        x=len(contenedor)
        if len(contenedor)==intervalo:
            lista_nueva.append(contenedor)
            contenedor=[]
        i=i+1
    return lista_nueva
print(len(ejemplo))

ejemplo=subconjuntos(ejemplo,7)
print(ejemplo)