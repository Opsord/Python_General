lista1=[1,2,3,4,5,6,7,8,4,3,1,6]

def contador(a_contar,donde_contar):
    total=0
    i=0
    while i<len(donde_contar):
        if donde_contar[i] == a_contar:
            total=total+1
        i=i+1
    return total

#x=contador(3,lista1)
print(lista1)

def intercambio_en_lista(lista_operada,pos1,pos2):
    a=lista_operada[pos1]
    b=lista_operada[pos2]
    lista_operada[pos1]=b
    lista_operada[pos2]=a
    return lista_operada

intercambio_en_lista(lista1,0,1)
print(lista1)