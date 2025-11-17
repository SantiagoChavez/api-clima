# api_clima.py

import requests

# Importamos render_template (para mostrar el HTML) y request (para leer el form)
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

        # URL de la API (ahora usa la clave del formulario)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={apiKey}&units=metric&lang=es"

        # print(f"Realizando consulta a: {url}")

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                error_msg = data.get(
                    "message", "Ciudad no encontrada o API Key incorrecta."
                )
                # Devolvemos la página con el mensaje de error
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

            # Devolvemos la página, pero esta vez con los datos del clima
            return render_template("index.html", data=resultado, error=None)

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
            error_msg = "Error de conexión con la API de OpenWeatherMap."
            return render_template("index.html", error=error_msg, data=None)

    # Si el método es GET (el usuario acaba de abrir la página)
    # Simplemente mostramos la página vacía
    return render_template("index.html", data=None, error=None)


# ----------------------------------------------------
# Ejecución de la Aplicación
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
