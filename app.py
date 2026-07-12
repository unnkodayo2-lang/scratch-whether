from flask import Flask, jsonify
import requests
import scratchattach as scratch3
import os
import threading
import time

app = Flask(__name__)

session = scratch3.login(
    os.environ["SCRATCH_USERNAME"],
    os.environ["SCRATCH_PASSWORD"]
)

conn = session.connect_cloud("1352998508")

def update_weather():
    while True:
        try:
            key = os.environ["OPENWEATHER_KEY"]

            data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid={key}&units=metric&lang=ja",
                timeout=10
            ).json()

            conn.set_var("temp", round(data["main"]["temp"]))
            conn.set_var("humidity", data["main"]["humidity"])
            conn.set_var("wind", int(data["wind"]["speed"] * 100))
            conn.set_var("clouds", data["clouds"]["all"])
            conn.set_var("weather_id", data["weather"][0]["id"])

            print("更新成功！")

        except Exception as e:
            print("エラー:", e)

        time.sleep(300)   # 300秒 = 5分

@app.route("/")
def home():
    return "Weather Bot Running!"

@app.route("/weather")
def weather():
    return jsonify({"status": "running"})

# 更新スレッド開始
threading.Thread(target=update_weather, daemon=True).start()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
