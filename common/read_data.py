import json

from config import BASE_DIR


def read_login_data(filename):
    """
    读取登录接口测试数据
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as f:
        login_list = []
        data = json.load(f)
        for d in data:
            # d.pop('desc')
            # res = tuple(d.values())[1:]
            res = tuple(d.values())
            login_list.append(res)
            # print(login_list)
        return login_list



if __name__ == '__main__':
    filename = BASE_DIR + '/data/login.json'
    read_login_data(filename)
        
            
