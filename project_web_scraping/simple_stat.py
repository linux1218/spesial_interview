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
from gtts import gTTS
import vlc
from mutagen.mp3 import MP3
import pymysql
import datetime


# DROP TABLE simple_stat_tb;
# CREATE TABLE `simple_stat_tb`(
#   `num`            BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#   `create_date`    DATETIME,
#   `subject`        VARCHAR(128) NOT NULL,
#   `view_count`     NUMERIC
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
# ALTER TABLE simple_stat_tb ADD INDEX IDX_simple_stat_tb_1(create_date ASC);
# ALTER TABLE simple_stat_tb ADD INDEX IDX_simple_stat_tb_2(subject ASC);


global mydb
global mycursor
global browser
global view_count_list
global subject_list
global currdate


def connect_stat_db():
    global mydb
    global mycursor
    
    mydb = pymysql.connect( host='127.0.0.1', port=5909, user='cho', passwd='Qwer1234!',db='cho_db', charset='utf8')
    mycursor = mydb.cursor()

def disconnect_stat_db():
    mycursor.close()
    mydb.close()

def init_webdriver():
    global browser
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(1)

def clear_webdriver():
    global browser
    browser.quit()


def scrape_special_interview_view_count():
    global browser
    global view_count_list
    global subject_list

    view_count_list=[]
    subject_list=[]
    base_url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page="

    #시작 URL로 변경
    page_index=0
    novel_index_offset=0

    while True:        
        page_index+=1

        url = base_url + str(page_index)
        
        # try:
        browser.get(url) # url 로 이동
        time.sleep(1)

        soup = BeautifulSoup(browser.page_source, "lxml")

        novel_list_elements = soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li", attrs={"class":"volumeComment"})

        for novel_list_element in novel_list_elements:
            view_count=novel_list_element.find_all("span", attrs={"class":"count"})[1].get_text().split(' ')[1].replace(',','').replace('만','0000')
            subject=novel_list_element.find("p", attrs={"class":"subj"}).get_text().replace('\n','').replace('\t','').split('화')[0]
            view_count_list.append(view_count)
            subject_list.append(subject)

        nest_page_index=soup.find("div", attrs={"class":"paging NE=a:lst"}).find("a", text=str(page_index+1))

        if not nest_page_index:
            break


def insert_curr_stat_info():
    global mydb
    global mycursor
    global currdate
    global view_count_list
    global subject_list

    for subject, view_count in zip(subject_list, view_count_list):
        sql = "INSERT INTO simple_stat_tb \
            (create_date, subject, view_count) \
                VALUES (%s, %s, %s)"
        val = (currdate, subject, view_count)

        mycursor.execute(sql, val)
        mydb.commit()


if __name__ == "__main__":
    connect_stat_db()
    
    try:
        while True:
            now = datetime.datetime.now()
            currdate = now.strftime('%Y-%m-%d %H:%M:%S')
            init_webdriver()
            scrape_special_interview_view_count()
            insert_curr_stat_info()
            clear_webdriver()
            print('전 작품 체크가 끝났습니다.')
            time.sleep(580)
    except Exception as err:
        print(err)
        disconnect_stat_db()

