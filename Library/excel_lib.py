import xlrd
from Library.config import Config



def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.LOCATOR_WEB_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.nrows
    d = {}
    for i in range(rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1], row[2])
    return d




def read_data(sheetname):
    workbook = xlrd.open_workbook(Config.TEST_EXCELDATA_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    header = next(rows)
    columns = worksheet.ncols
    list1 = []
    for i in rows:
        values = ()
        for j in range(columns):
            values +=(i[j].value,)
            list1.append(values)
        return list1

# print(read_locators(Config.WATCH_LOCATOR_SHEET))
# print(read_data(Config.WATCH_TESTDATA_SHEET))




















































#
# class ReadExcel:
#
#     def read_testdata(self):
#         wb = xlrd.open_workbook(Config.TEST_EXCELDATA_PATH)
#         ws = wb.sheet_by_name(Config.WATCH_TESTDATA_SHEET)
#         columns = ws.ncols
#         rows = ws.get_rows()  # generator object
#         header = next(rows)
#         data = []
#
#         for row in rows:
#             data.append((row[0].value,row[1].value))
#
#         return data
#
#     def read_locators(self, sheetname):
#         wb = xlrd.open_workbook(Config.LOCATOR_WEB_PATH)
#         ws = wb.sheet_by_name(sheetname)
#         rows = ws.get_rows()
#         header = next(rows)
#
#         dict_1 = {}
#         for row in rows:
#             dict_1[row[0].value] = (row[1].value, row[2].value)
#
#         return dict_1
#
#
# a1 =  ReadExcel()
# data_ = a1.read_testdata()
# print(a1)
# print(a1.read_locators())
