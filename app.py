from flask import Flask
import requests
import scratchattach as scratch3
import os

app = Flask(__name__)

# Scratchログイン
session = scratch3.login(
    os.environ["SCRATCH_USERNAME"],
    os.environ["SCRATCH_PASSWORD"]
)

conn = session.connect_cloud("1352998508")

@app.route("/")
def home():
    return "Weather Server Running!"

@app.route("/update")
def update():

    key = os.environ["OPENWEATHER_KEY"]

    data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat=35.694&lon=139.983&appid={key}&units=metric",
    timeout=10
).json()

    temp = round(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    wind = int(data["wind"]["speed"] * 100)   # 0.89→89
    clouds = data["clouds"]["all"]
    weather_id = data["weather"][0]["id"]

    conn.set_var("temp", temp)
    conn.set_var("humidity", humidity)
    conn.set_var("wind", wind)
    conn.set_var("clouds", clouds)
    conn.set_var("weather_id", weather_id)

    return {
        "status": "ok",
        "temp": temp,
        "humidity": humidity,
        "wind": wind,
        "clouds": clouds,
        "weather_id": weather_id
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
