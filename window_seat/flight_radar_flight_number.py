import requests

from flightradar24.api import FlightRadar24API

api = FlightRadar24API()
login = api.login(user="dan.checketts@protonmail.ch", password="iY%U@bxHBZvYu&L6V45")
flights = api.get_flights(flight="p57045")



resp = requests.get("https://www.flightradar24.com/v1/search/web/find?query=p57045&limit=18&type=schedule")
print(resp.content)

print("here")

# id=\"btn-playback-2ccf01ac\"

# ref="/data/flights/p57045#2ce72729"
