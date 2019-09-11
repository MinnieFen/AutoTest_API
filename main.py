# -*- coding:utf-8 -*-
import unittest
import os
from case.test_01_login import TestLogin
from case.test_02_getcominfo import Testgetcominfo
import time
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from config import reademail
from email.header import Header

cur_path = os.path.dirname(os.path.realpath(__file__))   #获取脚本的真实路径
def add_case(caseName = 'case',rule = 'test*.py'):
    '''第一步：加载所有测试用例'''
    case_path = os.path.join(cur_path,caseName)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case,reportName = 'report'):
    '''第二步：执行所有的用例，并把结果写进HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now + 'result.html')
    print('report path:%s' %report_abspath)
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'自动化测试报告，测试结果：',description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)     #列出report_path 路径下所有文件，结果以列表形式返回
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))   #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file
def send_email(mail_host,mail_pass,mail_user,sender,receiver,new_file):
    '''第四步：发送邮件'''
    f = open(new_file,'rb')
    mail_body = f.read()
    f.close()
    # mail_host = "smtp.qq.com"
    # mail_user = '517110453@qq.com'
    # mail_pass = 'swtpziuailjucafi'
    # sender = '517110453@qq.com'
    # receiver = '437889925@qq.com,chenmingfen@yunxitech.cn'
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = u'自动定时发送测试报告'
    msg['From'] = '517110453@qq.com'
    msg['To'] = '437889925@qq.com'
    smtp = smtplib.SMTP(mail_host,25)     # 创建SMTP对象
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receiver,msg.as_string())    #SMTP对象使用sendmail方法发送邮件
    smtp.quit()
    # print('test report email has send out !')
    # try:
    #     smtp = smtplib.SMTP()
    #     smtp.connect(mail_host,25)
    #     smtp.login(mail_user,mail_pass)
    #     smtp.sendmail(sender,receiver,msg.as_string())
    #     print('邮件发送成功')
    # except smtplib.SMTPException:
    #     print('Error:无法发送邮件')


    # smtpserver = "smtp.qq.com"
    # sender = '517110453@qq.com'
    # psw = 'swtpziuailjucafi'    #邮箱对SMTP的授权码，不是邮箱密码
    # receiver = '437889925@qq.com'
    # # msg = MIMEMultipart()
    # msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # msg['Subject'] = u"自动化测试报告"
    # msg["from"] = '517110453@qq.com'
    # msg["to"] = Header('测试','utf-8')
    # 添加附件
    # msg.attach(body)
    # att = MIMEText(mail_body, "base64", "utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment; filename= "report.html"'
    # msg.attach(att)

    # try:
    #     smtp = smtplib.SMTP(smtpserver, 25)
    # except:
    #     smtp = smtplib.SMTP()
    #     smtp.connect(smtpserver, 25)


    # smtp = smtplib.SMTP(smtpserver, 25)
    # smtp.login(sender, psw)
    # smtp.sendmail(sender, receiver, msg.as_string())
    # smtp.quit()
    # print('test report email has send out !')

if __name__ == '__main__':
    # 加载用例
    all_case = add_case()
    #执行用例，生成测试报告的路径
    run_case(all_case)
#获取最新的测试报告
    report_path = os.path.join(cur_path,'report')
    report_file = get_report_file(report_path)
    # send_email(report_file)
    #邮箱配置
    mail_host = reademail.mail_host
    mail_pass = reademail.mail_pass
    mail_user = reademail.mail_user
    sender = reademail.sender
    receiver = reademail.receiver
    send_email(mail_host,mail_pass,mail_user,sender,receiver,report_file)

# 方法2：构造测试集，将用例添加到测试套件中
# def add_case():
#     suite = unittest.TestSuite()   #实例化测试套件
#     suite.addTest(Testgetcominfo('test_getcominfo_01'))
#     suite.addTest(TestLogin('test_login_02'))    #将测试用例添加到测试套件中
#     suite.addTest(TestLogin('test_login_01'))
#     runner = unittest.TextTestRunner()      #实例化TextTestRunner 类
#     runner.run(suite)  #使用run方法运行测试套件中的所有用例
#     return suite
# if __name__ == '__main__':
#     add_case()

# 方法3：用discover 方法批量执行测试用例,Html生成测试报告
# cur_path = os.path.dirname(os.path.realpath(__file__))
# now = time.strftime("%Y_%m_%d_%H_%M_%S")
# def add_case():
#     case_path = cur_path + '\case'
#     discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)  #discover()方法可自动根据路径匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件
#     # suite = unittest.TestSuite()
#     # suite.addTest(discover)
#     return discover
# if __name__ == '__main__':
#     report_dir = os.path.join(cur_path,'report')    #拼接路径，当前路径下生成report文件
#     report_path = os.path.join(report_dir,now + 'result.html')    #report文件下生成report.html,+ 号是拼接名称
#     print(report_path)
#     fp = open(report_path,'wb')
#     runner = HTMLTestRunner(stream=fp,title=u'自动化测试报告，测试结果：',description=u'用例执行情况：')
#     # runner = unittest.TextTestRunner()
#     runner.run(add_case())
#     fp.close()

