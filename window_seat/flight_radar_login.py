from flightradar24.api import FlightRadar24API
import json
api = FlightRadar24API()
result = api.login(user="dan.checketts@protonmail.ch", password="iY%U@bxHBZvYu&L6V45")

# flights = api.get_flights(flight="P57045")
flights = api.get_flights(airline="RPB")

# img_flight = '2ccf01ac'
img_flight = '2ce08df2'
img_flight_details = api.get_flight_details(img_flight)

playback = api.get_flight_playback(img_flight)

print('Herer')
