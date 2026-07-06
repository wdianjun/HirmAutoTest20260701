def assert_login(resp,status_code,success,code,message):
    """
    断言登录接口
    :param resp: 登录接口响应对象
    :return:
    """
    assert status_code == resp.status_code
    assert success == resp.json().get("success")
    assert code == resp.json().get("code")
    assert message in resp.json().get("message")