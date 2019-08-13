# -*- coding:utf-8 -*-
import requests
import json
from public.get_config import Excel_data
from public.apimethod import Apimethod
from public.get_testdata import ReadExcel

def test_login():
    filepath_config = 'C:/Users/cmf/Desktop/test1/config/config.xlsx'
    config_sheetname = 'login'
    config_data = Excel_data(filepath_config,config_sheetname).get_excel_data()
    url = config_data[0]['host'] + config_data[0]['url']
    # print(config_data)
    # print(url)
    method = config_data[0]['method']
    datapath_login = 'C:/Users/cmf/Desktop/test1/testdata/data_pwdlogin.xlsx'
    login_sheetname = 'logindata'
    data = ReadExcel(datapath_login,login_sheetname).readexceldata()
    # print(data)
    if method == 'post':
        req_rul_post = Apimethod(url,method,data)
        req_result = req_rul_post.apimethod()
        return req_result

test_login()