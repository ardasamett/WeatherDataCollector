import logging
import logging.handlers
import os
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import TURKISH_CITIES, VERSION
from datetime import date

# Logger ayarları
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

# GitHub secrets
try:
    GH_SECRETS_APIKEY = os.environ["GH_SECRETS_APIKEY"]
    GH_SECRETS_URIKEY = os.environ["GH_SECRETS_URIKEY"]
except KeyError:
    GH_SECRETS_APIKEY = "GH_SECRETS_APIKEY ERROR"
    GH_SECRETS_URIKEY = "GH_SECRETS_URIKEY ERROR"

def fetch_weather_data(api_key, uri_key, cities):
    current_date = date.today().strftime("%Y-%m-%d")

    # MongoDB bağlantısı
    client = MongoClient(uri_key)
    data = {"_id": current_date, "Data": {}}

    for city, coordinates in cities.items():
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": api_key,
            "q": f"{coordinates[0]},{coordinates[1]}",
            "aqi": "no"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            fetchData = response.json()
            fetchedRegion = fetchData["location"]["region"].lower()
            fetchedName = fetchData["location"]["name"].lower()
            cityLower = city.lower()

            if (fetchedRegion != cityLower) or (fetchedName != cityLower):
                logger.info(f"We couldn't retrieve the coordinates for city {city}, so we obtained the data for the city {fetchedRegion} with the closest coordinates.")
            data["Data"][city] = fetchData
        else:
            raise Exception(f"STATUS CODE ERROR, {response.status_code}")

    db = client["WeatherDataDB"]
    collection = db["WeatherDataColl"]
    collection.insert_one(data)
    logger.info(f"Data successfully added on MongoDB\n{'<->'*10}")

if __name__ == "__main__":
    logger.info(f"VERSION: {VERSION}")
    fetch_weather_data(GH_SECRETS_APIKEY, GH_SECRETS_URIKEY, TURKISH_CITIES)
