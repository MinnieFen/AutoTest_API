# -*- coding:utf-8 -*-
class global_var:
    id = '0'
    name = '1'
    run = '2'
    url = '3'
    method = '4'
    data = '5'
    case_depend = '6'
    except_result = '7'
    real_result = '8'
#获取id
def get_id():
    return global_var.id
#获取名称
def get_name():
    return global_var.name
#获取是否运行
def get_run():
    return global_var.run
#获取url
def get_url():
    return global_var.url
#获取请求方式
def get_method():
    return global_var.method
#获取参数
def get_data():
    return global_var.data
#获取case是否依赖
def get_case_depend():
    return global_var.case_depend
#获取期望结果
def get_except_result():
    return global_var.except_result
#获取实际结果
def get_real_result():
    return global_var.real_result