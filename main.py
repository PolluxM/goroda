from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"


key = '9b90a8325e184c319cdfbca0fde66855'
city = "Moscow"
coordinates = get_coordinates(city, key)
print(f"Координаты гордо {city}: {coordinates}")