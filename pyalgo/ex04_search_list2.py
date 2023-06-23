# 학생번호에 해당하는 이름을 순차탐색으로 찾아 돌려주는 함수를 작성하세요
# 단 학생번호가 없으면 '?' 를 반환함
def search_list3(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return name[i]
    return '?'

v = [60, 5, 33, 12, 97]
name = ['이순신', '강감찬', '서희', '안중근', '유관순']

print(search_list3(v, 60))
print(search_list3(v, 1))


