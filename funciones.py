import math as ma

#acá calculo la formula de la variación
def variacion (actual,anterior):
    #return (actual-anterior);
    return ma.log(actual/anterior)

#acá recorro la lista y devuelvo la lista de variaciónes con el formato correcto
def calculoVariacion(lista):
    lista_variacion = [0]
    for i in range (1,len(lista),1):
        lista_variacion.append(variacion(lista[i],lista[i-1]))
    #print (lista_variacion)    
    return lista_variacion;
    


#lista = [100,300,750,1000]
#resultado = [0,200,450,250]
#print(calculoVariacion(lista))








