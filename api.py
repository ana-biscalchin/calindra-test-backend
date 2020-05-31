import googlemaps

gmaps = googlemaps.Client(key="AIzaSyBcLiSKnbHAeN0t4uFp9aHeEc1Aaa8TFi0")


def geocoding_adress(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result
