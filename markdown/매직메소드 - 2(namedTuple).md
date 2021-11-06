

## 들어가며

Python의 네임드 튜플 (Named Tuple)은 ML/DL등에서 학습을 위한 데이터셋 전처리 시에 데이터 타입에 대한 작업을 진행하거나, 웹 개발에서 DB에서 자료를 가져올 때 많이 사용하는 개념 중에 하나 입니다. 튜플은 한번 입력하면 수정이 안된다는 특징을 기억하고 본 포스팅을 읽어 주시면 감사하겠습니다.

지난 포스팅에서 `객체` 란 파이썬의 데이터를 추상화 한것이라고 설명 했었습니다. 이를 활용하여 모든 객체는 `id` 통해 확인 할 수 있고 value는 `type` 으로 객체 값을 확인 할 수 있습니다. 



### 일반적인 튜플

다음과 같이 두 점의 좌표를 튜플 형태로 저장 할 수 있습니다. 다음 코드의 문제점은 데이터 관점에서 봤을 때, `1.0` 이 뜻하는게 무엇인지, 인자에 대한 정보를 확인 할 수 없습니다. 

```python
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
```

### 두 점 사이의 거리 구하기

다음과 같이 두 점 사이의 거리를 구할 수 있습니다. 

```python
from math import sqrt
l_leng1 = (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2
l_leng1 = sqrt(l_leng1)
# 3.8078865529319543
```



### 네임드 튜플 사용해보기

> Named tuples are basically easy-to-create, lightweight object types. Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax. 
>
> 출처: stackoverflow

네임드 튜플은 튜플의 문법을 따는는 객체 라고 합니다. 이를 사용하기 위해서는 collection의 모듈을 사용해야 합니다. 우리는 네임드 튜플을 좌표로 생각 할 것이기때문에 `namedtuple('Point')` 과 같이 'point'를 명시적으로 작성해 줍니다. 

```python
from collections import namedtuple
# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)
# Point(x=1.0, y=5.0)
# Point(x=2.5, y=1.5)

print(pt3.x, pt3[0])
# 1.0
```

위 코드와 같이 `pt3` 에 대한 x좌표 접근은 `pt3.x` 로 가능합니다. 즉, 유연하게 직관적으로 데이터 관점에서 해당 객체에 대한 값을 확인 할 수 있는 것이지요.

이전 포스팅에서 인덱스로 값을 접근하는 것은 위험하다고 했습니다. 때문에 두 점 사이의 거리를 구하는 계산도 다음과 같이 수정 할 수 있습니다. 다음과 같이 코드가 보다 직관적으로 이해가 쉽게 바뀌였습니다.

```python
l_leng2 = (pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2
l_leng2 = sqrt(l_leng2)
```



<br/>

### 네임드 튜플 선언 방법

다음과 같이 여러 가지 방법으로 네임드 튜플 선언이 가능합니다. 단, 튜플은 key의 유일성을 보장해야하기 때문에 중복을 허용하지 않습니다. 이때는 `rename` 인자를 `True` 로 설정 해야 합니다. 

```python
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')


Point4 = namedtuple('Point', 'x y x class') # error: be unique!
Point4 = namedtuple('Point', 'x y x class', rename=True)
# <class '__main__.Point'>
```



이렇게 네임프 튜블 객체들을 생성하고 다음과 같이 인스턴스를 입력해 줍니다. `p4` 의 값을 살펴 보면 `Point(x=10, y=20, _2=30, _3=40)` 와 같이 출력됩니다. 즉, 중복되는 Key값은 자동으로 Key이름을 변경해서 변수를 생성 해 주었습니다. 

```python
# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

print(p4)
# Point(x=10, y=20, _2=30, _3=40)
```

<br>

### `Dict` to unpacking

이번에는 `dict` 타입의 객체를 받아서 네임드 튜플로 만들어 보겠습니다. `dict` 과 튜플은 어면히 다른 데이터 타입입니다. 때문에 **unpacking** 기능을 사용해서 네임드 튜플에 입력해 줍니다.

```python
temp_dict = {'x': 75, 'y': 55}

p5 = Point3(**temp_dict)
# Point(x=75, y=55)
```



<br>

## 네임드 튜플 메소드

#### `_make` : list to namedtuple

리트스를 네임드 튜플의 자료형으로 변환 해주는 메소드는 바로 `_make` 입니다. 

```python
temp = [52, 38]

p4 = Point._make(temp)
```

### `_fields` : 필드 네임 확인

```python
print(p1._fields)
# ('x', 'y')
```

### `_asdict()`: OrderedDict 반환

정렬된 딕셔너리로 반환 합니다. 

```python
print(p1._asdict())
```

