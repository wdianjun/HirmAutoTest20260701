
from api.hirm_auto_api import HirmLoginApi


class TestHirmLogin:
  def test_login01(self):
    data = {"mobile": "13800000002", "password": "929itheima.CN032@.20260706"}
    resp = HirmLoginApi.hirm_login(data)
    print("登录成功：",resp.json())
    # 断言
    assert 200 == resp.status_code
    assert True == resp.json().get("success")
    assert 10000 == resp.json().get("code")
    assert "操作成功" in resp.json().get("message")


  def test_login02(self):
    data = {"mobile": "13800000001", "password": "929itheima.CN032@.20260706"}
    resp = HirmLoginApi.hirm_login(data)
    print("手机号未注册：",resp.json())
    assert 200 == resp.status_code
    assert False == resp.json().get("success")
    assert 20001 == resp.json().get("code")
    assert "用户名或密码错误" in resp.json().get("message")



