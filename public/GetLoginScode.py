# coding:utf-8
from public.GetExcelData import get_excel_data
import os
from public.Apimethod import Apimethod
from ruamel import yaml
import ruamel
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
class GetScode():
    def save_scode(self):
        self.filepath_now = os.path.abspath(os.path.join(os.getcwd(),'..'))   # 获取上一级路径，单独运行用例时用
        # self.filepath_now = os.path.abspath(os.path.join(os.getcwd()))     #获取当前路径，运行main时用
        self.config_sheetname = 'urlconfig'
        self.config_data = get_excel_data(self.config_sheetname)
        self.url = self.config_data[0]['host'] + self.config_data[0]['url']
        self.method = self.config_data[0]['method']
        self.login_sheetname = 'get_scode'
        self.params = get_excel_data(self.login_sheetname)
        paramsdata1 = self.params[0]
        r = Apimethod(self.url,self.method,paramsdata1)
        req_result = r.apimethod()
        '''获取scode并存储scode值'''
        yamlpath = self.filepath_now + '\public\scode.yaml'
        scodevalue = {'scode':req_result['data']['scode']}
        with open(yamlpath,'w',encoding="utf-8") as f:
            yaml.dump(scodevalue,f,Dumper=yaml.RoundTripDumper)
    def get_scode(self):
        self.save_scode()
        f = os.path.abspath(os.path.dirname(__file__))
        p = f + '\scode.yaml'
        f = open(p)
        value = f.read()
        scode = yaml.load(value)
        return scode
# if __name__ == '__main__':
#     t = GetScode()
#     t.get_scode()