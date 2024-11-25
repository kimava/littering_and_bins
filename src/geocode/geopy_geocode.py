from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="littering_and_bins")

def get_coordinates_from_geopy(address):
    location = geolocator.geocode(address, timeout=10)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None