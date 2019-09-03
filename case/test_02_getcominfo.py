# -*- coding:utf-8 -*-
from public.get_config import Excel_data
from public.get_testdata import ReadExcel
from public.get_scode import get_scode
from public.apimethod import Apimethod
import unittest
import os

class Testgetcominfo(unittest.TestCase):
    '''获取公司信息'''
    def setUp(self):
        # self.filepath_now = os.path.abspath(os.path.join(os.getcwd(),'..'))    # 获取上一级路径，单独运行用例时用
        self.filepath_now = os.path.abspath(os.path.join(os.getcwd()))   #获取当前路径，运行main时用
        self.filepath_config = self.filepath_now + '\config\config.xlsx'
        self.config_sheetname = 'urlconfig'
        self.config_data = Excel_data(self.filepath_config, self.config_sheetname).get_excel_data()
        self.url = self.config_data[1]['host'] + self.config_data[1]['url']
        # print(self.url)
        self.method = self.config_data[1]['method']
        self.datapath_getcominfo = self.filepath_now + '\config\data_params.xlsx'
        self.cominfo_sheetname = 'cominfodata'
        self.params = ReadExcel(self.datapath_getcominfo, self.cominfo_sheetname).read_excel_data()

    def tearDown(self):
        print('test done!')

    def test_getcominfo_01(self):
        paramsdata = self.params[0]
        # print(paramsdata)
        # paramsdata = paramsdata0.update({'scode':get_scode()})
        paramsdata['scode'] = get_scode()     # 将scode添加到字典参数中
        # print(paramsdata)
        r = Apimethod(self.url, self.method, paramsdata)
        req_result = r.apimethod()
        # print(req_result)
        self.assertEqual(req_result['error'],'0')

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Testgetcominfo("test_getcominfo_01"))
#     unittest.TextTestRunner().run(suite)

# def test_login():
#     hearder = {'Content-Type':'application/json','Accept':'*/*','User-Agent':'SaySeal/2.8.7 (cn.yunxitech.dev4; build:288; iOS 12.1.4) Alamofire/4.4.0',
#                'Accept-Language':'zh-Hans-CN;q=1.0','Content-Length':'174','Accept-Encoding':'gzip;q=1.0, compress;q=0.5','Connection':'keep-alive'}
#     data = {'syscode': '03f37779cd022aa06f87eb92ad38ae3f', 'requestid': '20190826162020', 'signature': 'ff519a4b81',
#      'id_user': '152553170441131776', 'scode': '9b840b5826c300eeddb09f45b1f08036','id_company':'150519369415526246'}
#     url = 'http://api2-t.yunxitech.cn/v1/getuserinfo'
#     res = requests.post(url= url,json=data)
#     r = res.json()
#     print(r)
#
# test_login()