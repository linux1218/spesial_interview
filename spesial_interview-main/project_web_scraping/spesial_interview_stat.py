
# DB 생성정보
# create user cho@localhost identified by 'Qwer1234!';
# create user cho@'%' identified by 'Qwer1234!';
# create database cho_db default character set utf8;
# grant all privileges on cho_db.* to 'cho'@'%'
# ####grant all privileges on cho_db.* to 'cho'@'%' identified by 'Qwer1234!';


# DROP TABLE spesial_interview_stat_tb;
# CREATE TABLE `spesial_interview_stat_tb`(
#   `num`            BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#   `create_date`    DATETIME DEFAULT CURRENT_TIMESTAMP,
#   `subject`        VARCHAR(128) NOT NULL,
#   `score_average`  NUMERIC,
#   `score_count`    NUMERIC,
#   `heart_count`    NUMERIC,
#   `comment_count`  NUMERIC,
#   `view_count`     NUMERIC
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# ALTER TABLE spesial_interview_stat_tb ADD INDEX IDX_s_i_stat_tb_1(create_date ASC);
# ALTER TABLE spesial_interview_stat_tb ADD INDEX IDX_s_i_stat_tb_2(subject ASC);


import time
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결


global mydb
global mycursor
global browser
global view_count_list

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
            stat_rows=select_stat_info()
            seqnum=[stat_row[0] for stat_row in stat_rows]
            credate=[stat_row[1] for stat_row in stat_rows]
            subjects=[stat_row[2] for stat_row in stat_rows]
            score_counts=[stat_row[3] for stat_row in stat_rows]
            heart_counts=[stat_row[4] for stat_row in stat_rows]
            comment_counts=[stat_row[5] for stat_row in stat_rows]
            view_counts=[stat_row[6] for stat_row in stat_rows]

            data = {
                'seqnum' : seqnum,
                'credate' : credate,
                'subjects' : subjects,
                'score_counts' : score_counts,
                'heart_counts' : heart_counts,
                'comment_counts' : comment_counts,
                'view_counts' : view_counts
            }

            df = pd.DataFrame(data)
            df.reset_index(drop=True, inplace=True)
            df.set_index('seqnum', inplace=True)

            #조건 선택
            result = df[['credate', 'view_counts']]
            result_fin = result.groupby('credate').sum()
            groupKeys = result['credate'].unique()
            view_counts = [ view_count for view_count in result_fin['view_counts']]

            print(result_fin)
            print(view_counts)

            # X 축
            view_counts_len = len(view_counts)
            view_count_range=range(view_counts_len-2) # 첫번쨰 시작과, 마지막은 제외
            x_min = 0
            x_max = view_counts_len

            # Y 축            
            view_count_list=[]
            for idx in range(view_counts_len-1):
                if idx == 0:
                    continue
                print( idx, view_counts[idx], view_counts[idx-1])
                view_count_list.append(view_counts[idx]-view_counts[idx-1])
            y_min = min(view_count_list) - 50 # 표 여유를 위해 축 표시 보정
            y_max = max(view_count_list) + 50 # 표 여유를 위해 축 표시 보정
            
            # 표 그리기
            plt.style.use('seaborn')
            plt.figure(figsize=(16, 8)) # 그래프 크기
            plt.xlabel('TIME ---->', color='red', loc='right') # left, center, right 
            plt.ylabel('VIEW COUNT', color='#00aa00', loc='top') # top, center, bottom            
            plt.title('spesial_interview') # 그래프 제목
            plt.xlim([x_min, x_max])
            plt.ylim([y_min, y_max])
            plt.plot(view_count_range, view_count_list, 'g', linestyle='--', linewidth=1, marker='o', markersize=3, markerfacecolor='red')
            plt.show()

            time.sleep(10)



if __name__ == "__main__":
    connect_stat_db()

    try:
        while True:
            stat_chart_update()
            

    except Exception as err:
        print(err)



