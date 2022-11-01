# 코루틴: 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# yield: 메인 <-> 서브 루틴

# 쓰레드: OS에서 관리


# 서브루틴: 메인루틴에서 호출 -> 서브루틴에서 스택을 사용
# 코루틴: 루틴 실행중 중지 -> 동시성 프로그래밍에 적합
# 코루틴: 스레드에 비해 오버헤드 감소
# 스레드: 싱글스레드 -> 멀티스레드 -> 복잡, 공유되는 자원 -> 자원소모,  -> 컨텍스트 스위칭 비용 발생



# 코루틴 예제1



def coroutine1():
    print('>>> coroutine started.')
    i = yield # 제너레이터에서 사용하는 yield
    print('>>> coroutine received: {}'.format(i))

# yield가 들어가면 제너레이터가 됨
# 단순이 def를 선언한다고 해서 함수가 되는 것이 아니다. 함수 안에 yield가 들어 가면 제너레이터 함수가 됨

# 제너레이터 선언
# 메인 루틴 = 서브 루틴
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
# next(cr1) # next를 호출하면 제너레이터가 실행됨

# # 갑을 전송
# # send를 서브 루틴에서 100을 받음, 기본 전달 값 None
# cr1.send(100)

# # 잘못된 사용
# cr2 = coroutine1()
# next(cr2)
# cr2.send(200) # next로 코루틴을 실행해야, 이후에 서브 루틴으로 값을 전달 할 수 있음



# 코루틴 예제2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태 (중요, 이 상테에서 send로 값을 주고 받을 수 있음)
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print(f'>>> coroutine started: {x}')
    # 오른쪽에 있는 값을 왼쪽으로 전달
    y = yield x
    print(f'>>> coroutine received: {y}')
    z = yield x + y
    print(f'>>> coroutine received: {z}')



cr3 = coroutine2(10)

from inspect import getgeneratorstate # 제너레이터의 상태를 확인하는 함수

# print(getgeneratorstate(cr3))

print(next(cr3))


# print(getgeneratorstate(cr3))
# cr3.send(100) # 전달 받은 값을 출력
print(cr3.send(100)) # 전달 받아서 값을 계산한 후 출력

# print(getgeneratorstate(cr3))
# cr3.send(200)




