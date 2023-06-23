import sqlite3

def getconn():
    conn = sqlite3.connect("E:/NSW/pydb/mydb.db")
    return conn

def select():
    conn = getconn()
    # print()
    cursor = conn.cursor() # cursor 객체 꺼내옴
    sql = "SELECT * FROM employee"
    cursor.execute(sql) # execute() 함수 - 모든 조작(CRUD)를 수행하는 함수
    # 전체 검색 - fetchall(), 특정 1개 검색 fetchone()
    rs = cursor.fetchall() # 자료구조 리스트 여러개로 받기을수도 있기 때문
    # print(rs) # 확인 해보면 리스트 안의 요소가 튜플 수정 불가
    for i in rs:
        print(i)

    conn.close()
def insert():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e103','안산',22,10000)"
    cursor.execute(sql)
    conn.commit() # 삽입, 수정, 삭제시 반드시 커밋해야함
    conn.close()

def update():
    conn = getconn()
    cursor = conn.cursor()
    sql = "UPDATE employee SET age = 40 WHERE name = '추신수'"
    cursor.execute(sql)
    conn.commit() # 삽입, 수정, 삭제시 반드시 커밋해야함
    conn.close()

def select1(): # 특정요소 검색
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM employee WHERE empid='e103'"
    cursor.execute(sql)
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete():# 사원번호가 e102 삭제
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM employee WHERE empid = 'e102'"
    cursor.execute(sql)
    conn.commit() # 삽입, 수정, 삭제시 반드시 커밋해야함
    conn.close()

# 메인 영역에서 호출 해서 사용
# insert()
# update()
# select1()
# delete()
select()

