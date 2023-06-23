# 백신 접종
while True:
    try:
        birth_year = input("출생년도 입력: ")
        age= 2023-int(birth_year) + 1
        if age >= 20 and age <= 65:
            print("접종 대상")
            if birth_year[-1] == '1' or birth_year[-1] == '6':
                print("월요일 접종")
                break
            elif birth_year[-1] == '2' or birth_year[-1] =='7':
                print("화요일 접종")
                break
            elif birth_year[-1] == '3' or birth_year[-1] =='8':
                print("수요일 접종")
                break
            elif birth_year[-1] == '4' or birth_year[-1] =='9':
                print("목요일 접종")
                break
            elif birth_year[-1] == '5' or birth_year[-1] =='0':
                print("금요일 접종")
                break
        else:
            print("백신 대상자가 아니에요")
    except:
        print("숫자만입력해주세요\n")
   

