
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests
import pandas as pd

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv("API_KEY")
df = pd.read_csv("fabric_data.csv")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return None
    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "desc": data["weather"][0]["description"]
    }

def recommend_fabrics(temp, humidity, activity):
    humidity_level = (
        "High" if humidity >= 60 else
        "Low" if humidity < 40 else
        "Moderate"
    )
    matches = []

    for _, row in df.iterrows():
        if (
            row["MinTemp"] <= temp <= row["MaxTemp"] and
            (row["HumidityLevel"] == humidity_level or row["HumidityLevel"] == "Any") and
            (activity.lower() in row["Activity"].lower())
        ):
            matches.append((row["Fabric"], row["Notes"]))
    return matches

@app.route("/", methods=["GET", "POST"])
def index():
    fabrics = []
    weather = {}
    if request.method == "POST":
        city = request.form["city"]
        activity = request.form["activity"]
        weather = get_weather(city)
        if weather:
            fabrics = recommend_fabrics(weather["temp"], weather["humidity"], activity)
    return render_template("index.html", fabrics=fabrics, weather=weather)

@app.route("/fabric-info", methods=["GET", "POST"])
def fabric_info():
    result = None
    if request.method == "POST":
        fabric_name = request.form["fabric_name"].strip().lower()
        for _, row in df.iterrows():
            if fabric_name == row["Fabric"].strip().lower():
                result = row.to_dict()
                break
    return render_template("fabric_info.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


# also pip install waitress pandas requests python-dotenv flask gunicorn
