# import re
# import requests
# import random
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# def create_soup(url):
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     return soup

# def get_single_chapter_info(url):
#     options = webdriver.ChromeOptions()
#     # options.headless = True
#     # options.add_argument("window-size=1920x1080")
#     # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

#     browser = webdriver.Chrome(options=options)
#     browser.implicitly_wait(10) # seconds
#     browser.maximize_window()
#     browser.get(url) # url 로 이동

#     try:
#         score_average = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScore']"))).text
#         score_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScoreCount']"))).text       
#         heart_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em"))).text
#         # comment_orner   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cbox_module_wai_u_cbox_content_wrap_tabpanel']/ul/li[1]/div[1]/div/div[1]/span[1]/span/span/span[1]/span"))).text

#         # comment_orner   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_list")))
#         # soup = BeautifulSoup(browser.page_source, "lxml")

#         with open("1111_result.html", "w", encoding="utf8") as f:
#             f.write(browser.page_source)

#     finally:
#         print('finally 들어왔어')
#         browser.quit()


        
#     comment_list  = ''
#     name = soup.find("div", attrs={"id":"cbox_module"})
#     # name = soup.find("div", attrs={"id":"cbox_module_wai_u_cbox_content_wrap_tabpanel"})

#     if name:
#         print('name 결과가 있어요. ㅋㅋㅋ')
#         print(name)
#     else:
#         print('name 널이에요')

#     # name = soup.find("ul", attrs={"class":"u_cbox_list"}).find_all("span", attrs={"class":"u_cbox_nick"})

#     print("score_average : " + score_average )
#     print("score_count   : " + score_count   )
#     print("heart_count   : " + heart_count   )
#     # print("comment_list  : " + comment_list  )
#     # print("name          : " + name          )


#     # return [score_average, score_count, heart_count, comment_list]
#     return [score_average, score_count, heart_count]

# def scrape_special_interview():
#     print("[특별한 면접]")
#     page_index = 1
#     base_url = "https://novel.naver.com/"
#     url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"
#     soup = create_soup(url)

#     # page_list=soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("strong")
    
#     # news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
#     # with open("result.html", "w", encoding="utf8") as f:
#     #     f.write(soup.contents)

#     page_list = soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("a",attrs={"class":"NPI=a:page"})
#     max_page_index = int(page_list[len(page_list)-1].get_text().strip())
#     print(f'최대 페이지 {max_page_index}')

#     for page_index in range(1, max_page_index+1):
#         page_url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=" + str(page_index)
#         # print("page_index : "+ page_url)
        
#         subject_list_soup = create_soup(page_url)
#         subject_list = subject_list_soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})


#         for subject_index in range(len(subject_list)):
#             single_subject = subject_list[subject_index].find("p", attrs={"class":"subj"}).get_text().strip()
#             single_link = base_url + subject_list[subject_index].a["href"]

#             ret_v_list = get_single_chapter_info(single_link)
#             # print(ret_v_list)



#             # print( single_subject )
#             # print( single_link )
#             time.sleep(10)
#             break


# if __name__ == "__main__":
#     scrape_special_interview() # 오늘의 날씨 정보 가져오기









import re
import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def get_single_chapter_info(url):
    # options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("window-size=1920x1080")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url) # url 로 이동

    time.sleep(2)
    try:
        score_average = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScore']"))).text
        score_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScoreCount']"))).text       
        heart_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em"))).text

        time.sleep(10)
        # heart_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em"))).text
        # with open("1111_result.html", "w", encoding="utf8") as f:
        #     f.write(browser.page_source)
    finally:
        print('3초 기다리고 다시 시도해보자')
        time.sleep(3)
        print('파일에 써보자')
        with open("1111_result.html", "w", encoding="utf8") as f:
            f.write(browser.page_source)

        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "cbox_module_wai_u_cbox_content_wrap_tabpanel")))
        
        time.sleep(100)
        browser.quit()

    return [score_average, score_count, heart_count]


def scrape_special_interview():
    print("[특별한 면접]")
    page_index = 1
    base_url = "https://novel.naver.com/"
    url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"
    soup = create_soup(url)

    page_list = soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("a",attrs={"class":"NPI=a:page"})
    max_page_index = int(page_list[len(page_list)-1].get_text().strip())
    print(f'최대 페이지 {max_page_index}')

    for page_index in range(1, max_page_index+1):
        page_url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=" + str(page_index)
        # print("page_index : "+ page_url)
        
        subject_list_soup = create_soup(page_url)
        subject_list = subject_list_soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})


        for subject_index in range(len(subject_list)):
            single_subject = subject_list[subject_index].find("p", attrs={"class":"subj"}).get_text().strip()
            single_link = base_url + subject_list[subject_index].a["href"]
            single_info = [single_subject]
            single_info.extend(get_single_chapter_info(single_link))
            # single_info = get_single_chapter_info(single_link)

            print( single_info )



if __name__ == "__main__":
    scrape_special_interview()