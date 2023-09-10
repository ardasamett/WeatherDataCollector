import pandas as pd
from datetime import date
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


try:
    GH_SECRETS_URIKEY = os.environ["GH_SECRETS_URIKEY"]
except KeyError:
    GH_SECRETS_URIKEY = "GH_SECRETS_URIKEY ERROR"
    

df = pd.read_csv('WeatherData.csv')


client = MongoClient(GH_SECRETS_URIKEY, server_api=ServerApi('1'))
db = client["WeatherDataDB"]
collection = db["WeatherDataColl"]


today = date.today().strftime("%Y-%m-%d")

data = collection.find_one({"_id": today})
if data:
    for city, city_data in data['Data'].items():
        localtime = city_data['location']['localtime']
        temperature_c = city_data['current']['temp_c']
        wind_speed_kph = city_data['current']['wind_kph']
        humidity = city_data['current']['humidity']
        condition = city_data['current']['condition']['text']

        df = df._append({'City': city, 'LocalTime': localtime, 'Temperature_C': temperature_c, 'Wind_Speed_kph': wind_speed_kph, 'Humidity': humidity, 'Condition': condition}, ignore_index=True)

df.to_csv('WeatherData.csv', index=False)
