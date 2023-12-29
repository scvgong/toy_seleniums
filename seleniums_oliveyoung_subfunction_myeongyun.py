# # 제품명, 사용자ID, 옵션, 내용 3페이지까지 가져오기

# # * 웹 크롤링 동작
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.common.by import By
# # 접속 url https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%EC%98%A4%ED%8A%B9&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N
# # def getBrowserFromURI(uri="https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000192697&dispCatNo=90000010009&trackingCd=Best_Sellingbest&t_page=%EB%9E%AD%ED%82%B9&t_click=%ED%8C%90%EB%A7%A4%EB%9E%AD%ED%82%B9_%EC%A0%84%EC%B2%B4_%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=1"):
# webdriver_manager_directory = ChromeDriverManager().install()

# # ChromeDriver 실행
# browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# # - 주소 입력
# browser.get("https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000192697&dispCatNo=90000010009&trackingCd=Best_Sellingbest&t_page=%EB%9E%AD%ED%82%B9&t_click=%ED%8C%90%EB%A7%A4%EB%9E%AD%ED%82%B9_%EC%A0%84%EC%B2%B4_%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=1")

# # 랭킹 주소 #Container > div.best-area > div.TabsConts.on > ul:nth-child(1) > li:nth-child(1) > div

# # 리뷰 클릭
# browser.find_element(by=By.CSS_SELECTOR, value="#reviewInfo > a ").click()

time.sleep(4)

def selectOliveyoung(browser):
    # 리뷰페이지 클릭
    for i in range(2,4):
        # 리뷰 전체 li > div.review_cont
        select_review = "ul.inner_list > li > div.review_cont"
        element_review = browser.find_elements(by=By.CSS_SELECTOR,value=select_review)

        for index in range(len(element_review)):
            
            # 제품명 div > p.prd_name
            select_title = "p.prd_name"
            element_title = browser.find_element(by=By.CSS_SELECTOR,value=select_title)
            title = element_title.text

            # 사용자 id div > p.info_user > a.id
            select_id = "#gdasList > li:nth-child({}) > div.info > div > p.info_user > a.id".format(index+1)
            element_id = browser.find_element(by=By.CSS_SELECTOR,value=select_id)
            id = element_id.text

            # 피부 타입 답변 #gdasList > li:nth-child({}) > div.review_cont > div.poll_sample > dl:nth-child(1) > dd > span
            select_type_answer = "#gdasList > li:nth-child({}) > div.review_cont > div.poll_sample > dl:nth-child(1)".format(index+1)
            element_type_answer = browser.find_element(by=By.CSS_SELECTOR,value=select_type_answer)
            type_asnwer = element_type_answer.text

            # 피부 고민 답변 #gdasList > li:nth-child({}) > div.review_cont > div.poll_sample > dl:nth-child(2)
            select_worry_answer = "#gdasList > li:nth-child({}) > div.review_cont > div.poll_sample > dl:nth-child(2)".format(index+1)
            element_worry_answer = browser.find_element(by=By.CSS_SELECTOR,value=select_worry_answer)
            worry_asnwer = element_worry_answer.text

            # 자극도 답변 #gdasList > li:nth-child({}) > div.review_cont > div.poll_sample > dl:nth-child(3)
            select_stimulation_answer = "#gdasList > li:nth-child({}) > div.review_cont > div.poll_sample > dl:nth-child(3)".format(index+1)
            element_stimulation_answer = browser.find_element(by=By.CSS_SELECTOR,value=select_stimulation_answer)
            stimulation_answer = element_stimulation_answer.text

            print("{},{},{},{}".format(title,id,type_asnwer,worry_asnwer,stimulation_answer))
            
            pass
        url = "#gdasContentsArea > div > div.pageing > a:nth-child({})".format(i+1)
        browser.find_element(by=By.CSS_SELECTOR,value=url).click()
        time.sleep(3)

    pass








