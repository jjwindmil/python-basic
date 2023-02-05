# Chapter03-2
# 파이썬 문자형

# 문자형 중요
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), type(str2), len(str3), type(str4))

# 빈문자열
str5 = ''
str6 = str()

print(str5, type(str5), len(str5))

# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")

print('I\'m Boy')
print('a \t b')
print('a \n b')
print('a \"\" b')

# 파이썬은 indent에 민감

# 이스케이프와 반대 대는 raw String
# 소문자 r이 붙어있으면 로우스트링
raw_s1 = r'D:\python\test'
print(raw_s1)


# 멀티라인 입력
# 멀티라인 \사용
multi_str = '''
Strinmg
multi line
Test
'''
print(multi_str)
multi_str2 = \
    '''
Strinmg
multi line
Test
'''


# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How Are you"
str_o4 = "Seoul Daejeon Busan jinhju"

print(str_o1*3)
print(str_o1+str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열  형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum,startswith, count,endswith, isalpha....)
print("Capitalize: ", str_o1.capitalize())
print("endswith ? : ", str_o2.endswith("s"))
print("replace", str_o1.replace("Nice", "Good"))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(" "))

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))
for i in im_str:
    print(i)


# 슬라이싱 연습

str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3])  # 0 1 2

print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)])

print(str_s1[1:4:2])  # 3번째 인수는 몇개단위로 점프해서 가져와라
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[:: 2])
print(str_s1[:: -1])

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a))  # 문자열을 아스키
print(chr(122))  # 아스키를 문자열
