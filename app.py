import os
import requests

key = os.environ["OPENWEATHER_KEY"]

print("APIキー取得成功")

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q=Tokyo&appid={key}&units=metric"
)

print("APIアクセス中")

response = requests.get(url)

print("ステータス")
print(response.status_code)

print(response.text)
