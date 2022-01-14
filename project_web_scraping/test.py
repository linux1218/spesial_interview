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





























# import re
# import requests
# import random
# import time
# import pickle
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from gtts import gTTS
# import vlc
# from mutagen.mp3 import MP3  

# def text_to_speech(input_text):
#     checkval=len(input_text)
#     gSound = gTTS( input_text, lang='ko', slow=False)
#     gSound.save('inputtext.mp3')
#     media_player = vlc.MediaPlayer()
#     media=vlc.Media('inputtext.mp3')
#     audio = MP3("inputtext.mp3")
#     play_time = audio.info.length
#     media_player.set_media(media)
#     media_player.play()
#     time.sleep(play_time)


# def print_contents_info(old_total_info):
#     for old_total in old_total_info:
#         print( "subject       : ", old_total[0] )
#         print( "score_average : ", old_total[1] )
#         print( "score_count   : ", old_total[2] )
#         print( "heart_count   : ", old_total[3] )

#         old_comment_list = old_total[4]
#         for old_comment_index in range(len(old_comment_list[0])):
#             try:
#                 if( old_comment_list[0][old_comment_index] ):
#                     print("\tnick          : ", old_comment_list[0][old_comment_index] )
#                 if( old_comment_list[1][old_comment_index] ):
#                     print("\tid            : ", old_comment_list[1][old_comment_index] )
#                 if( old_comment_list[2][old_comment_index] ):
#                     print("\tcomment       : ", old_comment_list[2][old_comment_index] )
#             except IndexError:
#                 print("클린봇으로 댓글 삭제")


# def check_chang_info(old_total_info, new_total_info):

#     voice_notice=""

#     # for old_total in old_total_info:
#     for check_index in range(len(old_total_info)):
#         # print( "subject       : ", old_total[0] )
#         # print( "score_average : ", old_total[1] )
#         # print( "score_count   : ", old_total[2] )
#         # print( "heart_count   : ", old_total[3] )

#         old_total = old_total_info[check_index]
#         new_total = new_total_info[check_index]

#         if old_total[1] != new_total[1]:
#             voice_notice="{0}, 작품의 평점이 변경되어 기존 {1}에서, 현재 {2}" .format( old_total[0],old_total[1],new_total[1] )
#             text_to_speech(voice_notice)
#         if old_total[1] != new_total[1]:
#             voice_notice="{0}, 작품의 별점 참여 인원이 기존 {1}에서, 현재 {2}" .format( old_total[0],old_total[1],new_total[1] )
#             text_to_speech(voice_notice)
#         if old_total[1] != new_total[1]:
#             voice_notice="{0}, 작품의 하트가 변경되어 기존 {1}에서, 현재 {2}" .format( old_total[0],old_total[1],new_total[1] )
#             text_to_speech(voice_notice)

#         old_comment_list = old_total[4]
#         new_comment_list = new_total[4]

#         old_comment_list_cnt=len(old_comment_list[0])
#         new_comment_list_cnt=len(new_comment_list[0])

#         if old_comment_list_cnt < new_comment_list_cnt:
#             for new_comment_index in range(old_comment_list_cnt,new_comment_list_cnt):
#                 voice_notice="{0}, 작품의 댓글이 변경되어 알려드립니다." .format( old_total[0])
#                 text_to_speech(voice_notice)
#                 try:
#                     voice_notice="{0}님의 댓글, {1}" .format( new_comment_list[0][new_comment_index], new_comment_list[2][new_comment_index] )
#                     text_to_speech(voice_notice)
#                 except IndexError:
#                     voice_notice="{0}님의 댓글, 클린봇으로 삭제되었습니다." .format( new_comment_list[0][new_comment_index])
#                     text_to_speech(voice_notice)


# def check_change_info(old_total, new_total):
#     change_info_flag=False
#     voice_notice=""

