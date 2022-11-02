# 동시성 (Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
# 병렬성 (Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행

# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> 파일 I/O Network I/O 관련 작업 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우, 압도적으로 성능 향상


# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉽게 개선
# 2. 실행중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념


# 2가지 패턴 실습
# concurrent.futures wait
# concurrent.futures wait, as completed
# 작업을 수행할 때, 어떤 작업은 오류가 나고 시간이 오래 걸릴 수 있다. 이러한 작업을 처리 해주기 위해 wait 등이 필요


# GIL : 두개 이상의 스레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우 -> 문제발생
# GIL 실행, 리소스 전체에 락이 걸림 -> Context Switch(문맥 교환): 시간이 많이 소요 -> 즉, 하나의 자원을 여러명이 동시에 사용하고자 할 떄 시간이 많이 소요되는 문제가 존재한다.
# 이를 해결하기 위해서, 멀티프로세싱 혹은 Cpython을 사용한다.



import os
import time
from concurrent.futures import wait, as_completed, ThreadPoolExecutor


WORK_LIST = [100000, 1000000, 10000000, 100000000]


# 동시성 합계 계산 메인함수
# 누적 합계 함수(제너레이터)


def sum_generator(n):
    return sum(n for n in range(1, n+1))


# wait


def main():
    # worker count
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()
    # Futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExcutor
    with ThreadPoolExecutor() as executor:
        # map은 작업 순서를 유지, 즉시 실행
        for work in WORK_LIST:
            # future만 반환할 뿐(미래에 할 일 을 반환)
            future = executor.submit(sum_generator, work)
            futures_list.append(future) # future 리스트에 일들이 담기게 됨

            # 스케쥴링 확인
            print(f"Scheduled for {work}: {future}")
            print()

        # result = wait(futures_list, timeout=3) # 시간 제한을 1초로 둠. 인스턴스가 완료되는데 까지 기다림

        # # 성공
        # print(f"Completed Tasks : {result.done}")
        # # 실패
        # print(f"Pending ones after waiting for 7 seconds : {result.not_done}")

        # # 결과값 출력
        # print([future.result() for future in result.done])

        # as_competed 결과 출력
        for future in as_completed(futures_list):
            result = future.result() # 일이 가장 먼저 끝나는 놈
            done = future.done()
            cancelled = future.cancelled()
            # future 결과 확인
            print(f"Future Result : {result}, Done: {done}")
            print(f"Future Cancelled: {cancelled}")


    # 종료 시간
    end_tm = time.time() - start_tm

    print(f'\n Time: {end_tm}')

# 실행
if __name__ == "__main__":
    main()
