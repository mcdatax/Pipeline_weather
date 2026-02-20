import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, API_KEY_WAPI, PHONE_NUMBER_DESTINATION
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_wapi(api_key,city):

    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no' # URL de la API de WeatherAPI para obtener el pronóstico del clima de la ciudad especificada

    try :
        response = requests.get(url).json()
    except Exception as e:
        print(e)

    return response

def get_forecast_data(response, i): # Función para extraer los datos de la hora i del día 0 del pronóstico
    
    date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
    hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
    condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text'].strip()
    temp_c = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
    will_it_rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    chance_of_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
    
    return date, hour, condition, temp_c, will_it_rain, chance_of_rain



def create_df(data):
    
    cols = ['date', 'hour', 'condition', 'temp_c', 'will_it_rain', 'chance_of_rain'] # Nombres de las columnas para el DataFrame
    df = pd.DataFrame(data, columns=cols) # Crear un DataFrame de pandas a partir de la lista de datos y los nombres de las columnas
    df = df.sort_values(by = 'hour',ascending = True) # Ordenar el DataFrame por la columna "hour" en orden ascendente (de menor a mayor)
    df_rain = df[(df['will_it_rain']==1) & (df['hour']>6) & (df['hour']< 22)] # Filtrar el DataFrame para obtener solo las filas donde 'will_it_rain' es igual a 1 (indica que lloverá) y la hora está entre las 6 AM y las 10 PM
    df_rain = df_rain[['hour','condition']] # Seleccionar solo las columnas "hour" y "condition" del DataFrame filtrado
    df_rain.set_index('hour', inplace = True) # Establecer la columna 'hour' como el índice del DataFrame, lo que facilita la visualización y manipulación de los datos relacionados con las horas del día
    
    return df_rain

def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df,city):

    account_sid = TWILIO_ACCOUNT_SID # SID de la cuenta de Twilio, que es un identificador único para tu cuenta en Twilio
    auth_token = TWILIO_AUTH_TOKEN # Token de autenticación de Twilio, que es una clave secreta utilizada para autenticar tu cuenta al enviar mensajes a través de la API de Twilio

    if df.empty:
        mensaje_sms = "Hoy no va a llover, disfruta del buen clima !"
    else: 
        horas_lluvia = ", ".join(df['hour'].astype(str)) # Convertimos las horas a string y unirlas con comas para crear una lista de horas en las que se pronostica lluvia
        mensaje_sms = f"Alerta {city}: Lluvia a las {horas_lluvia} horas" # Crear el mensaje de texto que se enviará, indicando la ciudad y las horas en las que se pronostica lluvia

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=mensaje_sms,
        from_=TWILIO_PHONE_NUMBER,
        to=PHONE_NUMBER_DESTINATION
    )

    return message.sid
