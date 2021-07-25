import requests

json_data = requests.get('http://www.floatrates.com/daily/idr.json')

print(json_data.json())
