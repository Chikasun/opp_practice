# rectangle1 = Rectangle(height=5, width=6)
# rectangle1.area()  # 30.00
# rectangle1.diagonal()  # 7.81
#
# rectangle2 = Rectangle(height=3, width=3)
# rectangle2.area()  # 9.00
# rectangle2.diagonal()  # 4.24

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return f'{self.height * self.width:.2f}'

    def diagonal(self):
        return (f'{(self.height ** 2 + self.width ** 2) ** 0.5:.2f}')


rectangle1 = rectangle(5, 6)
rectangle2 = rectangle(3, 3)

print(rectangle1.area())
print(rectangle1.diagonal())

print(rectangle2.area())
print(rectangle2.diagonal())
