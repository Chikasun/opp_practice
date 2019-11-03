'''
class (成人の)BMI:
    関連しそうな属性：
    　　　ー身長
         ー体重
         ーBMIという値そのもの
　　 ルール：
         ー１０以上４０以下<--常識的な範囲
         ー表示するときは、少数第2位まで
            -ex: 23.6788 -> 23.67
            -ex: 23.671 -> 23.67
    できること：
    　　　ー？？？
'''


# クラス名はUpperCamellCaseが普通
class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)


# BMIクラスのインスタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)

print(hibiki_bmi.height, hibiki_bmi.weight)
print(hibiki_bmi.calculate_bmi())


noriya_bmi = BMI(height=1.78, weight=75.0)

print(noriya_bmi.height, noriya_bmi.weight)
print(noriya_bmi.calculate_bmi())
