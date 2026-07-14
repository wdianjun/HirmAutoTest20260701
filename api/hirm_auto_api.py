import requests
class HirmLoginApi:
  @classmethod
  def hirm_login(cls,json_data):
    resp = requests.post("https://ihrm-java.itheima.net/api/sys/login",
                         headers={
                           "User-Agent": "Mozilla/5.0",
                           "Accept": "application/json, text/plain, */*",
                           "Content-Type": "application/json;charset=UTF-8",
                           "Origin": "https://ihrm-java.itheima.net",
                           "Referer": "https://ihrm-java.itheima.net/"
                         },
                         json=json_data,
                         timeout=10)
    return resp



if __name__ == '__main__':
  json_data = {"mobile": "13800000002", "password": "929itheima.CN032@.20260714"}
  resp = HirmLoginApi.hirm_login(json_data)
  print(resp.json())
