Consulta de Clima con Flask 🌦️

Aplicación de escritorio y web desarrollada en Python que permite consultar el clima en tiempo real utilizando la API de OpenWeatherMap.

El proyecto ha evolucionado de un script simple a una aplicación completa que se ejecuta en el navegador y puede compilarse como un ejecutable de Windows (.exe).

🚀 Características

Interfaz Gráfica Web: Formulario amigable en HTML/CSS (ya no usa consola).

Modo Aplicación: Al iniciar, abre automáticamente tu navegador predeterminado.

Portátil: Soporte para convertir en .exe (no requiere Python instalado en la PC del usuario final).

Datos en Tiempo Real: Temperatura, sensación térmica, humedad y descripción del clima.

Validaciones: Manejo de errores para ciudades inexistentes o claves de API erróneas.

🛠️ Tecnologías Usadas

Python 3.13+

Flask: Backend web ligero.

HTML5 & CSS3: Frontend.

Requests: Consumo de API.

PyInstaller: Para generar el ejecutable de Windows.

Webbrowser & Threading: Para la automatización del inicio.

⚙️ Instalación y Ejecución (Modo Desarrollador)

Si quieres ver el código o modificarlo, sigue estos pasos:

Clonar el repositorio:

git clone [https://github.com/SantiagoChavez/api-clima.git](https://github.com/SantiagoChavez/api-clima.git)
cd api-clima


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

python api_clima.py


El navegador se abrirá automáticamente en http://127.0.0.1:5000/

📦 Crear el Ejecutable (.exe)

Para convertir este proyecto en un archivo .exe único que puedas compartir con amigos (sin que ellos instalen Python), usa PyInstaller:

Instalar PyInstaller (si no lo tienes):

pip install pyinstaller


Generar el ejecutable:
Ejecuta este comando en tu terminal (asegúrate de estar en la carpeta del proyecto):

pyinstaller --name="ClimaApp" --onefile --add-data "templates;templates" api_clima.py


Listo: Encontrarás tu aplicación en la carpeta dist/ClimaApp.exe.

📝 Notas

Necesitas una API Key gratuita de OpenWeatherMap para usar la aplicación.

La carpeta dist/ y build/ están ignoradas en el repositorio para mantenerlo limpio.