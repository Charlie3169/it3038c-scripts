import requests

r = requests.get('http://localhost:3000')
jsonData = r.json()

for i in range(len(jsonData)):    
    name = jsonData[i]['name']
    color = jsonData[i]['color']
    print(f'{name} is {color}.')

