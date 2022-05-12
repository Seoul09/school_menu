import requests
from bs4 import BeautifulSoup
from datetime import datetime



url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%83%81%EA%B5%AD%EB%A6%BD%EB%8C%80%ED%95%99%EA%B5%90%EC%82%AC%EB%B2%94%EB%8C%80%ED%95%99%EB%B6%80%EC%84%A4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90&oquery=%EA%B2%BD%EC%83%81%EA%B5%AD%EB%A6%BD%EB%8C%80%ED%95%99%EA%B5%90&tqi=hEpsjsp0JXVssbuCKKZssssssnZ-421774'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#main_pack > div.sc_new.cs_common_module.case_normal.color_23._school.cs_kindergarten._edu_list > div.cm_content_wrap > div:nth-child(3) > div > div.scroll_box._button_scroller > div > div > ul > li:nth-child(1) > div > div > ul')
   
    print(' - 급식 메뉴 안내 -')
    print('일자 : {}'.format(datetime.today()))
    for i in title:
        for j in i:
            print(j)
else :
    print(response.status_code)