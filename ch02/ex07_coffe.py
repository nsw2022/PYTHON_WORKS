coffe_c = 5

while True:
    try:
        chash = int(input('돈을 넣어주세요\n'))
        if chash==400:
            print('커피가 나옵니다')
            coffe_c-=1
            print(f'남은 커피의 양은 {coffe_c}개 입니다.')
        elif chash>400:
            print(f'커피가 나오고 거스름돈{chash-400}을 돌려받습니다')
            coffe_c-=1
            print(f'남은 커피의 양은 {coffe_c}개 입니다.')
        else:
            print('커피가나오지않습니다')
        if coffe_c==0:
            print("커피가 모두 소진되었습니다. 판매를 중지합니다")
            break
    except ValueError:
        #print('문자시군요 숫자를 입력하세요')
        pass
