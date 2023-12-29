# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
import time

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities


# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%ED%99%88&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N")

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)


# - 정보 획득
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# 제품 클릭
for i in range(4):  # 4개의 제품만 선택
    elements_click_product = browser.find_element(by=By.CSS_SELECTOR, value="#Container > div.best-area > div.TabsConts.on > ul:nth-child(1) > li:nth-child({}) > div > a".format(i+1)).click()

    time.sleep(3)

    # 리뷰 클릭
    elements_click_reviews = browser.find_element(by=By.CSS_SELECTOR, value="#reviewInfo > a ").click()

    # 랭킹 클릭하여 back
    elements_click_back = browser.find_element(by=By.CSS_SELECTOR, value="#gnbWrap > ul > li:nth-child(2) > a >span").click()

    

# def mongo_connect() :
#     from pymongo import MongoClient
#     mongoClient = MongoClient("mongodb://192.168.10.249:27017/")     
#     database = mongoClient["toy_seleniums"]     
#     collection = database["oliveyoung"]         
#     return collection

# oliveyoung_reviews = mongo_connect()
# for i in range(len()) :
#     oliveyoung_reviews.insert_one({"name":, "products":, "option":, "content":})

# 브라우저 종료
browser.quit()