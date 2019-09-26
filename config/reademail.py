# -*- coding:utf-8 -*-
import configparser
import os
cur_path = os.path.dirname(os.path.realpath(__file__))
cfg_path = os.path.join(cur_path,'email.ini')

# 调用读取配置模块中的类
conf = configparser.ConfigParser()
conf.read(cfg_path)

# 调用get方法，获取配置的数据
mail_host = conf.get('email','mail_host')
mail_pass = conf.get('email','mail_pass')
mail_user = conf.get('email','mail_user')
sender = conf.get('email','sender')
receivers = conf.get('email','receiver')


