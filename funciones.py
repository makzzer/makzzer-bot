import math as ma
import statistics

#acá calculo la formula de la variación
def variacion (actual,anterior):
    return ma.log(actual/anterior)

#acá recorro la lista y devuelvo la lista de variaciónes con el formato correcto
def calculoVariacion(lista):
    lista_variacion = [0]
    for i in range (1,len(lista),1):
        lista_variacion.append(variacion(lista[i],lista[i-1]))  
    return lista_variacion;
    
#Volatilidad de 6 periodos - volatilidad de x periodos

def desviacionEstandar (lista):
    return statistics.stdev(lista)

#metodo para armar la sublista que quiero recorrer en cada iteración
def armarSublista(lista,inicio,fin):
    sublista = []
    while(i < len(lista)):
        list.append(lista[i:i+n])
        #i += n
    return list; 

#metodo de volatilidad
def volatilidadxPeriodos (lista, indice):
    lista_volatilidad = []
    for i in range (indice,len(lista),1):
        lista_volatilidad.append(0)
    return lista_volatilidad;







lista = [100,300,750,1000,2000,3000,5000]

print(volatilidadxPeriodos(lista,5))

#resultado = [0,200,450,250]
#print(calculoVariacion(lista))