#     voice_notice = "{0} 작품 , ".format( old_total[0])
#     if old_total[1] != new_total[1]:
#         # voice_notice += ", 평점이 기존 {0}에서, {1}로 변경, " .format( old_total[1],new_total[1] )
#         voice_notice += ", 평점 {0} 추가, " .format( float(new_total[1].strip()) - float(old_total[1].strip()) )
#         change_info_flag = True
#     if old_total[2] != new_total[2]:
#         # voice_notice += ", 별점참여가 기존 {0}에서, {1}로 변경, " .format( old_total[2],new_total[2] )
#         voice_notice += ", 별점참여 {0} 추가, " .format( int(new_total[2].replace("명","").strip()) - int(old_total[2].replace("명","").strip()) )
#         change_info_flag = True
#     if old_total[3] != new_total[3]:
#         # voice_notice += ", 하트가 {0}에서, {1}로 변경, " .format( old_total[3],new_total[3] )
#         voice_notice += ", 하트 {0} 추가, " .format( int(new_total[3].strip()) - int(old_total[3].strip()) )
#         change_info_flag = True
    


#     old_comment_list = old_total[4]
#     new_comment_list = new_total[4]

#     old_comment_list_cnt=len(old_comment_list[0])
#     new_comment_list_cnt=len(new_comment_list[0])

#     if new_comment_list_cnt > 0:
#         loop_comment_index=range(0,new_comment_list_cnt)
#         for new_comment_index in loop_comment_index:
#             if old_comment_list_cnt > 0:
#                 continue_boolean=False
#                 for old_comment_index in range(0,old_comment_list_cnt):
#                     if old_comment_list[0][old_comment_index] == new_comment_list[0][new_comment_index]:                    
#                         if old_comment_list[2][old_comment_index] == new_comment_list[2][new_comment_index]:                        
#                             continue_boolean=True
#                             break
                
#                 if continue_boolean:
#                     continue

#             try:
#                 voice_notice+="추가 {0}님의 댓글, {1}" .format( new_comment_list[0][new_comment_index], new_comment_list[2][new_comment_index] )
#                 change_info_flag = True
#             except IndexError:
#                 voice_notice+="추가 {0}님의 댓글, 클린봇으로 삭제되었습니다." .format( new_comment_list[0][new_comment_index])
#                 change_info_flag = True


#     # if old_comment_list_cnt < new_comment_list_cnt:
#     #     for new_comment_index in range(0,new_comment_list_cnt-old_comment_list_cnt):
#     #         try:
#     #             voice_notice+="추가 {0}님의 댓글, {1}" .format( new_comment_list[0][new_comment_index], new_comment_list[2][new_comment_index] )
#     #             change_info_flag = True
#     #         except IndexError:
#     #             voice_notice+="추가 {0}님의 댓글, 클린봇으로 삭제되었습니다." .format( new_comment_list[0][new_comment_index])
#     #             change_info_flag = True
    
#     if( change_info_flag ):
#         print(voice_notice)
#         text_to_speech(voice_notice)

# def scrape_special_interview():
#     print("[특별한 면접]")
#     starturl = "https://novel.naver.com/best/list?novelId=1019899"
    
#     # 테스트 페이지
#     url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"

#     options = webdriver.ChromeOptions()
#     options.headless = True
#     options.add_argument("window-size=1920x1080")
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
#     browser = webdriver.Chrome(options=options)

#     # browser = webdriver.Chrome()
#     browser.implicitly_wait(2)
#     # browser.maximize_window()


#     #제일 마지막화 제목
#     browser.get(starturl) # start url 로 이동
#     soup = BeautifulSoup(browser.page_source, "lxml")
#     subject_list = soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})
#     stop_subject = subject_list[0].find("p", attrs={"class":"subj"}).get_text().strip()
#     stop_subject = stop_subject[:stop_subject.find('\n')]


#     #시작 URL로 변경
#     browser.get(url) # url 로 이동
#     browser.find_element(By.XPATH, "//*[@id='volume1']/a").click()


#     with open('C:/PythonWorkSpace/project_web_scraping/spesial_interview_old.pickle', 'rb') as rf:
#         old_total_info = pickle.load(rf)

#     # print_contents_info(old_total_info)

#     total_info=[] # 전체 정보를 저장할 변수

#     check_index = 0 #루프 횟수 

