# 半径1の円
# circle1 = circle(radius=1)
# print(circle1.area())  # 3.14
# print(circle1.perimeter())  # 6.28
#
# # 半径3の円
# circle3 = circle(radius=3)


# print(circle3.area())  # 28.27
# print(circle3.perimeter())  # 1 8.85


from math import pi

print(pi)


class circle:
    def __init__(self, radius):
        self.radius = radius

    # def 関数名と引数名を定義するだけ

    def area(self):
        return round(pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(self.radius * 2 * pi, 2)


circle1 = circle(1)
# .area class内の機能を使う
# ()はつける（メソッドを使ってることをわかってもらうため）
print(circle1.area())
print(circle1.perimeter())

circle3 = circle(3)
print(circle3.area())
print(circle3.perimeter())
