class Car():
    # 클래스 변수
    car_count = 0

    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self) -> str:
        return f'str : {self._company} - {self._details}'

    def __repr__(self) -> str:
        return f'repr : {self._company} - {self._details}'

    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    def __del__(self):
        Car.car_count -= 1

# self의 의미
car1 = Car("Ferrari", {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car("BMW", {'color': 'Black', 'horsepower':200, 'price': 3000})
car3 = Car("Audi", {'color': 'Silver', 'horsepower': 300, 'price': 8000})


# print(Car.detail_info(car1))
# print(car1.detail_info())

print(dir(car1))
