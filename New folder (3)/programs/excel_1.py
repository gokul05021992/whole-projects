from openpyxl import Workbook
wb=Workbook()
sheet=wb.active

sheet['A1']=100
sheet['A2']=200

sheet['A4']='python'

sheet.cell(row=5,column=3).value='new value'

wb.save("first_file.xlsx")