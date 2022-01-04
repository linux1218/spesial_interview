import re
import requests
import random
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_special_interview():
    print("[특별한 면접]")
    starturl = "https://novel.naver.com/best/list?novelId=1019899"
    
    # 테스트 페이지
    url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"

    # options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("window-size=1920x1080")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    # browser = webdriver.Chrome(options=options)

    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.maximize_window()


    #제일 마지막화 제목
    browser.get(starturl) # start url 로 이동
    soup = BeautifulSoup(browser.page_source, "lxml")
    subject_list = soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})
    stop_subject = subject_list[0].find("p", attrs={"class":"subj"}).get_text().strip()
    stop_subject = stop_subject[:stop_subject.find('\n')]


    #시작 URL로 변경
    browser.get(url) # url 로 이동
    browser.find_element(By.XPATH, "//*[@id='volume1']/a").click()


    total_info=[] # 전체 정보를 저장할 변수

    while True:
        try:
            time.sleep(5)            
            subject = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[2]/h2").text
            subject = subject[:subject.find('\n')]
            score_average = browser.find_element(By.XPATH, "//*[@id='currentStarScore']").text
            score_count = browser.find_element(By.XPATH, "//*[@id='currentStarScoreCount']").text
            heart_count = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em").text

            browser.switch_to.frame('nCommentIframe') # iframe 댓글 영역 이동
            nick_list    = [nick.text    for nick    in browser.find_elements(By.CLASS_NAME,"u_cbox_nick")]
            id_list      = [id.text      for id      in browser.find_elements(By.CLASS_NAME,"u_cbox_id")]
            content_list = [content.text for content in browser.find_elements(By.CLASS_NAME,"u_cbox_contents")]
            content_info = [nick_list, id_list, content_list]
            browser.switch_to.default_content() # iframe 댓글 영역 이동

            # 정보 일괄 취합
            single_info=[subject, score_average, score_count, heart_count, content_info]
            total_info.append(single_info)
            
            if stop_subject == subject:
                print('마지막화 입니다. 종료합니다.')
                break

            next_part = browser.find_element(By.XPATH, "//*[@id='nextVolumeBtn']").click()

        except:
            break

    with open('./spesial_interview_old.pickle', 'wb') as fw:
        pickle.dump(total_info, fw)
    print('picle dump succ')

    browser.quit()

            

if __name__ == "__main__":
    scrape_special_interview()



