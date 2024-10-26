#по Модулую M10_L3
from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return lat, lon
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"


key = '9b90a8325e184c319cdfbca0fde66855'
city = "Ryazan"
coordinates = get_coordinates(city, key)
print(f"Координаты гордо {city}: {coordinates}")