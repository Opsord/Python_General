lista_ejemplo=[1,4,6,2,5,7,3,32,74,12]
#Funcion que recorre listas y permite realizarle operaciones a cada uno de los elementos de la lista
def recorredor_de_listas(lista):
    largo=(len(lista)-1)
    i=0
    while i<=largo:
        #Si se realia una operacion a los elementos se pone en la linea siguiente
        #EJEMPLO: elemento elevado a 2
        lista[i]=(lista[i]**2)
        i=i+1
    #El retorno es la lista modificada(si se realiza una operacion)
    return lista

print(recorredor_de_listas(lista_ejemplo))