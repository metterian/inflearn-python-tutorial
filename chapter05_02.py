from typing import List, Any

# 클로저


# Ex2
b = 20

def func_v2(a):
    print(a)
    print(b)
    print(a + b)



# func_v2(10)


# Ex3
c = 30

def func_v3(a):
    print(a)
    print(c)
    c = 40

# func_v3(10) # 오류 출력

def func_v3(a):
    c = 40
    print(a)
    print(c)


# func_v3(10) # 오류 출력



# 일반적으로 함수가 실행되면 지역변수가 생성되고 함수가 종료되면 지역변수는 사라진다.
# Closer 사용이유 : 함수가 종료되더라도 지역변수가 사라지지 않고 유지되는 기술 -> 동시성 제어(Concurrency) -> 한정적 멀티태스킹
# 클로저는 특정 시점에서의 변수를 저장 (기억)하고 있음
# 클로저는 공유하되 변경되지 않는(Immutable, Read only) 값(숫자, 문자열, 튜플)을 사용할 때 사용 -> 함수형 프로그래밍
# 클로저는 불변자로 구조 및 atom, STM -> 멀티스레드(코루틴) 프로그래밍에 강점
# 클로저를 알아야, 데코레이터 등을 이해 할 수 있다.

# 클로저는 상태를 기억한다. 어떤 상태? 불변 상태!

# 결과 누적 함수
print(sum(range(1, 51)))


# 클래스
class Average():
    def __init__(self) -> None:
        self._series = []

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self._series.append(args[0])
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


average_cls = Average()
print(average_cls(10))
print(average_cls(30))
print(average_cls(50))
"""
inner >>> [10] / 1
10.0
inner >>> [10, 30] / 2
20.0
inner >>> [10, 30, 50] / 3
30.0
"""





