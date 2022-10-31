# 클로저 기초
# 외부에서 호출된 변수의 값을 변경하는 클로저(Closure)의 사용

from typing import List, Any
# 클래스
class Average():
    def __init__(self) -> None:
        self._series = []

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._series.append(args[0])
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

"""
inner >>> [10] / 1
10.0
inner >>> [10, 30] / 2
20.0
inner >>> [10, 30, 50] / 3
30.0
"""



# 클로저(Closure) 사용
def closure_ex1():
    # Free variable (자유 변수)
    # 클로저 영역

    series = [] # 자유 변수: 내가 사용하려는 함수 밖에 있는 변수 (자유롭게 사용할 수 있음)
    a = []
    b = 10
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager


avg_closure1 = closure_ex1()
avg_closure1(10)
avg_closure1(20)


# 자유 변수 출력
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__code__)



# 잘못된 클로저 사용
def closure_ex2():
    # Free variable (자유 변수)
    # 클로저 영역

    cnt = 0 # 리스트를 사용하지 않고 mutable한 변수를 사용하면 안됨
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

closure__cls2 = closure_ex2()
print(closure__cls2.__code__.co_freevars)
# print(closure__cls2(10))



def closure_ex2():


    cnt = 0 # 리스트를 사용하지 않고 mutable한 변수를 사용하면 안됨
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

closure__cls2 = closure_ex2()
print(closure__cls2.__code__.co_freevars)
print(closure__cls2(10))


# outer(), inner() 함수 입장에서 전역(global) 범위
def outer():
    # outer() 함수 입장에서 지역(local) 범위
    # inner() 함수 입장에서 비지역(nonlocal) 범위
    def inner():
        # inner 함수 입장에서 지역(local) 범위
        pass


global_var = "전역 변수"

def outer():
    nonlocal_var = "비전역 변수"
    print(global_var) # 가능
    print(nonlocal_var) # 가능

    def inner():
        local_var = "지역 변수"
        print(global_var) # 가능
        print(nonlocal_var) # 가능
        print(local_var) # 가능
    inner()
outer()