#     while True:
#         try:
#             time.sleep(3)
#             subject = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[2]/h2").text
#             subject = subject[:subject.find('\n')]
#             score_average = browser.find_element(By.XPATH, "//*[@id='currentStarScore']").text
#             score_count = browser.find_element(By.XPATH, "//*[@id='currentStarScoreCount']").text
#             heart_count = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em").text

#             browser.switch_to.frame('nCommentIframe') # iframe 댓글 영역 이동
#             nick_list    = [nick.text    for nick    in browser.find_elements(By.CLASS_NAME,"u_cbox_nick")]
#             id_list      = [id.text      for id      in browser.find_elements(By.CLASS_NAME,"u_cbox_id")]
#             comment_list = [content.text for content in browser.find_elements(By.CLASS_NAME,"u_cbox_contents")]
#             comment_info = [nick_list, id_list, comment_list]
#             browser.switch_to.default_content() # iframe 댓글 영역 이동

#             # 정보 일괄 취합
#             single_info=[subject, score_average, score_count, heart_count, comment_info]
#             total_info.append(single_info)
#             print()
#             print()
#             print(subject)
#             check_old_total_info = len(old_total_info)-1
#             if check_index < len(old_total_info)-1:
#                 check_change_info(old_total_info[check_index], single_info)
#             else:
#                 print(subject, "는 신규 작품이므로 이후부터 체크됩니다.")
            
#             check_index = check_index + 1

#             if stop_subject == subject:
#                 print('마지막화 입니다. 종료합니다.')
                
#                 with open('C:/PythonWorkSpace/project_web_scraping/spesial_interview_old.pickle', 'wb') as fw:
#                     pickle.dump(total_info, fw)
#                 break

#             next_part = browser.find_element(By.XPATH, "//*[@id='nextVolumeBtn']").click()

#         except:
#             break
#     browser.quit()

            

# if __name__ == "__main__":
#     while True:
#         scrape_special_interview()
#         voice_notice='''전 작품 체크가 끝났습니다.
#         60초 후 재진행 됩니다.'''
#         print(voice_notice)
#         text_to_speech(voice_notice)
#         time.sleep(60)
























# def create_soup(url):
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     return soup


# def get_single_chapter_info(url):
#     # options = webdriver.ChromeOptions()
#     # options.headless = True
#     # options.add_argument("window-size=1920x1080")
#     # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

#     # browser = webdriver.Chrome(options=options)
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(10)
#     browser.maximize_window()
#     browser.get(url) # url 로 이동

#     time.sleep(3)
#     try:
#         score_average = browser.find_element(By.XPATH, "//*[@id='currentStarScore']").text
#         score_count = browser.find_element(By.XPATH, "//*[@id='currentStarScoreCount']").text
#         heart_count = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em").text
#         browser.switch_to.frame('nCommentIframe')

#         nick_list    = [nick.text    for nick    in browser.find_elements(By.CLASS_NAME,"u_cbox_nick")]
#         id_list      = [id.text      for id      in browser.find_elements(By.CLASS_NAME,"u_cbox_id")]
#         content_list = [content.text for content in browser.find_elements(By.CLASS_NAME,"u_cbox_contents")]
#         content_info = [nick_list, id_list, content_list]
#         browser.switch_to.default_content()
#     finally:
#         browser.quit()

#     return [score_average, score_count, heart_count, content_info]


# def scrape_special_interview():
#     print("[특별한 면접]")
#     page_index = 1
#     base_url = "https://novel.naver.com/"
#     url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"
#     soup = create_soup(url)

#     page_list = soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("a",attrs={"class":"NPI=a:page"})
#     max_page_index = int(page_list[len(page_list)-1].get_text().strip())
#     print(f'최대 페이지 {max_page_index}')

#     for page_index in range(1, max_page_index+1):
#         page_url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=" + str(page_index)
        
#         subject_list_soup = create_soup(page_url)
#         subject_list = subject_list_soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})


#         for subject_index in range(len(subject_list)):
#             single_subject = subject_list[subject_index].find("p", attrs={"class":"subj"}).get_text().strip()
#             single_link = base_url + subject_list[subject_index].a["href"]
#             single_info = [single_subject]
#             single_info.extend(get_single_chapter_info(single_link))
#             # single_info = get_single_chapter_info(single_link)

