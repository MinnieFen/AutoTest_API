# -*- coding:utf-8 -*-
import xlrd
# import pandas as pd

class ReadExcel(object):
    def __init__(self,excelpath,sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.keys = self.table.row_values(0)       #获取第一行所有内容
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def read_excel_data(self):
        file_list = []
        for i in range(1,self.rowNum):
            data_dict = {}
            for j in range(self.colNum):
                data = self.table.cell_value(i,j)      #获取单元格数据
                data_dict[self.keys[j]] = data         #循环每一个有效的单元格，将字段与值对应存储到字典中
            file_list.append(data_dict)
        # print(file_list)
        return file_list

# if __name__ == '__main__':
#     excelpath = 'D:/appinstall/python3/test1/testdata/data_pwdlogin.xlsx'
#     sheetname = 'logindata'
#     get_data = ReadExcel(excelpath,sheetname)
#     datas = get_data.readexceldata()



# class ReadExcel(object):
#     def __init__(self,filepath):
#         self.filepath = filepath
#
#     def readexceldata(filepath):
#         # filepath = "D:/appinstall/python3/test1/testdata/data_pwdlogin.xlsx"
#         df = pd.read_excel(filepath)
#         file_list = []
#         for i in df.index.values:
#             row_data = df.ix[i,["syscode","requestid","version","sys_name","sys_version","device_model","device_id","device_name","signature","device_brand","device_product","net_type","phone","password"]].to_dict()
#             file_list.append(row_data)
#             print('最终数据：{}'.format(row_data))
#             print('最终数据：%s' %file_list)
#         return file_list

# if __name__ == '__main__':
     # ReadExcel.readexceldata("D:/appinstall/python3/test1/testdata/data_pwdlogin.xlsx")