from distutils.log import debug
from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")
def index():
    weather = weather_by_city('Ekaterinburg,Russia')
    if weather:
        return f"<h2>Погода: {weather['temp_C']}, ощущается как:  {weather['FeelsLikeC']}</h2>"
    else:
        return 'Сервис погоды временно недоступен :('

if __name__ == '__main__':
    app.run(debug=True) 