import os
import time
import requests

while True:
    print("weather update")

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid={os.environ['OPENWEATHER_KEY']}&units=metric"

    data = requests.get(url).json()

    print(data["main"]["temp"])

    time.sleep(300)
