import os
import warnings

# Suprimir todos los warnings ANTES de importar cualquier librería que los genere
warnings.filterwarnings('ignore', category=Warning)

from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, API_KEY_WAPI, PHONE_NUMBER_DESTINATION
import time 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime
from utils import request_wapi,get_forecast_data,create_df,send_message,get_date

city = 'Madrid' # Puedes cambiar la ciudad por la que quieras consultar el clima
api_key = API_KEY_WAPI # Puedes obtener tu API key gratuita en https://www.weatherapi.com

input_date= get_date()
response = request_wapi(api_key,city) 


datos = []
for i in tqdm(range(24),colour = 'green'):
    datos.append(get_forecast_data(response,i))

df_rain = create_df(datos)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_rain,city)
print(message_id)