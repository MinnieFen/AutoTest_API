# -*- coding:utf-8 -*-
import xlrd
import os
# import pandas as pd

class Excel_data(object):
    def __init__(self,excelpath,sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def get_excel_data(self):
        fileinfo = []
        for i in range(1,self.rowNum):
            excel_dict = {}
            for j in range(self.colNum):
                data = self.table.cell_value(i,j)
                excel_dict[self.keys[j]] = data
            fileinfo.append(excel_dict)
        # print(fileinfo)
        return fileinfo

        # print(fileinfo[0]['host'])
# if __name__ == '__main__':
#     filepath_now = os.path.abspath(os.path.join(os.getcwd(), '..'))
#     excelpath = filepath_now +'/config/config.xlsx'
#     sheetname = 'urlconfig'
#     get_data = Excel_data(excelpath,sheetname)
#     datas = get_data.get_excel_data()


# class Excel_data(object):
#     def __init__(self,datapath):
#         self.datapath = datapath
#
#     def get_excel_data(self):
#         # self.datapath = "D:/appinstall/python3/test1/config/config.xlsx"
#         df = pd.read_excel(self.datapath)
#         data_list = []
#         for i in df.index.values:
#             excel_data = df.ix[i,["name","host","url","method","data","check_point"]].to_dict()
#             data_list.append(excel_data)
#             # print('最终数据：{0}'.format(excel_data))
#             # print(data_list[0]['name'])       #获取name的值
#         return data_list
#
# if __name__ == '__main__':
#     datapath = 'D:/appinstall/python3/test1/config/config.xlsx'
#     data = Excel_data(datapath)
#     datas = data.get_excel_data()
#     print(datas)
