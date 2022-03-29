def leer_archivo(nombre):
#Funcion que deja como una lista de strings un texto
#Entrada: texto
#Salida: lista de strings
    nombre = nombre + ".txt"
    lista_palabras=[]
    with open(nombre,"r") as archivo:
        for linea in archivo:
            fila=linea.strip()
            lista_palabras.append(fila)
        archivo.close()
        return lista_palabras

archivo=input("Ingresar el nombre del archivo: ")
archivo=leer_archivo(archivo)
print(archivo)