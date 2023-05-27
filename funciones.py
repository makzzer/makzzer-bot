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
#Esto es (desviació estandar ( ultimos 6 datos de la variacion) * raiz (336))
def desviacionEstandar (lista,valorMultiplicar):
    return statistics.stdev(lista)*ma.sqrt(valorMultiplicar);

#metodo para probar el recorrido correcto de la desviacion estandar con un metodo sencillo de suma de array
def sumarArray (lista):
    return sum(lista);

#metodo para armar la sublista que quiero recorrer en cada iteración
def armarSublista(lista,numeroActual,indice):
    sublista = []
    for i in range (numeroActual-1,numeroActual-indice-1,-1):
        sublista.append(lista[i])
    return sublista; 

# lista = [10000,2,4,6,8,10,20,3,1,22]

#OJO ESTE METODO NO PUEDE TENER UN VALOR MENOR A 3
#metodo de volatilidad
#voy a asumir que la lista tiene siempre al menos 7 periodos

def volatilidadxPeriodos (lista, indice):

    #creo una lista auxiliar de la lista de variaciones original para no modificarla
    listaVarAux = lista.copy()
    #borro el primer elemento porque es un 0 pero de la lista auxiliar
    listaVarAux.pop(0)

    #creo la lista a retornar y en el primer for le agrego los 0
    lista_volatilidad = []
    for i in range (0,indice-1,1):
        lista_volatilidad.append(0)

    #acá laburo el armarsublista con el parametro listaVarAux porque es la lista original pero sin el primer elemento
    for j in range (indice,len(lista),1):
        #lista_volatilidad.append(desviacionEstandar(armarSublista(listaVarAux,j,indice),336))
        lista_volatilidad.append(sumarArray(armarSublista(listaVarAux,j,indice)))
    return lista_volatilidad;



lista = [10000,2,4,6,8,10,20,3,1,22]

# por 6 tiene que dar, tomando com primero el 20, luego 3,1,22
# [0, 0, 0, 0, 0, 50, 51, 48,64]


#print(volatilidadxPeriodos(lista,6))

#print(armarSublista(lista,4))

#print (volatilidadxPeriodos(lista,3))

#print (sumarArray(lista))





