# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터


# 파이썬 반복 가능한 타입 (Iterable)
# collections, text file, List, Dict, Set, Tuple, unpacking, *args... : iterable
# 제너레이터는 이터레이터를 생성해주는 함수

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(dir(t)) # __iter__ 가 있음
bool(t.__iter__()) # True

# 반복 가능한 이유? -> iter(x) 함수 호출

# 아래 for loop이 동작하는 이유는 next()함수가 호출 되면서 StopIteration이 발생할 때까지 동작하기 때문
# 즉, iteration 하고 있다.
# 반복형을 반환하는 함수 : iter()
for c in t:
    print('>', c)

# while
w = iter(t)
print(next(w))
print(next(w)) # 이렇게 호출 되는 이유는 next가 위치를 기억하면서 다음 원소를 호출하기 때문

# 즉 for loop는 아래와 같이 동작한다.
while True:
    try:
        print(next(w))
    except StopIteration:
        break


# 반복형 확인
print(hasattr(t, '__iter__')) # True

# collection에 있는 것는 모두 반복형이다.
from collections import abc
print(isinstance(t, abc.Iterable)) # True



# next 패턴
class WordSplitter:
    def __init__(self, text) -> None:
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')

        self._idx += 1

        return word

    def __repr__(self) -> str:
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi)) # 클래스인데 iterable 하게 사용이 가능해 진다.

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 시 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text) -> None:
        self._text = text.split(' ')
    def __init__(self) -> None:
        for word in self._text:
            yield word # 제너레이터는 yield를 사용한다. return과 비슷하다.


wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