#             print( single_info )

# def text_to_speech(input_text):
#     s = gTTS( input_text, lang='ko')
#     s.save('input_text.mp3')
#     playsound('input_text.mp3') 


# def test_page_parsing():
#     # 테스트 페이지
#     url = "https://novel.naver.com/best/detail?novelId=1019899&volumeNo=1"

#     browser = webdriver.Chrome()
#     browser.implicitly_wait(2)
#     browser.maximize_window()

#     #시작 URL로 변경
#     browser.get(url) # url 로 이동
#     time.sleep(5)
#     browser.switch_to.frame('nCommentIframe') # iframe 댓글 영역 이동
#     browser.find_element(By.XPATH,"//*[@id='cbox_module']/div/div[6]/div/a[2]").click()
#     browser.switch_to.default_content() # iframe 댓글 영역 이동
    
    
#     time.sleep(1000)

#     # browser.find_element(By.XPATH, "//*[@id='volume1']/a").click()

# def text_to_speech():
#     gSound = gTTS( "'01화. 전쟁터로 고고~ 작품 변경사항, , 별점참여가 기존 189명에서, 현재 190명로 변경, , 하트가 242에서, 현재 243로 변경, '", lang='ko')
#     gSound.save('test.mp3')
#     print("1")
#     media_player = vlc.MediaPlayer()
#     media=vlc.Media('test.mp3')
#     media_player.set_media(media)
#     media_player.play()
    
#     print("2")
#     media.play()
#     print("3")


# import re
# import requests
# import random
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from gtts import gTTS
# import vlc
# from mutagen.mp3 import MP3
# import pymysql

# global mydb
# global mycursor

# def connect_stat_db():
#     global mydb
#     global mycursor
    
#     mydb = pymysql.connect( host='127.0.0.1', port=5909, user='cho', passwd='Qwer1234!',db='cho_db', charset='utf8')
#     mycursor = mydb.cursor()

# def insert_stat_info(stat_in_db):
#     global mydb
#     global mycursor
    
#     sql = "INSERT INTO spesial_interview_tb \
#         (subject, score_average, score_count, heart_count, comment_count, view_count) \
#             VALUES (%s, %s, %s, %s, %s, %s)"
#     val = (stat_in_db[0], stat_in_db[1], stat_in_db[2], stat_in_db[3], stat_in_db[4], stat_in_db[5])

#     mycursor.execute(sql, val)
#     mydb.commit()

# if __name__ == "__main__":
#     # scrape_special_interview()
#     # text_to_speech()
#     #test_page_parsing()
#     connect_stat_db()
#     insert_stat_info(["test", 0.09, 2, 3, 4, 5])

















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time

# driver = webdriver.Chrome()
# driver.maximize_window()

# url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"
# driver.get(url)

# click_area = driver.find_element_by_xpath("//*[@id='volume1']/a")
# click_area.click()
# print('10초 대기')
# time.sleep(10)
# print('')
# driver.switch_to.frame('nCommentIframe')
# element       = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cbox_module_wai_u_cbox_content_wrap_tabpanel"))).find
# print(print(element.text))
# driver.switch_to.default_content()


# # if iframe:
# #     print('프레임을 찾았습니다.')
# # else:
# #     print('프레임을 못찾았어요 ㅠ.ㅠ')


# # driver.switch_to.default_content()



# # search_area = driver.find_element_by_class_name("srch_area").find_element_by_id("searchKeyword")
# # search_area.clear()
# # search_area.send_keys("특별한 면접")
# # search_area.send_keys(Keys.RETURN)
# # driver.find_element((By.XPATH("//*[@id='searchKeyword']"))).sendKeys("your value")
# # elem=driver.find_element((By.ID("searchKeyword"))).send_keys("my_id")
# # driver.find_element_by_id("searchKeyword").click()



# # driver.switch_to.frame('nCommentIframe')


# # driver.switch_to.default_content()



# # import re
# # import requests
# # import random
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from bs4 import BeautifulSoup

