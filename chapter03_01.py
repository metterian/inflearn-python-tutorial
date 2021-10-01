# print(dir(int))


n = 10


print(n+ 100)
print(n.__add__(100))



# 클래스 예제1
class Fruit:
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price

    def __str__(self) -> str:
        return f'Fruit Class Info {self._name}, {self._price}'

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price


# 인스턴스 사용
s1 = Fruit("Orange", 7500)
s2 = Fruit('Banana', 3000)

print(s1._price + s2._price)
