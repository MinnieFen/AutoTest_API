# -*- coding:utf-8 -*-
from public.get_config import Excel_data
from public.apimethod import Apimethod
from public.get_testdata import ReadExcel
import unittest
from ruamel import yaml
import os

class Logintest(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        self.filepath_now = os.path.abspath(os.path.join(os.getcwd(),'..'))
        self.filepath_config = self.filepath_now + '\config\config.xlsx'
        self.config_sheetname = 'urlconfig'
        self.config_data = Excel_data(self.filepath_config,self.config_sheetname).get_excel_data()
        self.url = self.config_data[0]['host'] + self.config_data[0]['url']
        self.method = self.config_data[0]['method']
        self.datapath_login = self.filepath_now + '\config\data_pwdlogin.xlsx'
        self.login_sheetname = 'logindata'
        self.params = ReadExcel(self.datapath_login,self.login_sheetname).readexceldata()

    def test_login_01(self):
        '''登录成功'''
        paramsdata1 = self.params[0]
        r = Apimethod(self.url,self.method,paramsdata1)
        req_result = r.apimethod()
        print(req_result)
        self.assertEqual(req_result['error'],'0')
        # print(req_result['data']['scode'])
        '''获取scode并存储scode值'''
        yamlpath = self.filepath_now + '\config\scode.yaml'
        scodevalue = {'scode':req_result['data']['scode']}
        with open(yamlpath,'w',encoding="utf-8") as f:
            yaml.dump(scodevalue,f,Dumper=yaml.RoundTripDumper)

    def test_login_02(self):
        '''登录失败'''
        paramsdata2 = self.params[1]
        r = Apimethod(self.url,self.method,paramsdata2)
        req_result = r.apimethod()
        self.assertEqual(req_result['error'],'PARAM_003')
        # print(req_result)

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()

# def test_login():
#     filepath_config = 'D:/appinstall/python3/test1/config/config.xlsx'
#     config_sheetname = 'login'
#     config_data = Excel_data(filepath_config,config_sheetname).get_excel_data()
#     url = config_data[0]['host'] + config_data[0]['url']
#     print(config_data)
#     # print(url)
#     method = config_data[0]['method']
#     datapath_login = 'D:/appinstall/python3/test1/testdata/data_pwdlogin.xlsx'
#     login_sheetname = 'logindata'
#     params = ReadExcel(datapath_login,login_sheetname).readexceldata()
#
#     req_rul_post = Apimethod(url,method,params)
#     req_result = req_rul_post.apimethod()
#     print(req_result)
#     return req_result
# test_login()