# # def create_soup(url):
# #     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# #     res = requests.get(url, headers=headers)
# #     res.raise_for_status()
# #     soup = BeautifulSoup(res.text, "lxml")
# #     return soup

# # def get_single_chapter_info(url):
# #     options = webdriver.ChromeOptions()
# #     # options.headless = True
# #     # options.add_argument("window-size=1920x1080")
# #     # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

# #     browser = webdriver.Chrome(options=options)
# #     browser.implicitly_wait(10) # seconds
# #     browser.maximize_window()
# #     browser.get(url) # url 로 이동

# #     try:
# #         score_average = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScore']"))).text
# #         score_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScoreCount']"))).text       
# #         heart_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em"))).text
# #         # comment_orner   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cbox_module_wai_u_cbox_content_wrap_tabpanel']/ul/li[1]/div[1]/div/div[1]/span[1]/span/span/span[1]/span"))).text

# #         # comment_orner   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_list")))
# #         # soup = BeautifulSoup(browser.page_source, "lxml")

# #         with open("1111_result.html", "w", encoding="utf8") as f:
# #             f.write(browser.page_source)

# #     finally:
# #         print('finally 들어왔어')
# #         browser.quit()


        
# #     comment_list  = ''
# #     name = soup.find("div", attrs={"id":"cbox_module"})
# #     # name = soup.find("div", attrs={"id":"cbox_module_wai_u_cbox_content_wrap_tabpanel"})

# #     if name:
# #         print('name 결과가 있어요. ㅋㅋㅋ')
# #         print(name)
# #     else:
# #         print('name 널이에요')

# #     # name = soup.find("ul", attrs={"class":"u_cbox_list"}).find_all("span", attrs={"class":"u_cbox_nick"})

# #     print("score_average : " + score_average )
# #     print("score_count   : " + score_count   )
# #     print("heart_count   : " + heart_count   )
# #     # print("comment_list  : " + comment_list  )
# #     # print("name          : " + name          )


# #     # return [score_average, score_count, heart_count, comment_list]
# #     return [score_average, score_count, heart_count]

# # def scrape_special_interview():
# #     print("[특별한 면접]")
# #     page_index = 1
# #     base_url = "https://novel.naver.com/"
# #     url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"
# #     soup = create_soup(url)

# #     # page_list=soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("strong")
    
# #     # news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
# #     # with open("result.html", "w", encoding="utf8") as f:
# #     #     f.write(soup.contents)

# #     page_list = soup.find("div", attrs={"class":"paging NE=a:lst"}).find_all("a",attrs={"class":"NPI=a:page"})
# #     max_page_index = int(page_list[len(page_list)-1].get_text().strip())
# #     print(f'최대 페이지 {max_page_index}')

# #     for page_index in range(1, max_page_index+1):
# #         page_url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=" + str(page_index)
# #         # print("page_index : "+ page_url)
        
# #         subject_list_soup = create_soup(page_url)
# #         subject_list = subject_list_soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})


# #         for subject_index in range(len(subject_list)):
# #             single_subject = subject_list[subject_index].find("p", attrs={"class":"subj"}).get_text().strip()
# #             single_link = base_url + subject_list[subject_index].a["href"]

# #             ret_v_list = get_single_chapter_info(single_link)
# #             # print(ret_v_list)



# #             # print( single_subject )
# #             # print( single_link )
# #             time.sleep(10)
# #             break


# # if __name__ == "__main__":
# #     scrape_special_interview() # 오늘의 날씨 정보 가져오기









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
#     # options = webdriver.ChromeOptions()
#     # options.headless = True
#     # options.add_argument("window-size=1920x1080")
#     # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

#     # browser = webdriver.Chrome(options=options)
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(10)
#     browser.maximize_window()
#     browser.get(url) # url 로 이동

