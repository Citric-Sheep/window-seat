from flightradar24.api import FlightRadar24API

fr_api = FlightRadar24API()
airports = fr_api.get_airports()
airlines = fr_api.get_airlines()


flights = fr_api.get_flights(airline="RPB")
interested = flights[0]
flight_details = fr_api.get_flight_details(interested.id)


img_flight = '2ccf01ac'
next_flight = '2ce08df2'

img_flight_details = fr_api.get_flight_details(img_flight)
next_flight_details = fr_api.get_flight_details(next_flight)


print("DOne")