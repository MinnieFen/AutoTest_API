# -*- coding:utf-8 -*-
from public.get_config import Excel_data
import data_config
class GetData:
    def __init__(self):
        self.get_excel = Excel_data
    def get_case_line(self):
        return self.