# 변수의 선언과 사용
# 어떤 학생의 이름과 학년과 반을 출력
# 변수 이름 작성시 주의
# - 숫자로 시작할 수 없음, 공백을 허용하지 않음, 예약어 쓸수없음
name = '이하나'
#print(name)

grade = 2
#print(grade)

#class = 1 #class는 예약어임으로 사용불가
school_class = 1 
#print(school_class)
print(name + " 학생은 " +  str(grade) + "학년 "
      + str(school_class) +"반 입니다")


# 문자열에 따옴표 포함하기
say = "'힘내세요.' 라고 말했습니다."
print(say)
say2 = '"Python is very easy." he says'
print(say2)

# 문자열을 여러줄로 출력하기
song1 =  '''
    동해문과 백두산이 마르고 닳도록
    하느님이 보우하사 우리나라 만세
    '''
print(song1)
print('가\n'+'나\n'+'다\n')

## 진수 표현하기
num=10
b_num= 0b1010   # 2진수 표기법(0b를 붙힘)
print(b_num)

# 16진수 표기법(0x를 붙임) - 0x32f12(메모리 주소)
h_num = 0xa     
print(h_num)

# 진수 표현 내장 함수
print(bin(10)) #0b1010
print(bin(65))
print(hex(10)) #0x1010

# 아스키 코드의 문자
print(chr(48)) # 0
print(chr(65)) # A
