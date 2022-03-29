# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-C-1
# PROFESOR DE TEORÍA: DIEGO ESCOBAR
# PROFESOR DE LABORATORIO: JUAN GONZALEZ
#
# AUTOR
# NOMBRE: Andres Pablo Zelaya Droguett
# RUT: 20.095.832-2
# CARRERA: Ingeniería Civil Informatica
# PEP N°2 ...<CONTINÚE CON EL PROGRAMA A PARTIR DE AQUÍ> 



#Bloque de definiciones:

def leer_archivo(nombre):
#Funcion que deja como una lista de strings un texto
#Entrada: texto
#Salida: lista de strings
    nombre = nombre + ".txt"
    lista_personas=[]
    with open(nombre,"r",encoding='utf-8') as archivo:
        for linea in archivo:
            fila=linea.strip("\n")
            lista_personas.append(fila)
        archivo.close()
        return lista_personas

def separador(lista_a_separar):
#Funcion que separa en listas mas pequeñas una lista mayor
#Entrada: lista
#Salida: lista de listas
    i=0
    lista_nueva=[]
    while i<len(lista_a_separar):
        contenedor=lista_a_separar[i]
        contenedor2=contenedor.split(",")
        lista_nueva.append(contenedor2)
        i=i+1
    return lista_nueva

def intercambio_en_lista(lista_operada,pos1,pos2):
#Funcion que intercambia de lugar la posicion de 2 elementos en una lista
#Entrada:lista
#Salida: lista con intercambio
    a=lista_operada[pos1]
    b=lista_operada[pos2]
    lista_operada[pos1]=b
    lista_operada[pos2]=a
    return lista_operada

def crear_txt(nombre, base):
#Funcion que crea un archivo de texto a partir de una variable
#Entrada: nombre archivo, variable
#Salida: texto
    with open(nombre,"w") as txt:
        for elemento in base:
            linea= elemento + "\n"
            txt.write(linea)
        txt.close()
    return True

#Bloque de entradas:
fecha=str(input("En formato dia-mes-año ingrese la fecha a analizar: "))
print("La lista de sospechosos del dia "+fecha+" se esta generando, espere un momento por favor.")
lista_gente=leer_archivo("PCR-"+fecha)
actividad_antenas=leer_archivo("LOGS-"+fecha)

#Bloque de procesamiento

#prmero se termina de organizar la entrada, es decir, se separa en listas con sublistas e informacion
lista_gente=separador(lista_gente)
actividad_antenas=separador(actividad_antenas)

#Luego, se separa en una lsita a parte a la gente que hay que evaluar
#respecto a su pcr
gente_a_evaluar=[]
i=0
while i<len(lista_gente):
    if lista_gente[i][3] == "ESPERANDO PCR" or "POSTIVIO":
        gente_a_evaluar.append(lista_gente[i])
    i=i+1

#luego se procede a modificar la lista de personas para organizar mejor los datos en la salida
j=0
while j<len(gente_a_evaluar):
    intercambio_en_lista(gente_a_evaluar[j],2,3)
    j=j+1

#Ahora se procede a cruzar los datos de las personas con la de la actividad de las antenas
#para poder encontrar a gente que posiblemente haya vulnerado al cuarentena
lista_sospechosos=[]

k=0
while k<len(gente_a_evaluar):
    if gente_a_evaluar[k][3]:
        persona_evaluada=gente_a_evaluar[k]
        telefono_a_evaluar=persona_evaluada[3]
        actividad_detectada=[]
        l=0
        while l<len(actividad_antenas):
            if telefono_a_evaluar in actividad_antenas[l]:
                actividad_detectada.append(actividad_antenas[l][0])
                lista_sospechosos.append(persona_evaluada+actividad_detectada)
            l=l+1
    k=k+1


#intento de mejora a resultado final
r=0
while r<len(lista_sospechosos):
    if lista_sospechosos[r][0] == lista_sospechosos[r+1][0]:
        lista_sospechosos.pop(r)
    r=r+1


#Esto finalmente logra reducir todo a una lista de posibles personas que hayan roto la cuarentena

#Finalmente se transofrman las listas dentros de listas en una lista de 
#strings con tal de poder escribirla en un solo texto

lista_para_texto=[]
for elemento in lista_sospechosos:
    lista_prov=" ,".join(elemento)
    lista_para_texto.append(lista_prov)


#Bloque de salida

crear_txt("RESULTADOS-"+fecha,lista_para_texto)
print("La lista ya esta lista para su revision")