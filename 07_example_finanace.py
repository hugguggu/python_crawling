

import requests

from bs4 import BeautifulSoup

codes = [
    '005930',
    '000660',
    '035720'
]

for idx in codes:
    # 주소 가져오기 및 텍스트로 변환
    url = f"https://finance.naver.com/item/sise.naver?code={idx}"
    res = requests.get(url)
    html = res.text

    #   HTML 분석 API
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal').text
    price = price.replace(',','')

    print(price)

