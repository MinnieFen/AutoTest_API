# -*- coding:utf-8 -*-
import unittest
import os
class Runcase(unittest.TestCase):
    def all_case(self):
        cur_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        case_path = cur_path + 'case'
        print(case_path)
        # testcase = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
        runner = unittest.TextTestRunner(verbosity=2)
        test_unit = unittest.TestSuite()
        for test_suite in discover:
            for test_case in test_suite:
                test_unit.addTest(test_case)
        runner.run(test_unit)
        # print(testcase)
        # return testcase
if __name__ == '__main__':
    unittest.main()