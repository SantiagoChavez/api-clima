# Consulta de Clima con Flask 🌦️

Aplicación web simple desarrollada en Python y Flask que permite a los usuarios consultar el clima actual de cualquier ciudad utilizando la API de OpenWeatherMap.

## 🚀 Características

* **Interfaz Limpia:** Un formulario simple para ingresar la ciudad y la API key.
* **Consulta en Tiempo Real:** Llama directamente a la API de OpenWeatherMap.
* **Resultados Claros:** Muestra la temperatura, sensación térmica, humedad y descripción del clima.
* **Manejo de Errores:** Informa al usuario si la API key es incorrecta o la ciudad no se encuentra.

## 🛠️ Tecnologías Usadas

* **Python**
* **Flask:** Como micro-framework web para el backend.
* **Requests:** Para realizar las consultas (peticiones HTTP) a la API externa.
* **HTML & CSS:** Para la interfaz de usuario (frontend).

## ⚙️ Cómo Ejecutar el Proyecto

Sigue estos pasos para correr el proyecto en tu máquina local.

### 1. Prerrequisitos

* Tener Python 3 instalado.
* Tener una **API key** de OpenWeatherMap. Puedes conseguir una gratis [registrándote aquí](https://openweathermap.org/appid).

### 2. Instalación

1.  Clona este repositorio (suponiendo que tu repo se llame `api-clima`):
    ```bash
    git clone [https://github.com/SantiagoChavez/api-clima.git](https://github.com/SantiagoChavez/api-clima.git)
    cd api-clima
    ```

2.  (Opcional pero recomendado) Crea un entorno virtual:
    ```bash
    # En Windows
    python -m venv venv
    venv\Scripts\activate
    
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
    *(Asegúrate de haber creado el archivo `requirements.txt` con `pip freeze > requirements.txt`)*

### 3. Ejecución

1.  Corre el servidor de Flask:
    ```bash
    python api_clima.py
    ```

2.  Abre tu navegador y ve a la siguiente dirección:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

3.  ¡Listo! Ingresa tu API key de OpenWeatherMap y el nombre de una ciudad para ver el clima.