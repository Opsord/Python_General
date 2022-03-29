#BLOQUE ENTRADAS:

def crear_txt(nombre, base):
#Funcion que crea un archivo de texto a partir de una variable
#Entrada: nombre archivo, variable
#Salida: texto
    with open(nombre,"w") as txt:
        for elemento in base:
            linea= elemento[0] + " " + elemento[1] + "\n"
            txt.write(linea)
        txt.close()
    return True


def validador(lista):
    vocales = "AEIOU"
    # creamos contenedor
    lista_pat_val = []
    # recorremos cada patente
    for pat in lista:
        # definimos que la patente sea invalida
        estado = "invalida"
        # primero verificamos el tamaño del string
        # SUPUESTO: las patentes validas solo tienen 6 caracteres
        if len(pat) == 6:
            # verificamos si la patente cumple con el formato nuevo
            if pat[0] not in vocales and pat[1] not  in vocales \
               and pat[2] not in vocales and pat[3] not in vocales \
               and pat[:4].isalpha() and pat[4:].isdigit():
                estado = "nueva"
            # verificar si cumple con el formato antiguo
            if pat[:2].isalpha() and pat[2:].isdigit():
                estado = "antigua"
        lista_pat_val.append([pat,estado])    
    return lista_pat_val



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



#BLOQUE PROCESAMIENTO:

#Se guarda lo que dice el texto en una variable en forma de lista
txt_arch=input("Ingresar el nombre del archivo: ")
txt_arch=leer_archivo(txt_arch)
txt_arch= validador(txt_arch)
crear_txt("ejemplo_escrito",txt_arch)

print(txt_arch)

#BLOQUE SALIDA

#crear_txt("ejemplo_escrito",txt_arch)