# 병행성(Concurrency): 한 컴퓨터가 여러일을 동시에 수행 (싱글코어, 내가 한일을 여러개 한다, 현재 일을 저장하고 있어야함)
# -> 코루틴
# 병렬성(Parallelism): 여러 컴퓨터가 여러일을 동시에 수행 (멀티코어, 여러개의 일을 동시에 한다)



# Generator Ex1
def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B point'
    print('End')


temp = iter(generator_ex1())

print(temp)
# print(next(temp)) # yield를 만나면 멈추고 다음 yield를 만날때까지 실행하지 않는다. (현재의 포인트를 저장하고 기다리고 있는다) - A 지점에서 멈춰 있음

# print(next(temp)) #  B 지점에서 멈춰 있음






# Generator Ex2
temp = [x * 3 for x in generator_ex1()] # A 포인트 이후에, B 포인트를 출력하는 것이 아니라, A 포인트에 멈춰서 return을 한다.
temp2 = (x * 3 for x in generator_ex1())

print(temp)

for i in temp2:
    print(i)



# Generator Ex3 (중요)
# filterfalse, accumulate, chain, product, groupby 등등

import itertools
gen1 = itertools.count(1, 2.5) # 1부터 2.5씩 증가하는 숫자를 무한히 생성

gen2 = itertools.takewhile(lambda n: n < 1000, gen1) # 1000보다 작은 숫자를 생성

print(gen2)


# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
print(list(gen3))

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
print(list(gen4))

# 연결
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))


# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))


# 개별
gen7 = itertools.product('ABCDE')


# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')
# print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group))
