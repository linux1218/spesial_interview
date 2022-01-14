import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

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
            view_limit =-60
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
            plt.style.use('seaborn')
            plt.figure(figsize=(14, 7)) # 그래프 크기
            plt.xlabel('TIME ---->', color='red', loc='right') # left, center, right 
            plt.ylabel('VIEW COUNT', color='#00aa00', loc='top') # top, center, bottom            
            plt.title('spesial_interview') # 그래프 제목
            plt.ylim([y_min, y_max])
            plt.xticks(rotation=90)
            plt.plot(fin_x_list, fin_y_list, 'g', linestyle='--', linewidth=1, marker='o', markersize=3, markerfacecolor='red')
            plt.show(block=False)
            plt.pause(180)
            plt.close()




if __name__ == "__main__":
    connect_stat_db()

    try:
        while True:
            stat_chart_update()
            

    except Exception as err:
        print(err)