#     time.sleep(3)
#     try:
#         score_average = browser.find_element_by_xpath("//*[@id='currentStarScore']").text
#         score_count = browser.find_element_by_xpath("//*[@id='currentStarScoreCount']").text
#         heart_count = browser.find_element_by_xpath("//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em").text
#         # search_area = driver.find_element_by_class_name("srch_area").find_element_by_id("searchKeyword")
#         # driver.find_element((By.XPATH("//*[@id='searchKeyword']"))).sendKeys("your value")
#         # elem=driver.find_element((By.ID("searchKeyword"))).send_keys("my_id")
#         # driver.find_element_by_id("searchKeyword").click()
#         # score_average = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScore']"))).text
#         # score_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='currentStarScoreCount']"))).text       
#         # heart_count   = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em"))).text
#         browser.switch_to.frame('nCommentIframe')
#         # element       = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "cbox_module_wai_u_cbox_content_wrap_tabpanel"))).find_elements_by_class_name("u_cbox_nick").text
#         comment_info_list = browser.find_elements_by_class_name("u_cbox_area")
        
#         print()
#         print(element)
#         print()
#         # soup = BeautifulSoup(browser.page_source, "lxml")
#         # print(soup.prettify)
#         browser.switch_to.default_content()
#     finally:
#         time.sleep(1000)
#         browser.quit()

#     return [score_average, score_count, heart_count]


# def scrape_special_interview():
#     print("[특별한 면접]")
#     page_index = 1
#     base_url = "https://novel.naver.com/"
#     url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"
#     soup = create_soup(url)

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
#             single_info = [single_subject]
#             single_info.extend(get_single_chapter_info(single_link))
#             # single_info = get_single_chapter_info(single_link)

#             print( single_info )



# if __name__ == "__main__":
#     scrape_special_interview()



# import re
# import requests
# import random
# import time
# import pickle
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from gtts import gTTS
# import vlc
# from mutagen.mp3 import MP3
# import pymysql



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

# global mydb
# global mycursor

# def connect_stat_db():
#     global mydb
#     global mycursor
    
#     mydb = pymysql.connect( host='127.0.0.1', port=5909, user='cho', passwd='Qwer1234!',db='cho_db', charset='utf8')
#     mycursor = mydb.cursor()

# def insert_stat_info(stat_in_db):
#     global mydb
#     global mycursor
    
#     sql = "INSERT INTO spesial_interview_tb \
#         (subject, score_average, score_count, heart_count, comment_count, view_count) \
#             VALUES (%s, %s, %s, %s, %s, %s)"
#     val = (stat_in_db[0], stat_in_db[1], stat_in_db[2], stat_in_db[3], stat_in_db[4], stat_in_db[5])

#     mycursor.execute(sql, val)
#     mydb.commit()


# def text_to_speech(input_text):
#     checkval=len(input_text)
#     gSound = gTTS( input_text, lang='ko', slow=False)
#     gSound.save('inputtext.mp3')
#     media_player = vlc.MediaPlayer()
#     media=vlc.Media('inputtext.mp3')
#     audio = MP3("inputtext.mp3")
#     play_time = audio.info.length
#     media_player.set_media(media)
#     media_player.play()
#     time.sleep(play_time)

# def check_change_info(old_total, new_total):
#     change_info_flag=False
#     voice_notice=""

#     subject_db = ""
#     score_average_db = score_count_db = heart_count_db = comment_count_db = view_count_db = 0

#     simple_subject = old_total[0].split('화')
#     subject_db = simple_subject[0]+"화"
#     voice_notice = "{0}화. ".format( simple_subject[0])

#     if old_total[1] != new_total[1]:
#         score_average_db = round( float(new_total[1].strip()) - float(old_total[1].strip()), 3)
#         voice_notice += ", 평점 {0} 추가, " .format( score_average_db )
#         change_info_flag = True

#     if old_total[2] != new_total[2]:
#         score_count_db = int(new_total[2].replace("명","").strip()) - int(old_total[2].replace("명","").strip())
#         voice_notice += ", 별점참여 {0} 추가, " .format( score_count_db )
#         change_info_flag = True

#     if old_total[3] != new_total[3]:
#         heart_count_db = int(new_total[3].strip()) - int(old_total[3].strip())
#         voice_notice += ", 하트 {0} 추가, " .format( heart_count_db )
#         change_info_flag = True
    
#     old_comment_list = old_total[4]
#     new_comment_list = new_total[4]

#     old_comment_list_cnt=len(old_comment_list[0])
#     new_comment_list_cnt=len(new_comment_list[0])

