api_key = "9ecf351b0867ca23b2ba8f1883bbb335"

import requests
parameters = {
    "lon":12.496365,
    "lat":41.902782,
    "appid": api_key,
    "exclude":"current,minutely,daily",
}
response =requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
will_rain= False
weather_slice = data["hourly"][:12]
for hour in weather_slice:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")

# print(weather_slice)
# print(data["hourly"][0]["weather"][0]["id"])
