from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Weather Server OK!"

@app.route("/weather")
def weather():
    key = os.environ["OPENWEATHER_KEY"]

    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid={key}&units=metric&lang=ja"
    ).json()

    return jsonify({
        "temp": round(data["main"]["temp"]),
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "clouds": data["clouds"]["all"],
        "weather_id": data["weather"][0]["id"],
        "weather": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
