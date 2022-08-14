from fileinput import close
from binance.client import Client
import config
import pandas as pd
import openpyxl
import pickle
import os
import funciones


#Conexión a Cuenta Binance
client = Client(config.api_key, config.secret_key)

#Detalle de las velas que traigo
candles = client.get_historical_klines("BTCUSDT", client.KLINE_INTERVAL_1HOUR, "3 weeks ago UTC")

#Formateo del dato que traje de velas en PANDAS y conversion en DataFrame
df = pd.DataFrame(candles,
                  columns=['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                           'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])

#Formateo de Columnas del Data Frame

df['Datetime'] = pd.DatetimeIndex(pd.to_datetime(df['Close time'], unit='ms'))
df['Open'] = df['Open'].astype('float')
df['High'] = df['High'].astype('float')
df['Low'] = df['Low'].astype('float')
df['Close'] = df['Close'].astype('float')
df['Volume'] = df['Volume'].astype('float')
df['Close time'] = pd.DatetimeIndex(pd.to_datetime(df['Close time'], unit='ms'))
df['Quote asset volume'] = df['Quote asset volume'].astype('float')
df['Number of trades'] = df['Number of trades'].astype('float')
df['Taker buy base asset volume'] = df['Taker buy base asset volume'].astype('float')
df['Taker buy quote asset volume'] = df['Taker buy quote asset volume'].astype('float')
df['Ignore'] = df['Ignore'].astype('float')


#Aca le doy una columna indice al dataframe para usar el TTI, pero en este ejemplo mio no uso TTI
#Esto lo descomenté y me empezó a salir solo la columna que quiero del DF sin el datetime en formato raro
#df = df.set_index('Datetime')

"""limpiando el DF"""
#Acá limpiamos el DataFrame para preparar la salida que necesitamos analizar con Facu
df2 = df.drop(['Open', 'High', 'Low', 'Quote asset volume', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore', 'Close time'], axis=1)

"""Calculo de la variación"""
#Tambien agrega la Columna de DataFrame
df2['Variacion'] = funciones.calculoVariacion(df2['Close'])


#Calculo de Volatilidad por X periodos
df2['VolatilidadXPeriodos'] = funciones.volatilidadxPeriodos(df2['Variacion'].tolist(),6)

#print(df2['Variacion'][0])


#Acá exporto el DataFrame a Excel (Descomentar el que no corresponda)

#PC DELL XEROX
#df2.to_excel('C:/Users/Friday/Desktop/BTC/BTCUSDT_3W.xlsx')

#PC Gamer makzO
df2.to_excel('C:/Users/makzO/Desktop/facu/BTCUSDT_3W.xlsx')

#PC Facu
#df2.to_excel('C:/Users/Facu/Desktop/Python/BTCUSDT_3W.xlsx')


#Acá voy a hacer una V2 de exportar el DF a excel usando openpyxl



