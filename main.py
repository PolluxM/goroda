#по Модулую M10_L3
from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon{lng}"

            #if "state" in results[0]['components']:
                #region = results[0]['components']['state']
                return {"coordinates": f"Широта {lat}, Долгота {lng},\n Страна: {country}.\n Регион: {region}", "map_url": osm_url}
            else:
                return {"coordinates": f"Широта {lat}, Долгота {lng},\n Страна: {country}", "map_url": osm_url}

        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"

def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты горда {city}:\n {result['coordinates']}")
    map_url = result['map_url']

def show_map():
    if map_url:
        webbrowser.open(map_url)

key = '9b90a8325e184c319cdfbca0fde66855'
map_url = ''

window = Tk()
window.title("Координаты городов")
window.geometry("400x200")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите на кнопку")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

window.mainloop()