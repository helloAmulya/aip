#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import sys, requests, pprint, os

API_KEY = os.getenv("WEATHER_API")


if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()

location = " ".join(sys.argv[1:])

url = "https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s" % (
    location,
    API_KEY,
)
response = requests.get(url)
response.raise_for_status()

# weatherData = json.loads(response.text)
weatherData = response.json()
pprint.pprint(weatherData)  # this will print the json data


print("Current weather in %s:" % location)
print(weatherData["weather"][0]["main"], "-", weatherData["weather"][0]["description"])
print("Temperature:", weatherData["main"]["temp"], "K")

{
    "coord": {"lon": 80.9167, "lat": 26.85},
    "weather": [
        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}
    ],
    "base": "stations",
    "main": {
        "temp": 298.88,
        "feels_like": 299.15,
        "temp_min": 298.88,
        "temp_max": 298.88,
        "pressure": 1010,
        "humidity": 63,
        "sea_level": 1010,
        "grnd_level": 996,
    },
    "visibility": 10000,
    "wind": {"speed": 1.34, "deg": 350, "gust": 1.47},
    "clouds": {"all": 0},
    "dt": 1792760643,
    "sys": {"country": "IN", "sunrise": 1792715998, "sunset": 1792756870},
    "timezone": 19800,
    "id": 1264733,
    "name": "Lucknow",
    "cod": 200,
}
