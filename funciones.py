import math as ma
import statistics

#acá calculo la formula de la variación
def variacion (actual,anterior):
    return ma.log(actual/anterior)

#acá recorro la lista  vuelvo la lista de variaciónes con el formato correcto
def calculoVariacion(lista):
    lista_variacion = [0]
    for i in range (1,len(lista),1):
        lista_variacion.append(variacion(lista[i],lista[i-1]))  
    return lista_variacion;
    
#Volatilidad de 6 periodos - volatilidad de x periodos

#FormulaDesviacion estandar
def desviacionEstandar (lista,valorMultiplicar):
    return statistics.stdev(lista)*ma.sqrt(valorMultiplicar);

def sumarArray (lista):
    return sum(lista);

#metodo para armar la sublista que quiero recorrer en cada iteración
def armarSublista(lista,numeroActual,indice):
    sublista = []
    for i in range (numeroActual-1,numeroActual-indice-1,-1):
        sublista.append(lista[i])
    return sublista; 

#OJO ESTE METODO NO PUEDE TENER UN VALOR MENOR A 3
#metodo de volatilidad
def volatilidadxPeriodos (lista, indice):
    #poner los ceros
    lista_volatilidad = []
    for i in range (0,indice-1,1):
        lista_volatilidad.append(0)
    for j in range (indice,len(lista)+1,1):
        lista_volatilidad.append(desviacionEstandar(armarSublista(lista,j,indice),338))
        #lista_volatilidad.append(sumarArray(armarSublista(lista,j,indice)))
    return lista_volatilidad;



lista = [2,4,6,8,10,3,1,22]
print(volatilidadxPeriodos(lista,6))


#print(armarSublista(lista,4))

#print (volatilidadxPeriodos(lista,3))

#print (sumarArray(lista))





