"""-----What will I learn in this project-----
- 1. What is an API?
- 2. How APIs Work
- 3. Using API Keys
- 4. Fetching Data from APls using requests
- 5. Project 19: Weather App using API
"""

# %% 1. What is an API?
# An API (Application Programming Interface) is a set of rules and tools that allow different software applications to communicate with each other.
# APIs enable developers to fetch data, send data, and interact with external services.
# Examples include retrieving weather data, financial market information, and more.
# 
# Example: Fetching weather data.
# You send a request for weather data, and then there is a response—the data returned by the API.
# When you make a request, you receive a response from the API.
# 
# The API endpoint is a specific URL that provides access to an API function.
# Additionally, an API key is a unique identifier required to access the API securely.
# 
# Typically, an API request consists of:
# - An **endpoint** (a URL that grants access to an API function).
# - An **API key** (which identifies the user and authorizes access).
# - The **request** (the action performed to retrieve or send data).
# 
# When you send a request to the API endpoint, you include an API key to let the server know who you are and why you are calling that endpoint.
# Based on the request, the API returns a response with the requested data.

# %% 2. How to API work 
"""
https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY
"""

# %% 3. Using API Keys

API_KEY = "5daffc5211149c934a96a128f9f015f7"

# %% 4. Fetching Data from APls using requests
import requests

API_KEY = "5daffc5211149c934a96a128f9f015f7"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
  weather_data = response.json()
  print(weather_data)
else:
    print("An error occurred. Status Code: ", response.status_code)

#%% 5. Weather App using OpenWeatherMap API
import requests

#Step 1: API SETUP
API_KEY = "5daffc5211149c934a96a128f9f015f7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 2: Get Weather Data
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}C",
                "Weather": data["weather"][0]['description'].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']}m/s"
            }
            return weather
        elif response.status_code == 404:
            print("City not found.")
        else:
            print("An error occurred. Status Code: ", response.status_code)
    except Exception as e:
        print("An error occurred: ", e)
    return None

# Step 3: Display Weather Information
def display_weather(weather):
    print("\n--- Weather Information ---")
    for key,value in weather.items():
        print(f"{key}: {value}")

# Step 4: Main Program Loop
while True:
    print("\n--- Weather App ---")
    city = input("Enter a city name (or 'q' to quit): ").strip()
    if city.lower() == 'q':
        break
    weather = get_weather(city)
    if weather:
        display_weather(weather)
# %%
