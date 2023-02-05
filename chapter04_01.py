# 파이썬 제어문
# if

# 기본 형식
print(type(True))  # 0이 아닌 수, "abc", [1,2,3], (1,2,3)
print(type(False))  # 0 "", [], {},() ...

# 예
if True:
    print('Good')

if 'a':
    print("A")

if False:
    print("Bad")
else:
    print("Good")


# 관계연산자
# >,>=, <, <=, ==, !=

x = 15
y = 10

if x == y:
    print("xy equals")

city = ""
if city:
    print("Your city in ", city)
else:
    print("please enter in your city")

city2 = "Seoul"
if city2:
    print("your City in ", city2)
else:
    print("please enter your city")

# 논리연산자
# and or not

a = 75
b = 40
c = 10

print("and : ", a > b and b > c)
print("or :", a > b or b > c)
print("not :", not a > b)
print(not True)
print(not False)


# 산술 관계 논리 우선순위
# 산술> 관계> 논리
print("e1 :", 3+12 > 7+3)
print("e2 : ", 5+10*3 > 7+3*20)
print("e3 : ", 5+10 > 3 and 7+3 == 10)
print("e4 : ", 5+10 > 0 and not 7+3 == 10)

score1 = 90
score2 = "A"

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == "A":
    print("Pass")
else:
    print("Fail")


id1 = "vip"
id2 = "admin"
id3 = "platinum"

if id1 == "vip" or id2 == "admin":
    print("관리자 입장")

if id1 == "admin" and id2 == "platinum":
    print("최상위 관리자")


num = 90
if num >= 90:
    print("Grade A")
elif num >= 80:
    print("Grade B")
elif num >= 70:
    print("Grade C")
else:
    print("과락")

# 중첩조건문
grade = "A"
total = 95

if grade == "A":
    if total >= 90:
        print("장학금 100")
    elif total >= 80:
        print("장학금 80")
    else:
        print("장학금 50")
else:
    print("장학금 없음")

# in, not in
q = [10, 20, 30]  # 리스트
w = {70, 80, 90, 100}  # 집합
e = {"name": "Lee", "city": "seoul", "grage": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())
