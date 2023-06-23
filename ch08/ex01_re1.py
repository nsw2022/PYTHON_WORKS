# re 모듈을 import
import re
# /정규표현식/g - > re.compile("정규표현식")
# 소문자 a부터 z까지 일치하는 문자를 반복해서 찾음
# math() - 일치하는 문자를 찾는 함수
# search - 일치하는 문자를 찾느 함수
p = re.compile("[a-z]+")

m1 = p.match('afternoon')
print(m1) # m1 객체
print(m1.group()) # 문자열 출력

m2 = p.match('2023 good luck') # 처음부터 일지해야 찾음
print(m2) # 숫자로시작해서 못찾음

s1 = p.search('2023 good luck') # 전체중에 일치하면 찾음
print(s1)
print(s1.group())
