import oracledb

def getconn():
    # dsn data source name 의 준말 ip:포트번호/오라클 버전
    conn = oracledb.connect(user='c##mydb', password='mydb',
                            dsn='localhost:1521/xe')
    return conn

# print(getconn())
def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM pytest"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO pytest VALUES('행운을 빌어요~~~')"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def delete():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM pytest WHERE message = '행운을 빌어요~~~'"
    cursor.execute(sql)
    conn.commit()
    conn.close()

# insert()
# delete()
select()

