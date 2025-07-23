import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print("City not found. Please check the spelling.")
            return

        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
