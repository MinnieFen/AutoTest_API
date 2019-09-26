# -*- coding:utf-8 -*-
import requests
import json

class Apimethod(object):
    def __init__(self,url,method,data):
        self.url = url
        self.method = method
        self.data = data

    def apimethod(self):
        if self.method == 'post':
            r = requests.post(url = self.url,json=self.data)
            res = json.loads(r.text)
            print('     请求响应状态：%s' %r.status_code)
            return res

        if self.method == 'get':
            r = requests.get(url=self.url,params = self.data)
            res = json.loads(r.text)
            print('    请求响应状态：%s' %r.status_code)
            return res
# if __name__ == '__main__':
#     url = 'http://api2-t.yunxitech.cn/v1/pwdlogin'
#     method = 'post'
#     data = {'syscode': '03f37779cd022aa06f87eb92ad38ae3f', 'requestid': '20190812153517', 'version': '2.8.5(280)',
#             'sys_name': 'iOS', 'sys_version': '12.1.4', 'device_model': 'iPhone 6s', 'device_id': '3730b9f19de94764b25b501ef0149b40',
#             'device_name': 'iPhone', 'signature': 'fa2d3a6c8e', 'device_brand': 'Apple', 'device_product': 'iPhone', 'net_type': 'WIFI', 'phone': '18782038145 ','password': 'a123456'}
#     result = Apimethod(url,method,data)
#     resl = result.apimethod()