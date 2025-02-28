import requests

API_KEY = "780e83d9b0d6386358339f8794332bc4"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Weather data not available"
    
    data = response.json()
    return f"🌡️ Temperature: {data['main']['temp']}°C, {data['weather'][0]['description']}"
