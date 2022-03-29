# BLOQUE DE DEFINICIÓN
    # DEFINICIÓN DE CONSTANTES
N_ARCH_ENTRADA = "patentes.txt"
N_ARCH_SALIDA = "validadas.txt"

    # DEFINICIÓN DE FUNCIONES
# Función que carga patentes desde un archivo
# ENtrada: nombre del archivo a trabajar (string)
# Saldia: lista de patentes (lista de string)
def cargar_patentes(n_arch):
    # 1. Crear un contenedor
    lista_pat = []
    # 2. Abrir archivo
    with open(n_arch,'r') as arch:
        # 3. recorremos cada linea del archivo
        for linea in arch:
            # 4. Procesamos la linea
            pat = linea.strip()
            # 5. Se agrega la linea procesada al contenedor
            lista_pat.append(pat)
        # 6. Cerrar el archivo
        arch.close()
    return lista_pat

# Función que agrega información a cada patente, indicando si
# esta es nueva, antigua, o no es valida
# Entrada: lista de patentes a revisar( lista de strings)
# Salida: Lista de patentes revisadas ( lista de listas de strings)
def validar_patentes(lista_pat):
    vocales = "AEIOU"
    # creamos contenedor
    lista_pat_val = []
    # recorremos cada patente
    for pat in lista_pat:
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

# Función que escribe en un archivo nuevo las patentes y su categorización
# Entrada: lista de patentes validadas (lista de listas de string)
# Salida: ninguna (se realiza la salida por archivo
def escribir_patentes_validadas(n_arch, lista_sal):
    # 1. Abrir archivo en modo requerido
    with open(n_arch,'w') as arch:
        # 2. preparar linea a escribir
        for elem in lista_sal:
            linea = elem[0] + ": " + elem[1] + "\n"
    # 3. escribir la línea
            arch.write(linea)
        arch.close()
    # 4. Cerrar archivo
    return True

# BLOQUE PRINCIPAL
    # ENTRADA
lista_patentes = cargar_patentes(N_ARCH_ENTRADA)
#print(lista_patentes)
# PROCESO
patentes_validadas = validar_patentes(lista_patentes)
print(patentes_validadas)
    # SALIDA
escribir_patentes_validadas(N_ARCH_SALIDA, patentes_validadas)
