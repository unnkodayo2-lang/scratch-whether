from flask import Flask
import requests
import os
import scratchattach as scratch3

app = Flask(__name__)

# Scratchログイン
session = scratch3.login(
    os.environ["SCRATCH_USERNAME"],
    os.environ["SCRATCH_PASSWORD"]
)

print("ログイン成功")

# クラウド接続
conn = session.connect_cloud("1352998508")

print("クラウド接続成功")

# OpenWeather APIキー
API_KEY = os.environ["OPENWEATHER_KEY"]


@app.route("/")
def home():
    return "Scratch Weather Server is Running!"


@app.route("/update")
def update():

    # 船橋市
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat=35.694&lon=139.983"
        f"&appid={API_KEY}"
        f"&units=metric"
        f"&lang=ja"
    )

    data = requests.get(url, timeout=10).json()

    # データ取得
    temp = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = int(data["wind"]["speed"] * 100)
    clouds = data["clouds"]["all"]
    weather_id = data["weather"][0]["id"]

    # Scratchクラウド変数更新
    conn.set_var("temp", temp)
    conn.set_var("feels_like", feels_like)
    conn.set_var("humidity", humidity)
    conn.set_var("pressure", pressure)
    conn.set_var("wind", wind)
    conn.set_var("clouds", clouds)
    conn.set_var("weather_id", weather_id)

    print("更新成功")

    return {
        "status": "ok",
        "temp": temp,
        "feels_like": feels_like,
        "humidity": humidity,
        "pressure": pressure,
        "wind": wind,
        "clouds": clouds,
        "weather_id": weather_id
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
