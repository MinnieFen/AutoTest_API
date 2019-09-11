# -*- coding:utf-8 -*-
import configparser
import os
cur_path = os.path.dirname(os.path.realpath(__file__))
cfg_path = os.path.join(cur_path,'email.ini')

conf = configparser.ConfigParser()
conf.read(cfg_path)

mail_host = conf.get('email','mail_host')
mail_pass = conf.get('email','mail_pass')
mail_user = conf.get('email','mail_user')
sender = conf.get('email','sender')
receiver = conf.get('email','receiver')
print(receiver)

