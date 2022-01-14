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

def scrape_upbit_data():
    page_index = 1
    base_url = "https://upbit.com"
    url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC"

    # options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("window-size=1920x1080")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url) # url 로 이동

    with open("1111_result.html", "w", encoding="utf8") as f:
        f.write(browser.page_source)

    # page_list = soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("a",attrs={"class":"NPI=a:page"})
    # max_page_index = int(page_list[len(page_list)-1].get_text().strip())
    # print(f'최대 페이지 {max_page_index}')

    # for page_index in range(1, max_page_index+1):
    #     page_url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=" + str(page_index)
    #     # print("page_index : "+ page_url)
        
    #     subject_list_soup = create_soup(page_url)
    #     subject_list = subject_list_soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})


    #     for subject_index in range(len(subject_list)):
    #         single_subject = subject_list[subject_index].find("p", attrs={"class":"subj"}).get_text().strip()
    #         single_link = base_url + subject_list[subject_index].a["href"]
    #         single_info = [single_subject]
    #         single_info.extend(get_single_chapter_info(single_link))
    #         # single_info = get_single_chapter_info(single_link)

    #         print( single_info )



if __name__ == "__main__":
    scrape_upbit_data()