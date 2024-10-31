import requests
import json

lat = 60
lon = 21
API_key = '53629cd97d95a4b8591741d1fb9c9809'
part = 'minutely,hourly'
request_url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={API_key}"

try:
    response = requests.get(request_url)
    response.raise_for_status()

    weather = response.json()
    print("Response JSON:", json.dumps(weather, indent=2))

    if 'current' in weather:
        print(f"""
        Location: Latitude {lat}, Longitude {lon}
        Temperature: {weather['current']['temp']}°C
        Weather: {weather['current']['weather'][0]['description']}
        """)
    else:
        print("The 'current' key is missing from the response.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server. Check your internet connection.")
except requests.exceptions.Timeout:
    print("Error: The request timed out. Try again later.")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
except KeyError as e:
    print(f"Unexpected response format. Missing key: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
