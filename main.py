# -*- coding:utf-8 -*-

import requests
import json

url = "http://api2-t.yunxitech.cn/v2/pwdlogin"
params = {"syscode":"03f37779cd022aa06f87eb92ad38ae3f","requestid":"20190812153517","version":"2.8.5(280)","sys_name":"iOS",
            "sys_version":"12.1.4","device_model":"iPhone 6s","device_id":"3730b9f19de94764b25b501ef0149b40","device_name":"iPhone","signature":"fa2d3a6c8e",
            "device_brand":"Apple","device_product":"iPhone","net_type":"WIFI","phone":"18782038145","password":"a123456"}
r = requests.post(url= url,params= params)
# res = json.loads(r.text)
print(r.status_code)

