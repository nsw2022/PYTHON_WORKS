# time 모듈
import time

# 1부터 10까지 출력 (1초 간격으로 출력)
start = time.time()
for i in range(1, 11):
    time.sleep(1.0)
    print(i)
end = time.time()
# print(start-end)
et = start-end
print(f'수행시간 : {0:.2f}'.format(et))
