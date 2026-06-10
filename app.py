import os
import requests

key = os.environ["OPENWEATHER_KEY"]

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q=Tokyo&appid={key}&units=metric&lang=ja"
)

data = requests.get(url).json()

print("気温")
print(data["main"]["temp"])

print("天気")
print(data["weather"][0]["description"])
