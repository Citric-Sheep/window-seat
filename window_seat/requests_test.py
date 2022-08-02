from datetime import datetime, timedelta

from flightradar24.api import FlightRadar24API

api = FlightRadar24API()
result = api.login(user="dan.checketts@protonmail.ch", password="iY%U@bxHBZvYu&L6V45")

requested_time = datetime.fromtimestamp(1659225600)
low_date = requested_time - timedelta(days=1)
high_date = requested_time + timedelta(days=1)

# low_date = 1658793600 - 43200
# high_date = 1658793600 + 43200

print(f"Requested time: {requested_time}")


flight_id = None
flights = api.get_flight_list(flight='p57045')
for fdata in flights:
    expected_departure = fdata['time']['scheduled']['departure']
    dt_expected = datetime.fromtimestamp(expected_departure)

    if low_date < dt_expected < high_date:
        flight_id = fdata['identification']['id']
        break

if flight_id is None:
    raise Exception("Flight on the given date not found")

playback = api.get_flight_playback(flight_id)
# {'id': '2ce08df2', 'row': 5248255998, 'number': {'default': 'P57045', 'alternative': None}, 'callsign': 'RPB7045', 'codeshare': None}
print("herer")