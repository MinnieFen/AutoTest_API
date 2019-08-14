from ruamel import yaml
import os

def get_scode(yamlName = "scode.yaml"):
    """获取scode，方便其他接口使用"""
    p = os.path.join(r'D:/appinstall/python3/test1/config/scode.yaml')
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    # print(t["scode"])
    return t["scode"]
