import openpyxl
import requests

from bs4 import BeautifulSoup

codes = [
    '005930',
    '000660',
    '035720'
]


# 엑셀 파일 불러오기
filepath = r'test_excel.xlsx'
workbook = openpyxl.load_workbook(filepath)

# 현재 워크시트 선택
sheet = workbook.active

row = 2
for idx in codes:
    # 주소 가져오기 및 텍스트로 변환
    url = f"https://finance.naver.com/item/sise.naver?code={idx}"
    res = requests.get(url)
    html = res.text

    #   HTML 분석 API
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal').text
    price = price.replace(',','')

    # 데이터 입력
    sheet[f'B{row}'] = int(price)
    row += 1

    print(price)



workbook.save(filepath)



