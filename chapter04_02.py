# for

# for in <collection>
#   <loop body>

for v1 in range(10):
    print("v1 is :", v1)

for v2 in range(1, 11):
    print("v2 is :", v2)

for v3 in range(1, 11, 2):
    print("v3 is :", v3)

# 1~1000합
sum1 = 0

for v1 in range(1, 1001):
    sum1 += v1

print(sum1)

print("1~1000 sum :", sum(range(1, 1001)))

print(type(range))

print("1~1000 4의배수의 합 ", sum(range(4, 1001, 4)))


# iterables 자료형
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["kim", "park", "cho", "lee", "choi", "youu"]

for n in names:
    print("you are : ", n)

# 예제2
lotto_numbers = [11, 10, 21, 28, 36, 37]
for n in lotto_numbers:
    print("current numbers : ", n)

# 예제3
word = "beautiful"

for s in word:
    print("word : ", s)


my_info = {
    "name": "Lee",
    "Age": 33,
    "city": "seoul"
}

for key in my_info:
    print("key : ", my_info[key])

for v in my_info.values():
    print("value : ", v)

# 예제5

name = "FineAppLE"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break

numbers = [14, 3, 70, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for n in numbers:
    if n == 34:
        print("Found 34")
        break
    else:
        print("Not Found")

# continue
lt = ["1", "2", 3, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is not bool:
        continue
    print("current Type:", v, type(v))
    print("multiply by2", v*3)

# for - else
numbers = [14, 3, 70, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found :", 24)
        break
else:
    print("not found : ", 24)


# 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()


# 변환 예제
name2 = "Aceman"

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))
