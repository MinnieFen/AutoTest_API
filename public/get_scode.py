from ruamel import yaml
import os
import warnings
import ruamel

warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
def get_scode(yamlName = "scode.yaml"):
    """获取scode，方便其他接口使用"""
    # p = os.path.join(os.path.abspath + 'config/scode.yaml')
    # f = os.path.abspath(os.path.join(os.getcwd(),'..'))   #获取上一级目录，单独执行使用
    f = os.path.abspath(os.path.join(os.getcwd()))    #获取当前目录，执行main使用
    p = f + '\config\scode.yaml'
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    # print(t["scode"])
    return t["scode"]

# if __name__ == '__main__':
#     get_scode()