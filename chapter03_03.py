# 두점 사이의 거리 구하기

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
l_leng1 = (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2
l_leng1 = sqrt(l_leng1)

print(l_leng1)


from collections import namedtuple
# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)

print(pt3.x, pt3[0])
# 1.0

l_leng2 = (pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2
l_leng2 = sqrt(l_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')


# Point4 = namedtuple('Point', 'x y x class') # error: be unique!
Point4 = namedtuple('Point', 'x y x class', rename=True)
print(Point4)


# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
temp_dict = {'x': 75, 'y': 55}
p5 = Point3(**temp_dict)
print(p5)


# 네임드 튜플 메소드

# list to namedtuple
temp = [52, 38]
p4 = Point._make(temp)

# field name check
print(p1._fields)

### `_asdict()`: OrderedDict 반환

# 정렬된 딕셔너리로 반환 합니다.

print(p1._asdict())



