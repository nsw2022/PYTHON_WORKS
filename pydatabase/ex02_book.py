# testdb -> book 테이블
import sqlite3


def getconn():
    conn = sqlite3.connect('E:/NSW/sqlworks/pydb/test.db')
    return conn
# DB 생성
def create():
    conn = getconn()
    cursor = conn.cursor() # cursor 객체는 sql을 조작함
    sql = '''
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            page INTEGER
        )
        
    '''
    cursor.execute(sql) # 실행
    conn.commit() # 커밋 완료
    cursor.close() # 연결 닫기

# 책추가
def insert():
    conn = getconn()
    cursor = conn.cursor()
    # 동적 바인딩 방식
    sql = 'INSERT INTO book(title, author, page) ' \
          'VALUES(?,?,?)'
    # cursor.execute(sql,("혼자 공부하는 자바","신용권",600))
    cursor.execute(sql,("python projects","켄 유엔스",500))
    conn.commit()
    conn.close()

# 책 전체 검색
def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = 'SELECT * FROM book'
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs) # 리스트로 출력
    for i in rs:
        print(i) # 튜플로 출력
    conn.close()

# 책 1권 검색
def select_one():
    conn = getconn()
    cursor = conn.cursor()
    # sql = 'SELECT * FROM book WHERE book_no = 2'
    sql = 'SELECT * FROM book WHERE book_no = ?'
    cursor.execute(sql,(2, )) # 튜플 자료구조이므로 1개일때 (,사용)
    rs = cursor.fetchone()
    print(rs)
    conn.close()

# 책 수정
def update():
    conn = getconn()
    cursor = conn.cursor()
    # 책번호 2번인 책의 페이지를 650페이로 변경
    sql = 'UPDATE book SET page = ? WHERE book_no = ?'
    cursor.execute(sql,(650,2))
    conn.commit()
    conn.close()

# 책번호 1번인책 삭제
def delete():
    conn = getconn()
    cursor = conn.cursor()
    # 책번호 1번인책 삭제
    sql = "DELETE FROM book WHERE book_no=?"
    cursor.execute(sql, (1,))
    conn.commit()
    conn.close()

# print(getconn(),"연결 객체 생성")
# create()
# insert()
update()
# delete()
select()
# select_one()
