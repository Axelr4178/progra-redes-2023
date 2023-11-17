#AXEL ALEJANDRO ALMAGUER RODRIGUEZ
#GIR0541

import requests
import webbrowser
import json

try:
    # Solicitar la ubicación al usuario
    latitude = float(input("Ingrese la latitud: "))
    longitude = float(input("Ingrese la longitud: "))

    # Construir la URL de la API con la ubicación proporcionada por el usuario
    api_key = "wWHwADySE1tOvEWdoS0c0ZfVZxAX0U9k"
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}"

    response = requests.get(url)
    response.raise_for_status()

    # Obtener el valor de location del JSON
    data = response.json()
    minutely_timeline = data.get('timelines', {}).get('minutely', [])

    # Crear una página HTML con el resultado
    html_content = f"""
    <html>
        <head>
            <title>Resultado del Pronóstico Minuto a Minuto</title>
        </head>
        <body>
            <h1>Pronóstico Minuto a Minuto</h1>
    """

    if minutely_timeline:
        # Imprimir información reducida en la página HTML
        html_content += "<ul>"
        for minute_data in minutely_timeline:
            values = minute_data.get('values', {})
            temperature = values.get('temperature', '')

            html_content += f"<li>La temperatura es: {temperature}°C</li>"
        html_content += "</ul>"
    else:
        html_content += "<p>No se encontró información minutely en los datos.</p>"

    html_content += """
        </body>
    </html>
    """

    # Guardar la página HTML en un archivo temporal
    with open("weather_forecast.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    # Abrir la página HTML en el navegador
    webbrowser.open("weather_forecast.html")

except ValueError:
    print("Por favor, ingrese valores numéricos para la latitud y longitud.")
except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error en la solicitud: {err}")
except Exception as err:
    print(f"Error inesperado: {err}")
