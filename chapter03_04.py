# 튜플
# 리스트와 비교가 중요 리스트를 쓸지 튜플쓸지

# 튜플 자료형(순서있고, 중복 있고, 수정 삭제 안됨)
# 한번 선언하면 끝까지 씀

# 선언
a = ()
b = (1)

print(type(b))

c1 = (1,)
print(type(c1))
c = (11, 12, 13, 14)
d = (100, 1000, "Ace", "Base", "Captine")
e = (100, 1000, ("Ace", "Base", "captine"))

# 인덱싱
print(">>>")
print(d[1])
print(d[0]+d[1]+d[1])
print(d[-1])
print(e[-1])
print(e[-1][1])
print(list(e[-1][1]))

# 수정 안됨
# d[0]=10

# 슬라이싱
print(">>>>")
print(d[0:3])
print(d[2:])
print(e[2][1:3])

# 튜플 연산
print(c+d)
print(c*3)

# 튜플함수
a = (5, 2, 3, 1, 4)
print(a)
print(a.index(3))
print(a.count(2))

# 팩킹 언팩킹(packing, unpacking)

# 패킹
t = ("foo", "bar", "baz", "qux")
print(t)
print(t[0])
print(t[-1])

# 언패킹1
(x1, x2, x3,  x4) = t
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))

# 언패킹 2
t2 = 1, 2, 3  # 괄호가 없어도 튜플
t3 = 4,  # 원소가 하나인 튜플임

x1, x2, x3 = t2
x4, x5, x6 = 1, 2, 3
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
