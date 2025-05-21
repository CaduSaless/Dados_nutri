import requests

var = requests.get(url=f'http://10.6.84.22:5000/api/ler_webcam')
print(var.json())