
from dataclasses import dataclass

@dataclass
class Vector(object):
    _x : int = 0
    _y : int = 0

    def __repr__(self) -> str:
        "Return the Vector information"
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other):
        """Return the vector addition of inputs"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        """Return the vector multiply of inputs"""
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):
        """Check inputs are in 2-D coordinate"""
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직 메소드 출력
print(Vector.__add__.__doc__)


print(v1, v2, v3)

print(v1 + v2)
print(v1 * v2)


