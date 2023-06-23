import  sqlite3

def getconn():
    conn = sqlite3.connect('E:/NSW/sqlworks/pydb/member.db')
    return conn
# board 테이블 연동
# board 테이블 생성
def create_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE board(
            bno INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEST NOT NULL,
            createdate DATETIME DEFAULT(datetime('now', 'localtime')),
            hit INTEGER DEFAULT 0,
            memberid TEXT NOT NULL,
            FOREIGN KEY(memberid) REFERENCES member(memberid) ON DELETE CASCADE
        )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("테이블생성")

def drop_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DROP TABLE board"
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 삭제 완료")

def insert_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO board(title, content, memberid) VALUES(?, ?, ?)"
    cursor.execute(sql,('가입인사','안녕하세요 노승우임돠','nsw1234'))
    conn.commit()
    conn.close()
    print("테이블 삽입 완료")

def select_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board"
    cursor.execute(sql)
    boardlist = cursor.fetchall()
    print(boardlist)
    for board in boardlist:
        print(board)
    conn.close()

# 함수 호출
# create_board()
# insert_board()
# drop_board()
select_board()

# member 테이블 연동
'''
def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM member"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = 'SELECT * FROM member' \
          ' WHERE memberid = ? AND password = ?'
    cursor.execute(sql,('test1234','!a12345678'))
    rs = cursor.fetchone()
    print(rs)
    conn.close()

# member 테이블 삽입
def insert():
    conn = getconn()
    cursor = conn.cursor()

    sql = "INSERT INTO member(memberid, password, name, gender)" \
          "VALUES(?,?,?,?)"
    cursor.execute(sql, ('today123', 'm123456$', '투데이', '여'))
    conn.commit()
    conn.close()
'''

# insert()
# select()
# select_one()
