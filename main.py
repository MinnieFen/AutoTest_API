# -*- coding:utf-8 -*-
import unittest
import os
import time
import HTMLTestRunner

cur_path = os.path.dirname(os.path.realpath(__file__))
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
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告，测试结果：',description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file

if __name__ == '__main__':
    all_case = add_case()
    run_case(all_case)
    report_path = os.path.join(cur_path,'report')
    report_file = get_report_file(report_path)

# 用discove 方法批量执行测试用例
# cur_path = os.path.dirname(os.path.realpath(__file__))
# now = time.strftime("%Y_%m_%d_%H_%M_%S")
# def add_case():
#     case_path = cur_path + '\case'
#     discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
#     suite = unittest.TestSuite()
#     suite.addTest(discover)
#     return suite
# if __name__ == '__main__':
#     report_path = os.path.join(cur_path,now + 'report.html')
#     fp = open(report_path,'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告，测试结果：',description=u'用例执行情况：')
#     runner = unittest.TextTestRunner()
#     runner.run(add_case())
# discover 方法2
# def add_case(caseName = 'case',rule = 'test*.py'):
#     cur_path = os.path.dirname(os.path.realpath(__file__))
#     case_path = os.path.join(cur_path,caseName)
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
#     runner = unittest.TextTestRunner()
#     for test_suite in discover:
#         for case in test_suite:
#             testcase.addTest(case)
#     runner.run(testcase)
#     print(testcase)
#     return testcase
# if __name__ == '__main__':
#     add_case()