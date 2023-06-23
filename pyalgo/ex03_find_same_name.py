# 동명 이인 찾기

def find_swame_name(a):
    same_name = set()#중복값 기억할 빈집합
    n = len(a)
    # same_name = []
    for i in range(0, n-1):
        # print(f'나는 i{i}')
        for j in range(i+1, n):
            # print(f'나는 i{i} j{j}')
            if a[i] == a[j]:
                # 중복값 추가
                same_name.add(a[i])
    return same_name
#same_name=[] same_name.append(i)도 가능함
name = ['흥부', '콩쥐', '놀부', '콩쥐']
print(find_swame_name(name))

'''
i=0 j=1 name[0]==name[1] False
    j=2 name[0]==name[2] False
    j=3 name[0]==name[3] False
    
i=1 j=2 name[1]==name[2] False
    j=3 name[1]==name[3] True {'콩쥐'} - 중복값 찾음
    
i=2 j=3 name[2]==name[3] False   
'''