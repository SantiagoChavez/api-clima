import webbrowser
from threading import Timer
import requests
from flask import Flask, jsonify, render_template, request

# ----------------------------------------------------
# Configuración de Flask
# ----------------------------------------------------
app = Flask(__name__)


# ----------------------------------------------------
# Ruta principal (GET para mostrar, POST para procesar)
# ----------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    # Si el método es POST (el usuario envió el formulario)
    if request.method == "POST":
        # Leemos los datos del formulario
        apiKey = request.form.get("api_key")
        ciudad = request.form.get("ciudad")

        if not apiKey or not ciudad:
            error_msg = "Ambos campos (API Key y Ciudad) son obligatorios."
            return render_template("index.html", error=error_msg, data=None)

        # URL de la API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={apiKey}&units=metric&lang=es"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                error_msg = data.get(
                    "message", "Ciudad no encontrada o API Key incorrecta."
                )
                return render_template("index.html", error=error_msg, data=None)

            # Armamos el JSON con los datos que queremos
            resultado = {
                "ciudad": data.get("name"),
                "pais": data.get("sys", {}).get("country"),
                "temperatura": f"{data.get('main', {}).get('temp')} °C",
                "sensacion_termica": f"{data.get('main', {}).get('feels_like')} °C",
                "humedad": f"{data.get('main', {}).get('humidity')}%",
                "clima": data.get("weather", [{}])[0]
                .get("description", "")
                .capitalize(),
            }

            # Devolvemos la página con los datos del clima
            return render_template("index.html", data=resultado, error=None)

        except requests.exceptions.RequestException as e:
            # print(f"Error de conexión: {e}") # Comentado para evitar error de consola
            error_msg = "Error de conexión con la API de OpenWeatherMap."
            return render_template("index.html", error=error_msg, data=None)

    # Si el método es GET (el usuario acaba de abrir la página)
    return render_template("index.html", data=None, error=None)


# ----------------------------------------------------
# Ejecución de la Aplicación
# ----------------------------------------------------


def open_browser():
    # Abre el navegador en la dirección local
    webbrowser.open_new("http://127.0.0.1:5000/")


if __name__ == "__main__":
    # Programa que el navegador se abra 1 segundo después de iniciar el servidor
    Timer(1, open_browser).start()

    # IMPORTANTE: debug=False es obligatorio para crear el .exe sin errores
    app.run(debug=False, port=5000)
