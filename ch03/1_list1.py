# 리스트 생성
cart = []  # 빈 리스트
# 리스트 요소는 append() 추가
cart.append('계란')
cart.append('사과')
cart.append('생수')
cart.append('콩나물')

# 특정한 위치에 요소 추가
cart.insert(2,"양파")

# 리스트 형태로 조회
print(cart)

# 리스트의 갯수
print(len(cart))

# 리스트 수정
cart[2] = '커피'

# 리스트 삭제
# del cart[0] 명령으로 삭제
# cart.remove('계란') 배열의 값으로 삭제
# pop : 인덱스의 요소로 삭제 값을 안넣으면 맨뒤에서 삭제
# cart.pop(1)
# cart.pop()
# cart2 = ["계란",'사과','생수']

# 전체조회
for i in cart:
    print(i)

# 특정한 값을 조회 
print(cart[-1]) # -숫자 맨뒤에서부터 출력

print(cart)
# print(cart2)

'''
#end로 요소 컨트롤 디폴트값은 end='\n'으로 출력결과가 한줄 씩 띄워진거 
for i in range(1, 11, 1):
    print(i, end='')
print()
# 값 : 123456789

#food 배열의 인텍스 0번을 배열만큼 출력함
food = ['짜장', '짬뽕','간짜장']
for i in food:
    # print(i)
    print(i[0])
# 값 : 짜짬간
seasons = ['spring','summer','autumn','winter']
seasons = [0:2]
>>>['spring','summer']
'''
