import requests
url = "https://comic.naver.com/webtoon/weekday"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

try:
    res = requests.get( url, headers=headers)
    res.raise_for_status()
    with open("result_html.html", "w", encoding="utf8") as f:
        f.write(res.text)
except requests.ConnectionError:
    print( 'connect 에러가 발생했습니다.')
