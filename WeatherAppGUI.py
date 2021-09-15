#source code from Keith Gali (youtube/github)
import tkinter 
import requests
from tkinter import font
HEIGHT = 500
WIDTH = 600
# api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}
# e7eeee39bcb9c72b7fc40936b9053734
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'
	return final_str
def get_weather(city):
	weather_key = 'e7eeee39bcb9c72b7fc40936b9053734'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city,'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	label['text'] = format_response(weather)	
root = tkinter.Tk()
root.title("Weather App")
canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
frame = tkinter.Frame(root, bg='#f45b5b', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = tkinter.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
button = tkinter.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)
lower_frame = tkinter.Frame(root, bg='#fdf06d', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tkinter.Label(lower_frame, font=("Arial", 24))
label.place(relwidth=1, relheight=1)
root.mainloop()