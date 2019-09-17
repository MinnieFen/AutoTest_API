# -*- coding:utf-8 -*-
# coding:utf=8
# python3 env
import unittest,os
class TestIP(unittest.TestCase):
    def test_case1(self):
        '''test arry len'''
        ipAddr = '12.0.0'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case2(self):
        '''test ip value'''
        ipAddr = '0.0.0.0'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case3(self):
        '''test ip value'''
        ipAddr = '255.255.255.255'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case4(self):
        '''test ip value'''
        ipAddr = '1.1.1.1'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case5(self):
        '''test ip value'''
        ipAddr = '254.254.254.254'
        result = GetIP(ipAddr)
        self.assertEqual(result,True)
    def test_case6(self):
        '''test ip value'''
        ipAddr = '-1.-1.-1.-1'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case7(self):
        '''test ip value'''
        ipAddr = '256.256.256.256'
        result = GetIP(ipAddr)
        self.assertEqual(result,False)
    def test_case8(self):
        '''test ip type'''
        ipAddr = 'sd.we.ww.ere'
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