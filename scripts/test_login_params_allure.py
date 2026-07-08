import logging
import json

import allure
import pytest

from api.hirm_auto_api import HirmLoginApi
from common.assert_login import assert_login
from common.log_common import init_log_config
from common.read_data import read_login_data
from config import BASE_DIR


# epic：报告中的一级业务分类，通常写项目或系统名称
@allure.epic("IHRM接口自动化")
# feature：报告中的二级功能分类，通常写被测模块名称
@allure.feature("登录模块")
class TestHirmLogin:
  # 初始化日志 
  init_log_config(BASE_DIR + '/log/hirm_login.log',interval=3,backupCount=7)
  # 读取登录接口参数化测试数据
  data = read_login_data(BASE_DIR + '/data/login.json')

  # story：报告中的三级功能点，通常写具体接口或业务场景
  @allure.story("登录接口参数化测试")
  # severity：用例严重级别，登录属于核心链路，这里设置为 critical
  @allure.severity(allure.severity_level.CRITICAL)
  # title：Allure报告中展示的用例标题，{desc} 会使用参数化数据中的 desc
  @allure.title("登录接口参数化用例：{desc}")
  # description：用例说明，会展示在 Allure 报告详情中
  @allure.description("校验登录接口在不同手机号、密码和参数组合下的响应状态码、业务码、success和message。")
  # ids：pytest参数化用例名称，让测试报告显示“登录成功”等中文场景名
  @pytest.mark.parametrize('desc,req_data,status_code,success,code,message',data,ids=[case[0] for case in data])
  def test_login_params(self,desc,req_data,status_code,success,code,message):
    # dynamic.title：运行时动态设置标题，确保每条参数化用例标题更清晰
    allure.dynamic.title(f"登录接口参数化用例：{desc}")
    # dynamic.tag：给用例增加标签，便于在 Allure 报告中筛选
    allure.dynamic.tag("login", "params", "api")

    # step：把测试过程拆成步骤，报告中可以清楚看到执行到哪一步
    with allure.step("准备登录接口请求数据"):
      # attach：把请求参数作为附件写入报告，失败时方便定位入参问题
      allure.attach(
        json.dumps(req_data, ensure_ascii=False, indent=2),
        name="请求参数",
        attachment_type=allure.attachment_type.JSON
      )

    with allure.step("发送登录接口请求"):
      resp = HirmLoginApi.hirm_login(req_data)
      resp_json = resp.json()
      # 记录接口响应日志，便于本地日志文件排查问题
      logging.info(f"{desc}: {resp_json}")
      # 把接口响应内容附加到 Allure 报告中
      allure.attach(
        json.dumps(resp_json, ensure_ascii=False, indent=2),
        name="响应结果",
        attachment_type=allure.attachment_type.JSON
      )

    with allure.step("断言登录接口响应"):
      # 把期望结果附加到报告中，方便和实际响应结果对比
      allure.attach(
        json.dumps(
          {
            "期望状态码": status_code,
            "期望success": success,
            "期望code": code,
            "期望message": message
          },
          ensure_ascii=False,
          indent=2
        ),
        name="期望结果",
        attachment_type=allure.attachment_type.JSON
      )
      # 调用公共断言方法，校验状态码、success、code 和 message
      assert_login(resp,status_code,success,code,message)

