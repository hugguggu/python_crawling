

import requests

from bs4 import BeautifulSoup

res = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = res.text

soup = BeautifulSoup(html, 'html.parser')
news_title = soup.select('.news_tit')

for idx in news_title:
    title = idx.text
    url = idx.attrs['href']
    print(title, [url])
    print('\n')



