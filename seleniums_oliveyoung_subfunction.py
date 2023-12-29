# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
import time

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities


# - 주소 function
def getBrowserFromURI(uri = "https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%ED%99%88&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N") :
    webdriver_manager_directory = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    browser.get(uri)
    return browser 

# - 정보 획득
def selectOliveyoung(browser) :
    from selenium.webdriver.common.by import By
    # 제품 클릭
    for i in range(4):  # 4개의 제품만 선택
        browser.find_element(by=By.CSS_SELECTOR, value="#Container > div.best-area > div.TabsConts.on > ul:nth-child(1) > li:nth-child({}) > div > a".format(i+1)).click()

        time.sleep(3)

        # 리뷰 클릭
        browser.find_element(by=By.CSS_SELECTOR, value="#reviewInfo > a ").click()

        time.sleep(3)

        # 랭킹 클릭하여 back
        browser.find_element(by=By.CSS_SELECTOR, value="#gnbWrap > ul > li:nth-child(2) > a >span").click()

    return
    
# 브라우저 종료
def quitBrowser(browser) :
    browser.quit()