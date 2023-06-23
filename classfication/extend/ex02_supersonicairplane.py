# SuperSonicAirplane 클래스 생성

from classfication.ex02_airplane import Airplane


# Airplane를 상속받음
class SuperSonicAirplane(Airplane):
    # 1번 - NORMAL, 2번 - SUPERSONIC
    NORMAL = 1
    SUPERSONIC = 2

    # 모드 - 멤버 변수
    def __init__(self):
        self.fly_mode = SuperSonicAirplane.NORMAL

    def fly(self):
        if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
            print("초음속으로 비행합니다.")
        else:
            super().fly()


sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.SUPERSONIC # 모드 변경
sa.fly()
sa.land()
