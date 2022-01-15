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


# DB 생성정보
# create user cho@localhost identified by 'Qwer1234!';
# create user cho@'%' identified by 'Qwer1234!';
# create database cho_db default character set utf8;
# grant all privileges on cho_db.* to 'cho'@'%'
# ####grant all privileges on cho_db.* to 'cho'@'%' identified by 'Qwer1234!';


# DROP TABLE spesial_interview_tb;
# CREATE TABLE `spesial_interview_tb`(
#   `num`            BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#   `create_date`    DATETIME DEFAULT CURRENT_TIMESTAMP,
#   `subject`        VARCHAR(128) NOT NULL,
#   `score_average`  NUMERIC,
#   `score_count`    NUMERIC,
#   `heart_count`    NUMERIC,
#   `comment_count`  NUMERIC,
#   `view_count`     NUMERIC
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# ALTER TABLE spesial_interview_tb ADD INDEX IDX_s_i_tb_1(create_date ASC);
# ALTER TABLE spesial_interview_tb ADD INDEX IDX_s_i_tb_2(subject ASC);


global mydb
global mycursor
global browser
global view_count_list
global currdate
global novel_url_list


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
    global novel_url_list

    novel_url_list=[]

    view_count_list=[]
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
            view_count_list.append(view_count)

            novel_url=novel_list_element.find("a", attrs={"class":"list_item NPI=a:list"})["href"]
            print("https://novel.naver.com"+novel_url)
            novel_url_list.append("https://novel.naver.com"+novel_url)
        
        nest_page_index=soup.find("div", attrs={"class":"paging NE=a:lst"}).find("a", text=str(page_index+1))

        if not nest_page_index:
            break

       

def insert_chang_stat_info(stat_in_db):
    global mydb
    global mycursor
    
    sql = "INSERT INTO spesial_interview_tb \
        (subject, score_average, score_count, heart_count, comment_count, view_count) \
            VALUES (%s, %s, %s, %s, %s, %s)"
    val = (stat_in_db[0], stat_in_db[1], stat_in_db[2], stat_in_db[3], stat_in_db[4], stat_in_db[5])

    mycursor.execute(sql, val)
    mydb.commit()


def insert_curr_stat_info(stat_in_db):
    global mydb
    global mycursor
    global currdate
    
    sql = "INSERT INTO spesial_interview_stat_tb \
        (create_date, subject, score_average, score_count, heart_count, comment_count, view_count) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (currdate, stat_in_db[0], stat_in_db[1], stat_in_db[2], stat_in_db[3], stat_in_db[4], stat_in_db[5])

    mycursor.execute(sql, val)
    mydb.commit()


def text_to_speech(input_text):
    pass
    # checkval=len(input_text)
    # gSound = gTTS( input_text, lang='ko', slow=False)
    # gSound.save('inputtext.mp3')
    # media_player = vlc.MediaPlayer()
    # media=vlc.Media('inputtext.mp3')
    # audio = MP3("inputtext.mp3")
    # play_time = audio.info.length
    # media_player.set_media(media)
    # media_player.play()
    # time.sleep(play_time)


def check_change_info(old_total, new_total):
    change_info_flag=False
    voice_notice=""

    subject_db = ""
    score_average_db = score_count_db = heart_count_db = comment_count_db = view_count_db = 0

    simple_subject = old_total[0].split('화')
    subject_db = simple_subject[0]+"화"
    voice_notice = "{0}화. ".format( simple_subject[0])

    insert_curr_stat_info([subject_db, round(float(new_total[1].strip()),3), int(new_total[2].replace("명","").strip()), int(new_total[3].strip()), 0, int(new_total[4].strip())])

    if old_total[1] != new_total[1]:
        score_average_db = round( float(new_total[1].strip()) - float(old_total[1].strip()), 3)
        voice_notice += ", 평점 {0} 추가, " .format( score_average_db )
        change_info_flag = True

    if old_total[2] != new_total[2]:
        score_count_db = int(new_total[2].replace("명","").strip()) - int(old_total[2].replace("명","").strip())
        voice_notice += ", 별점참여 {0} 추가, " .format( score_count_db )
        change_info_flag = True

    if old_total[3] != new_total[3]:
        heart_count_db = int(new_total[3].strip()) - int(old_total[3].strip())
        voice_notice += ", 하트 {0} 추가, " .format( heart_count_db )
        change_info_flag = True

    if old_total[4] != new_total[4]:
        view_count_db = int(new_total[4].strip()) - int(old_total[4].strip())
        voice_notice += ", 조회수 {0} 추가, " .format( view_count_db )
        change_info_flag = True
    
    old_comment_list = old_total[5]
    new_comment_list = new_total[5]

    old_comment_list_cnt=len(old_comment_list[0])
    new_comment_list_cnt=len(new_comment_list[0])

    comment_count_db = 0
    if new_comment_list_cnt > 0:
        loop_comment_index=range(0,new_comment_list_cnt)
        for new_comment_index in loop_comment_index:
            if old_comment_list_cnt > 0:
                continue_boolean=False

                for old_comment_index in range(0,old_comment_list_cnt):
                    if old_comment_list[0][old_comment_index] == new_comment_list[0][new_comment_index]:
                        try:
                            if old_comment_list[2][old_comment_index] == new_comment_list[2][new_comment_index]:
                                continue_boolean=True
                                break
                        except IndexError:
                            continue_boolean=True
                            continue
                
                if continue_boolean:
                    continue

            try:
                voice_notice+="추가 {0}님의 댓글, {1}" .format( new_comment_list[0][new_comment_index], new_comment_list[2][new_comment_index] )
                change_info_flag = True
                comment_count_db+=1
            except IndexError:
                voice_notice+="추가 {0}님의 댓글, 클린봇으로 삭제되었습니다." .format( new_comment_list[0][new_comment_index])
                change_info_flag = True
                comment_count_db+=1
    
    if( change_info_flag ):
        print(voice_notice)
        text_to_speech(voice_notice)
        insert_chang_stat_info([subject_db, score_average_db, score_count_db, heart_count_db, comment_count_db, view_count_db])


