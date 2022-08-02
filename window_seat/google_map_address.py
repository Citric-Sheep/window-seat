# Will take in a latitude and longitude and return the Google Maps link for the address
# https://www.google.com/maps/@41.6771878,-83.622739,15z

base_url = "https://www.google.com/maps/@"


def get_address(latitude, longitude):
    return base_url + str(latitude) + "," + str(longitude) + ",15z"

