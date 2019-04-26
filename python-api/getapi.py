# coding: utf-8
import json
import requests

#-*- coding: utf-8 -*-

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
# Print the status code of the response.
print('200 is the response')
print(response.status_code)
print(response.content)
print(response.content.decode("utf-8"))

response = requests.get("http://api.open-notify.org/iss-pass")
print('404 — the resource you tried to access wasn’t found on the server.')
print(response.status_code)
print(response.content)

response = requests.get("http://api.open-notify.org/iss-pass.json")
print('This can happen when you don’t send along the right data, among other things')
print(response.status_code)
print(response.content)



# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
print('Skipping line for parameters')
parameters = {"lat": 40.71, "lon": -74}
# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# Print the content of the response (the data the server returned)
print(response.content)
# This gets the same data as the command aboveresponse = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content.decode("utf-8"))


print("sending latitude of 37 and longitude of -122")
# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)


print('This is a separate line \n ')
# Headers is a dictionary
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["content-type"])


print('Finding the number of people in space \n')
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space.
print(data["number"])
print(data)