#     comment_count_db = 0
#     if new_comment_list_cnt > 0:
#         loop_comment_index=range(0,new_comment_list_cnt)
#         for new_comment_index in loop_comment_index:
#             if old_comment_list_cnt > 0:
#                 continue_boolean=False

#                 for old_comment_index in range(0,old_comment_list_cnt):
#                     if old_comment_list[0][old_comment_index] == new_comment_list[0][new_comment_index]:
#                         try:
#                             if old_comment_list[2][old_comment_index] == new_comment_list[2][new_comment_index]:
#                                 continue_boolean=True
#                                 break
#                         except IndexError:
#                             continue_boolean=True
#                             continue
                
#                 if continue_boolean:
#                     continue

#             try:
#                 voice_notice+="추가 {0}님의 댓글, {1}" .format( new_comment_list[0][new_comment_index], new_comment_list[2][new_comment_index] )
#                 change_info_flag = True
#                 comment_count_db+=1
#             except IndexError:
#                 voice_notice+="추가 {0}님의 댓글, 클린봇으로 삭제되었습니다." .format( new_comment_list[0][new_comment_index])
#                 change_info_flag = True
#                 comment_count_db+=1
    
#     if( change_info_flag ):
#         print(voice_notice)
#         text_to_speech(voice_notice)
#         insert_stat_info([subject_db, score_average_db, score_count_db, heart_count_db, comment_count_db, view_count_db])

# def scrape_special_interview():
#     print("[특별한 면접]")
#     starturl = "https://novel.naver.com/best/list?novelId=1019899"
    
#     # 테스트 페이지
#     url = "https://novel.naver.com/best/list?novelId=1019899&order=Oldest&page=1"

#     options = webdriver.ChromeOptions()
#     options.headless = True
#     options.add_argument("window-size=1920x1080")
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
#     browser = webdriver.Chrome(options=options)

#     # browser = webdriver.Chrome()
#     browser.implicitly_wait(2)
#     # browser.maximize_window()


#     #제일 마지막화 제목
#     browser.get(starturl) # start url 로 이동
#     soup = BeautifulSoup(browser.page_source, "lxml")
#     subject_list = soup.find("ul", attrs={"class":"list_type2 v3 league_num NE=a:lst"}).find_all("li",attrs={"class":"volumeComment"})
#     stop_subject = subject_list[0].find("p", attrs={"class":"subj"}).get_text().strip()
#     stop_subject = stop_subject[:stop_subject.find('\n')]


#     #시작 URL로 변경
#     browser.get(url) # url 로 이동
#     browser.find_element(By.XPATH, "//*[@id='volume1']/a").click()


#     with open('C:/PythonWorkSpace/project_web_scraping/spesial_interview_old.pickle', 'rb') as rf:
#         old_total_info = pickle.load(rf)

#     # print_contents_info(old_total_info)

#     total_info=[] # 전체 정보를 저장할 변수

#     check_index = 0 #루프 횟수 

#     while True:
#         try:
#             time.sleep(3)
#             subject = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[2]/h2").text
#             subject = subject[:subject.find('\n')]
#             score_average = browser.find_element(By.XPATH, "//*[@id='currentStarScore']").text
#             score_count = browser.find_element(By.XPATH, "//*[@id='currentStarScoreCount']").text
#             heart_count = browser.find_element(By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]/div[1]/a/em").text

#             browser.switch_to.frame('nCommentIframe') # iframe 댓글 영역 이동
#             nick_list    = [nick.text    for nick    in browser.find_elements(By.CLASS_NAME,"u_cbox_nick")]
#             id_list      = [id.text      for id      in browser.find_elements(By.CLASS_NAME,"u_cbox_id")]
#             comment_list = [content.text for content in browser.find_elements(By.CLASS_NAME,"u_cbox_contents")]
#             comment_info = [nick_list, id_list, comment_list]
#             browser.switch_to.default_content() # iframe 댓글 영역 이동

