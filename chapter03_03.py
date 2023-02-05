# 파이썬 리스트
# 리스트 자료형(순서있고, 중복가능, 수정 가능, 삭제가능)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]

print(c, len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine']

print(d)
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
print(e)
f = [21.42, 'foobar', 3, 4, False, 3.14565]

# 인덱싱
print(">>>>>")
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0]+d[1]+d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print(">>>>")
print("d - ", d[0:3])
print("d - ", d[2:])
print("e - ", e[-1][1:3])

# 리스트 연산
# 리스트 + 리스트는 리스트
# 집합+집합은 집합

print("c+d:", c+d)
print("c*3", c*3)
print("'Test'+c[0]", 'Test'+str(c[0]))

# 값비교
print(c == c[:3]+c[3:])
print(c)
print(c[:3]+c[3:])
print()

# Identity
temp = c
print(temp, c)
print(id(c))

# 리스트 수정 삭제
print(">>>>")
c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c']
print(c)
c[1] = ['a', 'b', 'c']
print(c)
c[1:2] = [['a', 'b', 'c']]
print(c)
c[1:3] = []
print(c)

del c[2]  # 삭제
print(c)

# 리스트 함수
a = [5, 2, 3, 1, 4]
print(a)
# a[5] = 10

print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(3), a[3])
a.insert(2, 7)
print(a)
# del a[9534]
a.remove(10)
print(a)
a.pop()
print(a)
print(a.count(4))

ex = [8, 9]
a.extend(ex)
print(a)

# 삭제 remove pop del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
