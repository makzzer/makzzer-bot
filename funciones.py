import math as ma

lista = [100,200,150]

def variacion (ultimo,anterior):
    return (ultimo-anterior);
    #return ma.log(ultimo/anterior)

#codiguito
lista_variacion = [0]
for i in range (1,len(lista)-1,1):
    lista_variacion.append(variacion(lista[i+1],lista[i]))

    
print(lista_variacion)





