

import requests

from bs4 import BeautifulSoup

import pyautogui

## 파이썬 기본 입력 API
# keyword = input("keywords??  ")
keyword = pyautogui.prompt("keywords?? ")

# 주소 가져오기 및 텍스트로 변환
res = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = res.text

#   HTML 분석 API
soup = BeautifulSoup(html, 'html.parser')
news_title = soup.select('.news_tit')

for idx in news_title:
    title = idx.text
    url = idx.attrs['href']
    print(title, [url])
    print('\n')



