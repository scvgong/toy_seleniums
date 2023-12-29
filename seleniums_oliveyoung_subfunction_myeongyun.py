# 제품명, 사용자ID, 옵션, 내용 3페이지까지 가져오기

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# 접속 url https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%EC%98%A4%ED%8A%B9&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N
def getBrowserFromURI(uri="https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%EC%98%A4%ED%8A%B9&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N"):
    webdriver_manager_directory = ChromeDriverManager().install()

    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

    # - 주소 입력
    browser.get(uri)
    return browser

# 랭킹 주소 #Container > div.best-area > div.TabsConts.on > ul:nth-child(1) > li:nth-child(1) > div

def item():
    # 제품명 div > p.prd_name
    
    # 리뷰 전체 #gdasContentsArea > div > div.review_list_wrap
    # 사용자 id div > p.info_user > a.id
    # 피부 타입 #gdasList > li:nth-child(1) > div.review_cont > div.poll_sample > dl:nth-child(1) > dt > span
    # 피부 타입 답변 #gdasList > li:nth-child(1) > div.review_cont > div.poll_sample > dl:nth-child(1) > dd > span
    # 피부 고민 #gdasList > li:nth-child(1) > div.review_cont > div.poll_sample > dl:nth-child(2) > dt > span
    # 피부 고민 답변 #gdasList > li:nth-child(1) > div.review_cont > div.poll_sample > dl:nth-child(2) > dd > span
    # 자극도 #gdasList > li:nth-child(1) > div.review_cont > div.poll_sample > dl:nth-child(3) > dt > span
    # 자극도 답변 #gdasList > li:nth-child(1) > div.review_cont > div.poll_sample > dl:nth-child(3) > dd > span
    pass
