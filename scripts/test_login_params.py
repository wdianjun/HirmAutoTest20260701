import logging

import pytest

from api.hirm_auto_api import HirmLoginApi
from common.assert_login import assert_login
from common.log_common import init_log_config
from common.read_data import read_login_data
from config import BASE_DIR


class TestHirmLogin:
  # 初始化日志 
  init_log_config(BASE_DIR + '/log/hirm_login.log',interval=3,backupCount=7)
  data = read_login_data(BASE_DIR + '/data/login.json')
  @pytest.mark.parametrize('desc,req_data,status_code,success,code,message',data)
  def test_login_params(self,desc,req_data,status_code,success,code,message):
    # data = req_data
    resp = HirmLoginApi.hirm_login(req_data)
    # 打印日志
    logging.info(f"{desc}: {resp.json()}")
    # print(desc + ':',resp.json())
    # 断言
    assert_login(resp,status_code,success,code,message)



