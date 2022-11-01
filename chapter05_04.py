# 데코레이터
# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 조합해서 사용 용이


# 단점
# 1. 가독성 감소? (상황에 따라 다름)
# 2. 디버깅 불편

# 실습

import time
# 클로저 형태로 만든 데코레이터 테스스
def per_check(func):
    def per_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return per_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
none_deco = per_check(time_func)
none_deco2 = per_check(sum_func)

print(none_deco, none_deco.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
print(none_deco(1.5))
print('-' * 40, 'Called None Decorator -> sum_func')
print()
print(none_deco2(100, 200, 300, 400, 500))

# 데코레이터 사용
@per_check
def time_func(seconds):
    time.sleep(seconds)
@per_check
def sum_func(*numbers):
    return sum(numbers)




print("-" * 40, "Called Decorator -> time_func")
print()
time_func(1.5)
print("-" * 40, "Called Decorator -> sum_func")
print()
sum_func(100, 200, 300, 400, 500)
# 불필요하게 클로저를 사용하지 않고, 함수를 그대로 호출해서 사용이 가능하다.
