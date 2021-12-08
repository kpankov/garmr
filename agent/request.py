import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/json"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"login":"my_login","password":"my_password"}'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)