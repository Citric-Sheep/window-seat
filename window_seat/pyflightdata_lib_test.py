from pyflightdata import FlightData

f = FlightData()

#optional login
f.login(email="dan.checketts@protonmail.ch", password="iY%U@bxHBZvYu&L6V45")
flight_data = f.get_flight_for_date('P57045', '20220726')

print("here")

# page={2}&limit={3}&token={1}&timestamp={4}'
# FLT_BASE = 'https://api.flightradar24.com/common/v1/flight/list.json?query=p57045&fetchBy=flight

# https://api.flightradar24.com/common/v1/flight/list.json?query=p57045&fetchBy=flight

