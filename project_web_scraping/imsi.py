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


 

if __name__ == "__main__":    
    try:
        with open('C:/PythonWorkSpace/project_web_scraping/spesial_interview_old.pickle', 'rb') as rf:
            old_total_info = pickle.load(rf)

        fin_result_list=[]
        for old_total in old_total_info:
            old_comment_list = old_total[5]
            for old_comment_index in range(0,len(old_comment_list[0])):
                fin_result_list.append(old_comment_list[0][old_comment_index])

        fin_result_set=set(fin_result_list)

        temp_1=list(fin_result_set)

        print(len(temp_1))

        fin_str = "  ,  ".join(temp_1)

        print(fin_str)
    except Exception as err:
        print(err)



