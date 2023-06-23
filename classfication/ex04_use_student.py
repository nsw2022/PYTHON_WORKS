import student2
from student2 import Student

# 파일이름.클래스 이름
# st1 = student2.Student('이셋',3)
'''
st1 = Student('이셋',3)
print(st1)
'''

# 객체 리스트 생성
s = [
    Student("김하나", 1),
    Student("박둘", 2),
    Student("이셋", 3)
]

# 특정한 학생
# print(s[0])
# print(s[1])
# print(s[2])

for i in s:
    print(i)