def scrape_special_interview():
    global browser
    global view_count_list
    print("[특별한 면접]")
    starturl = "https://novel.naver.com/best/list?novelId=1019899"
    
    # 테스트 페이지
    url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"

    #제일 마지막화 제목
    browser.get(starturl) # start url 로 이동
    soup = BeautifulSoup(browser.page_source, "lxml")
    subject_list = soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})
    stop_subject = subject_list[0].find("p", attrs={"class":"subj"}).get_text().strip()
    stop_subject = stop_subject[:stop_subject.find('\n')]




    with open('C:/PythonWorkSpace/spesial_interview/project_web_scraping/spesial_interview_old.pickle', 'rb') as rf:
        old_total_info = pickle.load(rf)

    total_info=[] # 전체 정보를 저장할 변수

    check_index = 0 #루프 횟수 

    while True:
        try:
            #시작 URL로 변경
            # browser.get(url) # url 로 이동
            # browser.find_element(By.XPATH, "//*[@id='volume1']/a").click()

            browser.get(novel_url_list[check_index])

            time.sleep(3)
            subject = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[2]/h2").text
            subject = subject[:subject.find('\n')]
            score_average = browser.find_element(By.XPATH, "//*[@id='currentStarScore']").text
            score_count = browser.find_element(By.XPATH, "//*[@id='currentStarScoreCount']").text
            heart_count = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em").text
            view_count = view_count_list[check_index]

            browser.switch_to.frame('nCommentIframe') # iframe 댓글 영역 이동
            nick_list    = [nick.text    for nick    in browser.find_elements(By.CLASS_NAME,"u_cbox_nick")]
            id_list      = [id.text      for id      in browser.find_elements(By.CLASS_NAME,"u_cbox_id")]
            comment_list = [content.text for content in browser.find_elements(By.CLASS_NAME,"u_cbox_contents")]
            comment_info = [nick_list, id_list, comment_list]
            browser.switch_to.default_content() # iframe 댓글 영역 이동

            # 정보 일괄 취합
            single_info=[subject, score_average, score_count, heart_count, view_count, comment_info]
            total_info.append(single_info)

            # print(f'{subject}  검사를 시작합니다.')

            if check_index < len(old_total_info):
                check_change_info(old_total_info[check_index], single_info)
            else:
                print(subject, "는 신규 작품이므로 이후부터 체크됩니다.")

            check_index = check_index + 1

            if stop_subject == subject:
                print('마지막화 입니다. 종료합니다.')
                
                with open('C:/PythonWorkSpace/spesial_interview/project_web_scraping/spesial_interview_old.pickle', 'wb') as fw:
                    pickle.dump(total_info, fw)
                break

            # next_part = browser.find_element(By.XPATH, "//*[@id='nextVolumeBtn']")

            # while not  next_part:
            #     next_part = browser.find_element(By.XPATH, "//*[@id='nextVolumeBtn']")
            #     print('다음화 버튼을 기다립니다.')
            #     time.sleep(1)

            # next_part.click()

        except Exception as err:
            print(err)
            break


if __name__ == "__main__":
    connect_stat_db()
    
    try:
        while True:
            now = datetime.datetime.now()
            currdate = now.strftime('%Y-%m-%d %H:%M:%S')
            init_webdriver()
            scrape_special_interview_view_count()
            scrape_special_interview()
            clear_webdriver()
            voice_notice='''전 작품 체크가 끝났습니다.'''
            print(voice_notice)
    except Exception as err:
        print(err)
        disconnect_stat_db()



