# 집합
# set 특징
# 순서가 없다
# 중복 허용 안함
# 추가 삭제 가능

# 선언
a = set()
# 빈집합을 선언
print(a, type(a))
b = set([1, 2, 3, 4, 5])
print(b)
c = set([1, 4, 5, 6, 7])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'fooff', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.1466}

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 중복 허용안함
aa = set([1, 2, 3, 4, 4, 4])
print(aa)
# 튜플 변환 (set->tuple)

t = tuple(b)
print(t, type(t))
print(t[0])

# 리스트 변환 (set->list)
l = list(c)
l2 = list(e)
print(l)
print(l2)


# 집합 자료형
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))

print('s1-s2', s1-s2)
print('s1-s2', s1.difference(s2))
print()

# 중복원소 확인
print('s1 & s2', s1.isdisjoint(s2))  # 있으면 false 없으면 true

# 부분집합
print(s1.issubset(s2))
print(s2.issubset(s1))  # s2가 s1의 부분집합이다
print(s1.issuperset(s2))


# 추가 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print(s1)
s1.remove(2)
print(s1)
# s1.remove(7) error 발생
s1.discard(3)
print(s1)
s1.discard(7)  # error 발생 안함

s1.clear()
