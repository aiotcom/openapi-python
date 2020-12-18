# openapi-python
连接八城物联网平台Python代码样例

```
import requests
import json

url="https://protobuf.stepiot.com/api/operate"

data = {
    'token': '填入token',
    'action': '填入action'
}
## headers中添加上content-type这个参数，指定为json格式
headers = {'Content-Type': 'application/json'}
## post的时候，将data字典形式的参数用json包转换成json格式。
response = requests.post(url=url, headers=headers, data=json.dumps(data))
print(response.text)

```
