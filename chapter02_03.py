class Car():
    """
    Car class
    Author : Lee
    Date : 2021
    Description : Class, Static, Instance Method
    """

    # 클래스 변수
    price_per_raise = 1.0

    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details

    def __str__(self) -> str:
        return f'str : {self._company} - {self._details}'

    def __repr__(self) -> str:
        return f'repr : {self._company} - {self._details}'


    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    def get_price(self):
        return f"Before Car price -> company : {self._company} price : { self._details.get('price') * Car.price_per_raise}"

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1.0:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')


    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return f'OK! This is {inst._details}'
        return 'Sorry. This is car not BMW'


# self의 의미
car1 = Car("Ferrari", {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car("BMW", {'color': 'Black', 'horsepower':200, 'price': 3000})



print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car2))
