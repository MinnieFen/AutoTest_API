# -*- coding:utf-8 -*-
from public.get_config import Excel_data
from public.get_testdata import ReadExcel
from public.get_scode import get_scode
from public.apimethod import Apimethod
import unittest
import os

class Testgetcominfo(unittest.TestCase):
    def setUp(self):
        self.filepath_now = os.path.abspath(os.path.join(os.getcwd()))
        self.filepath_config = self.filepath_now + '\config\config.xlsx'
        self.config_sheetname = 'urlconfig'
        self.config_data = Excel_data(self.filepath_config, self.config_sheetname).get_excel_data()
        self.url = self.config_data[1]['host'] + self.config_data[1]['url']
        self.method = self.config_data[1]['method']
        self.datapath_getcominfo = self.filepath_now + '\config\data_params.xlsx'
        self.cominfo_sheetname = 'cominfodata'
        self.params = ReadExcel(self.datapath_getcominfo, self.cominfo_sheetname).read_excel_data()
        # paramsdata0 = self.params[0]
        # paramsdata = paramsdata0.update({'scode': get_scode()})
        # print(paramsdata)

    def test_getcominfo_01(self):
        paramsdata = self.params[0]
        print(paramsdata)
        # paramsdata = paramsdata0.update({'scode':get_scode()})
        paramsdata['scode'] = get_scode()
        print(paramsdata)
        r = Apimethod(self.url, self.method, paramsdata)
        req_result = r.apimethod()
        print(req_result)
        self.assertEqual(req_result['error'],'0')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Testgetcominfo("test_getcominfo_01"))
    unittest.TextTestRunner().run(suite)