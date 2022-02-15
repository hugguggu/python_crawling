import openpyxl

# 엑셀 파일 불러오기
filepath = r'test_excel.xlsx'
workbook = openpyxl.load_workbook(filepath)

# 엑셀 워크시트 생성
sheet = workbook["test"]

# 데이터 추가
sheet['A1'] = '참가번호'
sheet['B1'] = '성명'

sheet['A2'] = '2'
sheet['B2'] = 'DEF'

sheet['A3'] = '3'
sheet['B3'] = 'HIJ'


workbook.save(filepath)



