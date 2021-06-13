from openpyxl import load_workbook
wb=load_workbook("second_file.xlsx")
sheet=wb.active

data=((1,2,3),(4,5,6),(7,8,9),(10,11,12))

for i in data:
    sheet.append(i)
wb.save("second_file.xlsx")
