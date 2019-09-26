from ruamel import yaml
import os
import warnings
import ruamel

warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
def get_scode(yamlName = "scode.yaml"):
    """获取scode，方便其他接口使用"""
    file_path = os.path.abspath(os.path.join(os.getcwd(),'..'))+ '\config\scode.yaml'  #获取上一级目录，单独执行使用
    # file_path = os.path.abspath(os.path.join(os.getcwd()))+'\config\scode.yaml'    #获取当前目录，执行main使用
    with open(file_path,"r") as f:
        t = yaml.load(f)
    return t["scode"]

if __name__ == '__main__':
    get_scode()