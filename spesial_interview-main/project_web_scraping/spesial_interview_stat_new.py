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
            num, DATE_FORMAT(create_date,'%Y%m%d%H%i%s') AS credate, \
                replace( subject, '화', '') as subject, score_count, \
                heart_count, comment_count, view_count \
                FROM \
                spesial_interview_stat_tb \
                ORDER BY create_date;"
    mycursor.execute(sql)

    # 데이타 Fetch
    rows = mycursor.fetchall()
    mydb.commit()
    return rows


def stat_chart_update():
            # DB에서 데이터 가져오기
            stat_rows=select_stat_info()

            # 각 데이터 배열로 생성
            seqnum=[stat_row[0] for stat_row in stat_rows]
            credate=[stat_row[1] for stat_row in stat_rows]
            subjects=[stat_row[2] for stat_row in stat_rows]
            score_counts=[stat_row[3] for stat_row in stat_rows]
            heart_counts=[stat_row[4] for stat_row in stat_rows]
            comment_counts=[stat_row[5] for stat_row in stat_rows]
            view_counts=[stat_row[6] for stat_row in stat_rows]

            # 기본 데이터 생성
            data = {
                'seqnum' : seqnum,
                'credate' : credate,
                'subjects' : subjects,
                'score_counts' : score_counts,
                'heart_counts' : heart_counts,
                'comment_counts' : comment_counts,
                'view_counts' : view_counts
            }

            # DataFrame 생성 후 index 재생성
            df = pd.DataFrame(data)
            df.reset_index(drop=True, inplace=True)
            df.set_index('seqnum', inplace=True)

            # 필요한 데이터만 추출
            df = df[['credate', 'view_counts']].groupby('credate').sum()[-70:]
            check_count=[]
            for idx in range(len(df)-1):
                if idx == 0:
                    continue
                check_count.append((df['view_counts'].iloc[idx] - df['view_counts'].iloc[idx-1])%10000)
            df = df[1:-1]
            
            # x축 재정의
            check_day_str=''
            date_list=[]
            for groupKey in df.index:
                if check_day_str != groupKey[4:8]:
                    check_day_str=groupKey[4:8]
                    date_list.append(groupKey[4:6] + " / " + groupKey[6:8])
                else:
                    date_list.append(groupKey[8:10] + ":" + groupKey[10:12])

            # 표 여유를 위해 축 표시 보정
            y_min = min(check_count) - 50
            y_max = max(check_count) + 50

            # 표 그리기
            plt.style.use('seaborn')
            plt.figure(figsize=(14, 7)) # 그래프 크기
            plt.xlabel('TIME ---->', color='red', loc='right') # left, center, right 
            plt.ylabel('VIEW COUNT', color='#00aa00', loc='top') # top, center, bottom            
            plt.title('spesial_interview') # 그래프 제목
            plt.ylim([y_min, y_max])
            # plt.xticks(rotation=90)
            plt.plot(date_list, check_count, 'g', linestyle='--', linewidth=1, marker='o', markersize=3, markerfacecolor='red')
            plt.show(block=False)
            plt.pause(60)
            plt.close()




if __name__ == "__main__":
    connect_stat_db()

    try:
        while True:
            stat_chart_update()
            

    except Exception as err:
        print(err)



