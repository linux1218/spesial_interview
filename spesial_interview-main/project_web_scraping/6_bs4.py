import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
#url="https://upbit.com/home"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
# print(soup.title.get_text)

print(soup.find("a", att ))
