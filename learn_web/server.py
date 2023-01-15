from distutils.log import debug
from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")
def index():
    page_title = 'Прогноз погоды'
    weather = weather_by_city('Ekaterinburg,Russia')
    if weather:
        weather_text = f"Погода: {weather['temp_C']}, ощущается как:  {weather['FeelsLikeC']}"
    else:
        weather_text = 'Сервис погоды временно недоступен :('
    return render_template("index.html", page_title=page_title, weather_text=weather_text)

if __name__ == '__main__':
    app.run(debug=True) 