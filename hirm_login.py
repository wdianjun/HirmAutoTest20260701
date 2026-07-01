import requests

resp = requests.post(url='http://ihrm-java.itheima.net/api/sys/login',
                     headers={"User-Agent": "PostmanRuntime/7.39.0"},
                      json={"mobile": "13800000002", "password": "929itheima.CN032@.20260701"}
                     )
print(resp.json())
