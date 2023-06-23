# ScaleConverter를 상속받는 클래스
# 화씨온도(F) = 섭씨 온도(C) x 1.8 + 32
# import 상위폴더명.모듈이름
import classfication.ex06_scale_converter
# from 상위폴더명.모듈이름 import 클래스
from classfication.ex06_scale_converter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    # 메서드 재정의
    def convert(self, value):
        # return self.factor * value + self.offset
        return super().convert(value) + self.offset

if __name__ == '__main__':
    conv = Converter('C', 'F', 1.8, 32)
    print("Converting 21C")
    print(f'{conv.convert(21):.2f}{conv.units_to}')
    # con = ScaleConverter("KB", "B", 1024)
    # print("Converting 1 KB")
    # print(str(con.convert(1)) + con.units_to)

