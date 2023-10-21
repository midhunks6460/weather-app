from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = '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'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    weather_description = data['weather'][0]['description'].capitalize()
    temperature = data['main']['temp'] - 273.15  # Convert to Celsius
    return f"{weather_description}, {temperature:.2f}°C"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather_route():
    city = request.form['city']
    weather = get_weather(city)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
