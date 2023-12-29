# import seleniums_oliveyoung_subfunction as subfunction
# # 기본 function 형식 - 기다림. 불릴 때 기능
# def main() :  
#     try :
#         uri = "https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%EC%98%A4%ED%8A%B9&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N"
#         browser = subfunction.getBrowserFromURI(uri)
#         oliveyoung_count = subfunction.selectCourts(browser=browser)
#         print("court count : {}".format(oliveyoung_count))
#     except :
#         pass  # 업무 코드 문제 발생 시 대처 코드
#     finally :
       
        subfunction.quitBrowser(browser=browser)

if __name__ == "__main__" :
    try :
        main() # 업무 코드
    except :
        pass  # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass # try