import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'name':72911, 'vehicleType':4, 'yearOfRegistration':2001, 'gearbox':1, 'powerPS':75, 'model':118, 'kilometer':150000, 'monthOfRegistration':6, 'fuelType':1, 'brand':38, 'notRepairedDamage':1})

print(r.json())
