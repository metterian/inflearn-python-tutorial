chars = '+_)(*&^%$#@!)'
# chars[1] = '3'

code_list1 = []
for s in chars:
    # Unicode List
    code_list1.append(ord(s))


coding_list2 = [ord(s) for s in chars]
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)


code_list4 = list(filter(lambda x: x>40, map(ord, chars)))
print(code_list4)


# 제너레이터
import array

tuple_g = [ord(s) for s in chars]
print(tuple_g)

tuple_g = (ord(s) for s in chars) # 제너레이터
print(tuple_g)

print(next(tuple_g))


array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
