import requests

def get_weather(city_name, api_key):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None
  return response.json()

def display_weather(weather_data):
  if not weather_data:
    return

  city = weather_data["name"]
  description = weather_data["weather"][0]["description"]
  temp_kelvin = weather_data["main"]["temp"]
  temp_celsius = round(temp_kelvin - 273.15, 2)

  print(f"Weather in {city}:")
  print(f"- Description: {description}")
  print(f"- Temperature: {temp_celsius:.2f} °C")

if __name__ == "__main__":
  api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
  city_name = input("Enter city name: ")

  weather_data = get_weather(city_name, api_key)
  display_weather(weather_data)

