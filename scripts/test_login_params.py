import pytest

from api.hirm_auto_api import HirmLoginApi
from common.assert_login import assert_login
from common.read_data import read_login_data
from config import BASE_DIR


class TestHirmLogin:
  data = read_login_data(BASE_DIR + '/data/login.json')
  @pytest.mark.parametrize('desc,req_data,status_code,success,code,message',data)
  def test_login_params(self,desc,req_data,status_code,success,code,message):
    # data = req_data
    resp = HirmLoginApi.hirm_login(req_data)
    print(desc + ':',resp.json())
    # 断言
    assert_login(resp,status_code,success,code,message)



