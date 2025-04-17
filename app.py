from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = {}
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            api_key = os.getenv("WEATHER_API_KEY")
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                
                if data.get("main"):
                    weather = {
                        "city": data["name"],
                        "temp": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "description": data["weather"][0]["description"].capitalize(),
                        "icon_url": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                        "wind_speed": data["wind"]["speed"],
                        "pressure": data["main"]["pressure"]
                    }
                else:
                    error = "City not found. Please try another location."
            except requests.exceptions.RequestException as e:
                error = "Unable to connect to weather service. Please try again later."
    
    return render_template("index.html", weather=weather, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    