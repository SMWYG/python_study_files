import requests #웹상의 데이터를 처리할 때 필요한 모듈
from bs4 import BeautifulSoup #웹언어를 가독성 좋게 만들어주는 모듈

def crawler(max_pages): #max_pages로 크롤할 페이지수를 받는다.
    page=1
    while page<max_pages:
