import xlrd
loc = ("student_id.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(sheet.nrows):
    for j in range(sheet.nrows):
        print(sheet.cell_value(j,i))
