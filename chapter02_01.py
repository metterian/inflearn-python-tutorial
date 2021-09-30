# Chapter02-01
# 객체 지향 프로그래밍 -

# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'white'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color': 'black'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량3
car_company_3 = 'BMW'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]


# 리스트 구조
car_company_list = ['Ferrari', 'BMW', "Audi"]
car_detail_list = [
    {'color': 'white', 'horsepower': 400, 'price': 800},
    {'color': 'black','horsepower': 400, 'price': 800},
    {'color': 'Silver','horsepower': 300, 'price': 6000}
]




# 클래스 구조

class Car():
    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details


    def __str__(self) -> str:
        return f'str : {self._company} - {self._details}'




car1 = Car("Ferrari", {'color': 'white', 'horsepower': 400, 'price': 800})

print(dir(car1))
