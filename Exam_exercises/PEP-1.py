# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-C-1
# PROFESOR DE TEORÍA: DIEGO ESCOBAR
# PROFESOR DE LABORATORIO: JUAN GONZALES
#
# AUTOR
# NOMBRE: Andres Pablo Zelaya Droguett
# RUT: 20.095.832-2
# CARRERA: Ingeniería Civil Informatica
# Programa para PEP 1

#1 Seleccionar facultad a la que se reperesenta

#1.1 Se planea la lista de elecciones y variables implicadas
alumnos_m =0
alumnos_fae =0
alumnos_ig =0
Medicina =["Medicina", ["A favor", "En contra", "Se Abstiene", "med"], alumnos_m]
FAE =["FAE", ["A favor", "En contra", "Se Abstiene", "fae"], alumnos_fae]
Ingenieria=["Ingenieria", ["A favor", "En contra", "Se Abstiene", "ig"], alumnos_ig]
lista_elecciones=[Medicina, FAE, Ingenieria]
k=int(input("Elija la facultad a la que representa, siendo MEDICINA 1, FAE 2 e INGENIERIA 3: "))
#1.2 Se escoge una eleccion
while alumnos_fae == 0 or alumnos_ig == 0 or alumnos_m == 0:
    #2 Verificar la validez de la lista/facultad/eleccion seleccionada (si las listas estan incompletas)
    if lista_elecciones[0][2] != 0 and lista_elecciones[1][2] != 0 and lista_elecciones[2][2] != 0:
            lista_elecciones[0][2] = alumnos_m
            lista_elecciones[1][2] = alumnos_fae
            lista_elecciones[2][2] = alumnos_ig
            print(lista_elecciones)
    else:
        lista_elecciones[k-1][2]=int(input("Ingrese la cantidad de almunos que votaron: "))
        resultado=int(input("Si la facultad SE SUMA al paro, escriba 1, si SE OPONE escriba 2 o si SE ABSTIENE escriba 3: "))-1        
        lista_elecciones[k-1][1]=lista_elecciones[k-1][1][resultado]
        #Se muestra el resultado formado de la eleccion de la facultad seleccionada
        print(lista_elecciones[k-1])
        if lista_elecciones[0][2] != 0 and lista_elecciones[1][2] != 0 and lista_elecciones[2][2] != 0:
            lista_elecciones[0][2] = alumnos_m
            lista_elecciones[1][2] = alumnos_fae
            lista_elecciones[2][2] = alumnos_ig
            print(lista_elecciones)
        else:
            k = int(input("Ahora elija otra facultad, siendo MEDICINA 1, FAE 2 e INGENIERIA 3: "))
    if lista_elecciones[k-1][2] != 0:
        print("La lista seleccionada ya se encuentra constutuida")
        k = int(input("Intente con otra facultad: "))
        
    #3 De ser valida la votacion se procede a pedir los resultados
    
        
#4 Una vez se tienen los datos se hace el conteo de votos
total_votos = Medicina[2]+FAE[2]+Ingenieria[2]
print(total_votos)


