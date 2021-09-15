from geolite2 import geolite2
reader = geolite2.reader()
location = reader.get('73.43.205.153')
data = {"continent": location["continent"]["names"]["en"], 
"country": location["country"]["names"]["en"], "state": location["subdivisions"][0]["names"]["en"],
"city": location["city"]["names"]["en"], "postal": location["postal"]["code"]}
for key, value in data.items():
    print(f'{key}: {value}')