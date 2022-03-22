# parser.py
from urllib import request
import requests

# Session 생성, with 구문 안에서 유지
request_headers = { 
'lang' : 'ko_KR',
'user-agent' : 'Mozilla/5.0 (M acintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;\q=0.9,imgwebp,*/*;q=0.8',
 } 
res = requests.get('https://etf.com', headers = request_headers)
print(res.ok)

with requests.Session() as s:
    # HTTP GET Request: requests대신 s 객체를 사용한다.
    req = s.get('https://www.etf.com', headers = request_headers)
    # HTML 소스 가져오기
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    print(header)
    print(status)
    print(is_ok)