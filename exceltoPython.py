import openpyxl as xl

wb = xl.load_workbook('example.xlsx')

sn = wb.sheetnames
print(sn)

sheet1 = wb['Sheet 1 ']
cellA1 = wb['cellA1']

print(sheet1)
print(cellA1.value)
print(cellA1.row)
print(cellA1.column)
print(cellA1.coordinate)