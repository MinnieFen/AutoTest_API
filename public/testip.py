# -*- coding:utf-8 -*-
# coding:utf=8
# python3 env
import unittest,os
class TestIP(unittest.TestCase):
    '''
    测试点：
    1、正常最小值：0.0.0.0
    2、正常最大值：255.255.255.255
    3、正常用例：12.34.254.1
    4、小于最小值：-1.-1.-1.-1
    5、超过最大值：256.256.256.256
    6、包含字母：23.12.23.sdf
    7、以.拆分后，长度小于4: 12.23.34
    8、不包含.的字符串：dfsdf
    9、空字符：
    '''
    def test_case1(self):
        ipAddr = '0.0.0.0'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case2(self):
        '''test ip value'''
        ipAddr = '255.255.255.255'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case3(self):
        '''test ip value'''
        ipAddr = '12.34.254.1'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case4(self):
        '''test ip value'''
        ipAddr = '-1.-1.-1.-1'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case5(self):
        '''test ip value'''
        ipAddr = '256.256.256.256'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case6(self):
        '''test ip value'''
        ipAddr = '23.12.23.sdf'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case7(self):
        '''test ip value'''
        ipAddr = '12.23.34'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case8(self):
        '''test ip type'''
        ipAddr = 'dfsdf'
        result = GetIP(ipAddr)
        self.assertEqual(result, False)
    def test_case9(self):
        '''test ip type'''
        ipAddr = '     '
        result = GetIP(ipAddr)
        self.assertEqual(result, False)

def GetIP(ipAddr):
    arry = ipAddr.split('.')
    arry_len = len(arry)
    flag = True
    if arry_len != 4:
        flag = False
    else:
        for arry_i in arry:
            try:
                arry_i = int(arry_i)
                if  arry_i >= 0 and arry_i <= 255:
                    continue
                else:
                    flag = False
            except:
                flag = False
    return flag

if __name__ == '__main__':
    str_ip = input('pls input str：')
    result = GetIP(str_ip)
    print(result)
    case_path = os.path.abspath(os.getcwd())
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    runner = unittest.TextTestRunner()
    runner.run(discover)