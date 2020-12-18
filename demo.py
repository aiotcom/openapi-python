import requests
import json

url="https://protobuf.stepiot.com/api/operate"

data = {
    'token': 'eyJhbGciOiJIUzI1NiJ9.eyJncm91cEJybiI6IjEzMzk0NTIzNzc3OTIwNTMyNDkifQ.P7z47ML6hWAZaYytvs-lVS-X0H_vaMdTrAGDOEU7ZAQ',
    'action': 'turnOnLight'
}
## headers中添加上content-type这个参数，指定为json格式
headers = {'Content-Type': 'application/json'}
## post的时候，将data字典形式的参数用json包转换成json格式。
response = requests.post(url=url, headers=headers, data=json.dumps(data))
print(response.text)