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

