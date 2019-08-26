# -*- coding:utf-8 -*-
import unittest
import os

def add_case(caseName = 'case',rule = 'test*.py'):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    case_path = os.path.join(cur_path,caseName)
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    runner = unittest.TextTestRunner()
    for test_suite in discover:
        for case in test_suite:
            testcase.addTest(case)
    runner.run(testcase)
    print(testcase)
    return testcase


if __name__ == '__main__':
    add_case()