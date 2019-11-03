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
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 40):
            raise ValueError('BMIが正常値の範囲を超えています')

    def __str__(self):
        return f'{self.value:.2f}'


# BMIクラスのインスタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)
print(hibiki_bmi)


noriya_bmi = BMI(height=1.78, weight=75.0)
print(noriya_bmi)
