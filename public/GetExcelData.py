from public.ReadExcel import ReadExcel
import os
def get_excel_data(sheetname):
    filepath_now = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    excel_path = filepath_now + '\TestData\\test_data.xlsx'
    return ReadExcel(excel_path,sheetname).read_excel_data()
# get_excel_data('urlconfig')