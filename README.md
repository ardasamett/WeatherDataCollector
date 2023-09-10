![](https://i.ibb.co/Wnyg61L/Blank-diagram.png)

<center>

# Weather Data Collector

</center>

This project includes a Python application that retrieves, processes, and stores daily weather data for specific cities using the "WeatherAPI." It also integrates this data with a MongoDB database and exports it to a CSV file.

## Table of Contents

- [Project Description](#project-description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Requirements](#requirements)
- [Contributing](#contributing) 
- [Raw Data Example](#raw-data-example)
- [Processed Data](#processed-data)

## Project Description

This project fetches daily weather data for Turkish cities using the "WeatherAPI" and stores it in a MongoDB database. It also converts this data into a CSV file and integrates it with current data.

**Dependencies**

* WeatherAPI: API KEY
* MongoDB: Cluster/DB URI KEY
* GitHub Actions (to schedule and workflow)

## Getting Started

You can get started with the project by either cloning it to your local machine or downloading it as a ZIP file.

```
git clone https://github.com/ardasamett/WeatherDataCollector.git
```

## Usage
(Please make sure to pay attention to dependencies.)

To run the project manually, follow these steps: 

1. Navigate to the project directory: `cd WeatherDataCollector`
2. Run the main.py to collect weather data: `python main.py`
3. Run the datamanager.py to process and store the data: `python datamanager.py`

## GitHub Actions Workflow

This project uses GitHub Actions to automate the process of collecting and storing weather data. The workflow is defined in the [actions.yml](.github/workflows/actions.yml) file.

Here's a brief overview of the workflow steps:

- It sets up the required Python environment.
- Starts the specified version of MongoDB.
- Executes `main.py` to collect weather data.
- Executes `datamanager.py` to process and store the data.
- Commits any changes to the repository and pushes them to the main branch.

This automation ensures that the weather data is regularly updated and integrated into the project.

## Requirements

To run the project manually, you'll need the following dependencies:

- Python 3.9 or higher
- Pandas library
- MongoDB database
- WeatherAPI API key

You can install the requirements using the following command:

```
pip install -r requirements.txt
```

## Contributing

To contribute to the project, you can follow these steps:

1. Open or contribute to an existing issue.
2. Submit your code changes via a pull request.
3. Wait for the review process and make necessary updates if required.

## Raw Data Example

Here's an example of the raw weather data on MongoDB collected for a city:

```json
{
  "_id": "2023-09-10",
  "Data": {
    "Van": {
      "location": {
        "name": "Van",
        "region": "Van",
        "country": "Turkey",
        "lat": 38.49,
        "lon": 43.38,
        "tz_id": "Europe/Istanbul",
        "localtime_epoch": 1694294429,
        "localtime": "2023-09-10 0:20"
      },
      "current": {
        "last_updated_epoch": 1694294100,
        "last_updated": "2023-09-10 00:15",
        "temp_c": 19.0,
        "temp_f": 66.2,
        "is_day": 0,
        "condition": {
          "text": "Partly cloudy",
          "icon": "//cdn.weatherapi.com/weather/64x64/night/116.png",
          "code": 1003
        },
        "wind_mph": 6.9,
        "wind_kph": 11.2,
        "wind_degree": 200,
        "wind_dir": "SSW",
        "pressure_mb": 1016.0,
        "pressure_in": 30.0,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 46,
        "cloud": 25,
        "feelslike_c": 19.0,
        "feelslike_f": 66.2,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 1.0,
        "gust_mph": 7.6,
        "gust_kph": 12.2
      }
    }
  }
}
```

## Processed Data

Here is the processed weather data for some cities:

| City           | LocalTime        | Temperature_C | Wind_Speed_kph | Humidity | Condition |
| -------------- | ---------------- | ------------- | -------------- | -------- | --------- |
| Adana          | 2023-09-10 15:35 | 33.0          | 22.0           | 49       | Sunny     |
| Adiyaman       | 2023-09-10 15:35 | 31.3          | 23.4           | 11       | Sunny     |
| Afyonkarahisar | 2023-09-10 15:35 | 25.0          | 3.6            | 28       | Sunny     |
| Agri           | 2023-09-10 15:35 | 18.0          | 14.4           | 17       | Sunny     |
| Aksaray        | 2023-09-10 15:35 | 25.1          | 26.3           | 20       | Sunny     |

...
..
.
