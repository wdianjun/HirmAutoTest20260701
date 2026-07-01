import requests
class HirmLoginApi:
  @classmethod
  def hirm_login(cls,json_data):
    resp = requests.post("https://hirm.cn.com/login/login",
                         headers={"User-Agent": "PostmanRuntime/7.39.0"},
                         json=json_data)
    print(resp.json())



if __name__ == '__main__':
  json_data = {"mobile": "13800000002", "password": "929itheima.CN032@.20260701"}
  HirmLoginApi.hirm_login(json_data)