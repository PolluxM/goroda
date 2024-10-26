#Открываем карту в браузере
from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')

        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components'].get('country', 'Страна не определена')
            region = results[0]['components'].get('state', 'Регион не определен')

            # Получаем URL для OpenStreetMap
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            return {
                "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион: {region}",
                "map_url": osm_url
            }
        else:
            return {"coordinates": "Город не найден", "map_url": None}
    except Exception as e:
        return {"coordinates": f"Ошибка: {e}", "map_url": None}

def show_coordinates(event=None):
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=result["coordinates"])
    # Сохраняем URL в глобальной переменной для доступа из другой функции
    global map_url
    map_url = result["map_url"]

def show_map():
    if map_url:
        webbrowser.open(map_url)

# Интерфейс
window = Tk()
window.title("Поиск координат города")
window.geometry("400x200")

key = '9b90a8325e184c319cdfbca0fde66855'
map_url = None

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

# Запуск приложения
window.mainloop()



