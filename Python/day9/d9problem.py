# Use APIS

#  Pick any 3 of the below.

# 1. **Weather Data Retrieval:**
#    Write a program that fetches the current weather data for a specific city using a weather API.
#    - Utilize a weather API (such as OpenWeatherMap) to retrieve the current weather details (temperature, humidity, wind speed, etc.) for a user-input city.

# 2. **Currency Converter:**
#    Create a currency converter program using a currency exchange rate API.
#    - Use a currency exchange rate API (like Open Exchange Rates) to convert an amount from one currency to another based on user input.

# 3. **Fetching News Headlines:**
#    Develop a program that fetches the latest news headlines from a news API.
#    - Utilize a news API (such as NewsAPI) to retrieve the top headlines or articles for a specific category or from a particular source.

# 4. **Geolocation Information:**
#    Write a program that retrieves geolocation information using an IP geolocation API.
#    - Use an IP geolocation API (like ipstack or ipapi) to fetch geolocation details (country, city, latitude, longitude, etc.) based on a user's IP address.

# 5. **Public Transport Information:**
#    Create a program that fetches public transport details for a specific location using a transport API.
#    - Utilize a transport API (e.g., TransportAPI) to retrieve details such as train schedules, bus routes, or nearest stations for a user-input location.
			           	




# # fetches the current weather data for a specific city using a weather API.
# # OpenWeatherMap to retrieve the current weather details (temperature, humidity, wind speed, etc.)
# # for a user-input city.

# # import the request module to request the specific url
# # import json module 
# import requests, json

# # basic url for weather api
# basic_url = "http://api.openweathermap.org/data/2.5/weather?q="

# # get city name from user
# city_name = input("Enter City Name : ")

# # combain city name with url
# url = basic_url + city_name

# # request url and get weather data using requests module
# response_data = requests.get(url)

# # response data
# weather_data = response_data.json()

# print(response_data)

