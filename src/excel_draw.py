import openpyxl as opx
import pandas as pd
from openpyxl import load_workbook, Workbook

import stores_for_report as sfr
import formatting as frmt

excel_file = Workbook()
excel_file.create_sheet("Отчет", 0)
active_sheet = excel_file.active

report_sheet = frmt.FormattingTable(active_sheet)

for data in sfr.lenta("Мини"):
    active_sheet.append(data)

for data in sfr.am():
    active_sheet.append(data)

report_sheet.column_alignment_center(['A', 'E', 'F', 'G'])
report_sheet.column_alignment_left(['B', 'C', 'D', 'H', 'I'])

report_sheet.set_border(active_sheet)
report_sheet.set_font(active_sheet)

excel_file.save('report.xlsx')

# Конвертирую Страницу в DataFrame
df = pd.DataFrame(active_sheet.values)
