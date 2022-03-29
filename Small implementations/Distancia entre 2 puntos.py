from math import sqrt
def calcular_distancia(x1, y1, x2, y2):
    """ 
    Función que calcula la distancia entre dos puntos,
    según el teorema de pitágoras
    Entradas: cuatro valores numéricos (x1, y1, x2, y2)
    Salida: valor de la distancia, redondeado a dos decimales
    """
    resultado = (x1 - x2) ** 2 + (y1 - y2) ** 2
    resultado = sqrt(resultado)
    resultado = round(resultado, 2)
    return resultado

# ENTRADAS
x_1 = input('Ingrese valor de coordenada x1: ')
y_1 = input('Ingrese valor de coordenada y1: ')
x_2 = input('Ingrese valor de coordenada x2: ')
y_2 = input('Ingrese valor de coordenada y2: ')
# PROCESAMIENTO
x_1 = float(x_1)
y_1 = float(y_1)
x_2 = float(x_2)
y_2 = float(y_2)
distancia = calcular_distancia(x_1, y_1, x_2, y_2)
# SALIDA
print('La distancia entre:')
print(x_1,',', y_1, ' y ', x_2,',', y_2)
print('es:', distancia)