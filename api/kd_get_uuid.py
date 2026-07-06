import requests
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.get_uuid import get_uuid
# resp = requests.get(url='http://kdtx-test.itheima.net/api/captchaImage',
#                     headers={"User-Agent": "PostmanRuntime/7.39.0"})
# print(resp.json())

class KdGetUuidApi:
  @classmethod
  def kd_get_uuid(cls):
    resp = requests.get(url='http://kdtx-test.itheima.net/api/captchaImage',
                        headers={"User-Agent": "PostmanRuntime/7.39.0"})
    return resp
  

if __name__ == '__main__':
  resp = KdGetUuidApi.kd_get_uuid()
  print(resp.json())
  print(get_uuid(resp))