#             # 정보 일괄 취합
#             single_info=[subject, score_average, score_count, heart_count, comment_info]
#             total_info.append(single_info)
#             print()
#             print()
#             print(subject)
#             check_old_total_info = len(old_total_info)
#             if check_index < len(old_total_info):
#                 check_change_info(old_total_info[check_index], single_info)
#             else:
#                 print(subject, "는 신규 작품이므로 이후부터 체크됩니다.")
            
#             check_index = check_index + 1

#             if stop_subject == subject:
#                 print('마지막화 입니다. 종료합니다.')
                
#                 with open('C:/PythonWorkSpace/project_web_scraping/spesial_interview_old.pickle', 'wb') as fw:
#                     pickle.dump(total_info, fw)
#                 break

#             next_part = browser.find_element(By.XPATH, "//*[@id='nextVolumeBtn']").click()

#         except:
#             break
#     browser.quit()

            

# if __name__ == "__main__":
#     while True:
#         connect_stat_db()
#         scrape_special_interview()
#         voice_notice='''전 작품 체크가 끝났습니다.
#         60초 후 재진행 됩니다.'''
#         print(voice_notice)
#         # text_to_speech(voice_notice)
#         # time.sleep(60)



import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결


global mydb
global mycursor

def connect_stat_db():
    global mydb
    global mycursor
    
    mydb = pymysql.connect( host='127.0.0.1', port=5909, user='cho', passwd='Qwer1234!',db='cho_db', charset='utf8')
    mycursor = mydb.cursor()

def disconnect_stat_db():
    mycursor.close()
    mydb.close()


def select_stat_info():
    global mydb
    global mycursor

    sql = "SELECT \
                num, \
                DATE_FORMAT(create_date,'%Y%m%d%H%i%s') AS credate, \
                subject, \
                SUM(view_count) \
            FROM  \
                simple_stat_tb \
            GROUP BY create_date \
            ORDER BY create_date desc\
            LIMIT 100;"

    mycursor.execute(sql)

    # 데이타 Fetch
    rows = mycursor.fetchall()
    mydb.commit()
    return rows


def stat_chart_update():
            # DB에서 데이터 가져오기
            stat_rows=select_stat_info()

            # 각 데이터 배열로 생성
            credate=[stat_row[1] for stat_row in stat_rows]
            view_counts=[stat_row[3] for stat_row in stat_rows]

            credate.reverse()
            view_counts.reverse()

            # 최대 몇건까지 보여줄지 정의
            view_limit =-20
            credate=credate[view_limit:]
            view_counts=view_counts[view_limit:]

            # x축 재정의
            check_day_str=''
            fin_x_list=[]
            for index, groupKey in enumerate(credate):
                if index == 0:
                    continue
                if check_day_str != groupKey[4:8]:
                    check_day_str=groupKey[4:8]
                    fin_x_list.append(groupKey[4:6] + " / " + groupKey[6:8])
                else:
                    fin_x_list.append(groupKey[8:10] + ":" + groupKey[10:12])


            # x축 재정의
            # 표 여유를 위해 축 표시 보정
            fin_y_list=[]
            for idx in range(len(view_counts)):
                if idx == 0:
                    continue
                fin_y_list.append((view_counts[idx] - view_counts[idx-1])%10000)
            # fin_x_list=date_list[1:]

            y_min = min(fin_y_list) - 100
            y_max = max(fin_y_list) + 100

            # 표 그리기

            plt.ylim([y_min, y_max])
            # plt.xticks(rotation=90)
            plt.plot(fin_x_list, fin_y_list, 'g', linestyle='--', linewidth=1, marker='o', markersize=3, markerfacecolor='red')
            plt.show(block=False)
            time.sleep(10)
            print("@#@#!@#!@#!@#")
            # plt.pause(180)
            # plt.close()




if __name__ == "__main__":
    connect_stat_db()

    plt.style.use('seaborn')
    plt.figure(figsize=(14, 7)) # 그래프 크기
    plt.xlabel('TIME ---->', color='red', loc='right') # left, center, right 
    plt.ylabel('VIEW COUNT', color='#00aa00', loc='top') # top, center, bottom            
    plt.title('spesial_interview') # 그래프 제목

    try:
        while True:
            stat_chart_update()
            
            

    except Exception as err:
        print(err)



