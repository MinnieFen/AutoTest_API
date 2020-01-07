# -*- coding:utf-8 -*-
from public.Apimethod import Apimethod
from public.GetExcelData import get_excel_data
import unittest

class TestLogin(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        self.config_data = get_excel_data('urlconfig')
        self.url = self.config_data[0]['host'] + self.config_data[0]['url']
        self.method = self.config_data[0]['method']
        self.params = get_excel_data('logindata')
    def tearDown(self):
        # print('test login done!')
        pass
    def test_login_01(self):
        '''登录成功'''
        r = Apimethod(self.url,self.method,self.params[0])
        req_result = r.apimethod()
        self.assertEqual(req_result['error'],'0')
    def test_login_02(self):
        '''登录失败'''
        r = Apimethod(self.url,self.method,self.params[1])
        req_result = r.apimethod()
        self.assertEqual(req_result['error'],'PARAM_003')
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
    # suite.addTest(TestLogin('test_login_02'))
    # suite.addTest(TestLogin("test_login_01"))
    # unittest.TextTestRunner().run(suite)



# def test_login():
#     filepath_config = 'D:/appinstall/python3/test1/config/config.xlsx'
#     config_sheetname = 'login'
#     config_data = Excel_data(filepath_config,config_sheetname).get_excel_data()
#     url = config_data[0]['host'] + config_data[0]['url']
#     print(config_data)
#     # print(url)
#     method = config_data[0]['method']
#     datapath_login = 'D:/appinstall/python3/test1/TestData/data_pwdlogin.xlsx'
#     login_sheetname = 'logindata'
#     params = ReadExcel(datapath_login,login_sheetname).readexceldata()
#
#     req_rul_post = Apimethod(url,method,params)
#     req_result = req_rul_post.apimethod()
#     print(req_result)
#     return req_result
# test_login()