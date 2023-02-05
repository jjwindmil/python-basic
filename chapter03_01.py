# Chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int:정수
float:실수
complex:복소수
bool:불린
str:문자열(시퀀스)
list: 리스트(시퀀스)
tuple:튜플(시퀀스)
set:집합
dict:사전
"""

import math
str1 = "python"
bool = True
str2 = "Anaconda"
float = 10.0
int = 7
list = [str1, str2]
print(list)
dict = {
    "name": "Machine Learning",
    "version": 2.0

}
tuple = (7, 8, 9)
tuple2 = 7, 8, 9
set = {7, 8, 9}
print(dict)

print(type(str1))
print(type(str2))
print(type(bool))
print(type(float))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(tuple2))
print(type(set))


"""
+
-
*
/
//:몫
%: 나머지
abs(x) :절대값
pow(x,y) x**y-> 2**3
"""


# 정수선언
i = 77
i2 = -14
big_int = 77787777777777777799999999999


# 정수출력
print(i)
print(i2)
print(big_int)


# 실수선언
f = 0.9999
f2 = 3.145145151
f3 = -3.9
f4 = 3/9


# 연산실습
i1 = 39
i2 = 939
big_int1 = 1234918239012893081290
big_int2 = 1298312983091839012830912830

f1 = 1.234
f2 = 3.923


# 파이썬은 큰 숫자도 자동으로 담김
# 형변환 실습
a = 3
b = .8
c = 6
d = 12.8


# 수치연산함수
print(abs(-7))
x, y = divmod(100, 8)

print(x, y)
print(pow(5, 3), 5**3)

# 외부모듈
print(math.pi)
print(math.ceil(5.1))  # x이상의 수 중에서 가장 작은 정수
