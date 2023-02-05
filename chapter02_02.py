# 기본선언
n = 100
print(n)

print(type(n))

# 동시선언
x = y = z = 700
print(x, y, z)


# 선언
var = 75

# 재선언
var = "change value"

print(var)
print(type(var))

# Object reference
# 변수 값이 할당 상태일때
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))

m = n
print(m, type(m))

# id (identity) 확인 : 객체의 고유값 확인(참조값)
m = 800
n = 655

print(id(m))
print(id(n))

print(m == n)
print(id(m) == id(n))
n = 800
print(m == n)


# 같은 오브젝트를 참조 한다(id 값이 동일 신기!!!!!)
m = 1200
n = 1200
x = 1200
y = 1200
z = m*2  # 값이 다른것은 아이디값을 다르게 생성
print(id(m), id(n), id(x), id(y), id(z))

# 다양한 변수 선언
# Camel Case = numberOfColleageGraduates -> Method
# Pascal Case = NumberOfColleageGraduates -> Class
# Snake Case = number_of_colleage_graduates
