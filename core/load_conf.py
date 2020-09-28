import json

conf_json = {
    "name": "py_zinx",
    "ip_version": "tcp4",
    "ip": "0.0.0.0",
    "port": 8888,
}
try:
    # 加载配置文件
    file = open("../demo/conf.json", "r")
    conf_json = json.load(file)
except Exception as e:
    print(e)
    pass
