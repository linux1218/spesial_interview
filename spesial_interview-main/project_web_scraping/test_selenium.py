from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


def test_selenium():
    # 테스트 페이지
    url = "https://www.naver.com"
    browser = webdriver.Chrome("C:/Users/21801004/Desktop/python/chromedriver.exe")
    wait = WebDriverWait(browser, 10)
    # browser.maximize_window()
    
    #시작 URL로 변경
    browser.get(url) # url 로 이동

    # time.sleep(3)

    # soup = BeautifulSoup(browser.page_source, "lxml")
    # find_check = browser.find_element(By.XPATH, "//*[@id='NM_THEME_CONTAINER']/div[1]/div/ul/li[2]/a[2]") #xpath 로 접근



    # find_check = browser.find_elements(By.CLASS_NAME, "theme_category") #class 로 접근
    # find_check[1].click()  # class name에 해당하는 놈 가져와서 몇번째 놈 골라서 클릭 가능

    # items = soup.find_all("li", attrs={"class":"theme_item"}).find("em", attrs={"class":"theme_category"})

    # browser.find_element_by_id('ke_kbd_btn') #id 속성으로 접근
    # browser.find_element_by_link_text('회원가입')    #링크가 달려 있는 텍스트로 접근
    # browser.find_element_by_css_selector('#account > div > a')   #css 셀렉터로 접근
    # browser.find_element_by_name('join') #name 속성으로 접근
    # browser.find_element_by_partial_link_text('가입')  #링크가 달려 있는 엘레먼트에 텍스트 일부만 적어서 해당 엘레먼트에 접근
    # browser.find_element_by_tag_name('input')    #태그 이름으로 접근

    # browser.find_element_by_tag_name('input').find_element_by_tag_name('a')  #input 태그 하위태그인 a 태그에 접근
    # browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]').find_element_by_name('join')
    #xpath 로 접근한 엘레먼트의 안에 join 이라는 속성을 가진 tag 엘레먼트에 접근

    time.sleep(100)

def pprint(arr):
    print()
    print()
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)
    print()
    print()


def test_matplotlib():
    plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend(loc=(0, 1))
    # plt.legend(loc=(1.0, 1.0))

    plt.show()

def test_numpy():
    arr = [1, 2, 3]
    a = np.array([1, 2, 3])
    pprint(a)

    arr = [(1,2,3), (4,5,6)]
    a= np.array(arr, dtype = float)
    pprint(a)

    arr = np.array([[[1,2,3], [4,5,6]], [[3,2,1], [4,5,6]]], dtype = float)
    a= np.array(arr, dtype = float)
    pprint(a)

    a = np.zeros((3, 4))
    pprint(a)

    a = np.ones((2,3,4),dtype=np.int16)
    pprint(a)

    a = np.full((2,2),7)
    pprint(a)

    a = np.eye(4)
    pprint(a)

    a = np.empty((4,2))
    pprint(a)

    a = np.array([[1,2,3], [4,5,6]])
    b = np.ones_like(a)
    pprint(a)
    pprint(b)

    a = np.linspace(0, 1, 5)
    pprint(a)

    plt.plot(a, 'o')
    plt.show()

    a = np.arange(0, 10, 2, np.float)
    pprint(a)

if __name__ == "__main__":
    # test_selenium()
    # test_matplotlib()
    test_numpy()