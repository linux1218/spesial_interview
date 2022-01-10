import time
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

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


if __name__ == "__main__":
    connect_stat_db()

    try:
        while True:
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
            groupKeys = df.groupby('credate').size()

            for index, keyCount in enumerate(groupKeys):
                print(index, keyCount)
            
            print(groupKeys.columns[0])
            
            # for groupKey in groupKeys:
            #     filt = keyList['credate'] == groupKey 
            #     print(keyList[filt].count())

            print("##############")
            time.sleep(100)


            result = df[['credate', 'view_counts']]
            result_fin=result.groupby('credate').sum()

            print(result_fin)




            # print(result.groupby('credate').count)

            # plt.plot(result_fin)
            # plt.show()

            # df['credate'] = df['credate'].str.slice(start=6, stop=11)
            # result = df[['credate', 'view_counts']]
            # result_fin=result.groupby('credate')['view_counts'].sum()
            # result_fin=result.groupby('credate').sum()
            # print(result_fin['view_counts'])
            # plt.plot(result_fin['credate'], result_fin['view_counts'])
            # plt.plot(result_fin)
            # plt.show()

            # filt = (df['subjects'] == '105')
            # result=df.loc[(df['subjects'] == '105'), ['credate','view_counts']]
            # result['credate'] = result['credate'].str.slice(start=6, stop=11)
            # plt.plot(result['credate'], result['view_counts'])
            # plt.show()


            time.sleep(10000)
    except:
        disconnect_stat_db()



