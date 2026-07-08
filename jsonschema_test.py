# 导包
import jsonschema

# 创建校验规则
schema = {
    "type": "object",
    "properties": {
      "desc":{"type": "string"},
      "req_data": {
        "type": "object",
        "properties": {
          "mobile": {"const": "13800000002"},
          "password": {"type": "string","const": "929itheima.CN032@.20260707"}
        },
        "required": ["mobile", "password"]
      },
      "status_code": {"type": "integer", "const": 200},
      "success": {"type": "boolean", "const": True},
      "code": {"type": "integer", "const": 10000},
      "message": {"type": "string", "const": "操作成功！","pattern": "^操作成功！$"}
    },
    "required": ["desc", "req_data", "status_code", "success", "code", "message"]
}



# 准备待校验数据
data = {
    "desc": "登录成功",
    "req_data": {
      "mobile": "13800000002",
      "password": "929itheima.CN032@.20260707"
    },
    "status_code": 200,
    "success": True,
    "code": 10000,
    "message": "操作成功！"
  }
# 调用方法
res = jsonschema.validate(instance=data, schema=schema)
# 查看结果
print(res)  # None表示校验通过