# funciton


# 함수정의방법
# def function_name(paramter):
#   code

def first_func(w):
    print("hello", w)


first_func("hiiiii")

print(first_func)

# 예제2


def return_func(w1):
    return "Hello "+str(w1)


print(return_func("park b m"))

# 함수형 프로그래밍

# 예제3(다중반환)


def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return y1, y2, y3


x, y, z = func_mul(10)

print(x, y, z)

# 튜플리턴


def func_mul1(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return (y1, y2, y3)


q = func_mul1(20)

print(q)

print(type(q), q, list(q))

# 리스트 리턴


def func_mul2(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return [y1, y2, y3]


p = func_mul2(30)

print(type(p), p, set(p))


def func_mul3(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return {"v1": y1, "v2": y2, "v3": y3}


d = func_mul3(40)
print(type(d), d, d.get('v2'), d.items(), d.keys())


# 중요
# packing unpacking

# paramter * 한개, ** 두개
# *args, **kwargs

# *args(언팩킹)

def args_func(*args):
    # 매개변수명 자유
    for i, v in enumerate(args):
        print('Result L: {}'.format(i), v)
    print('-----')


args_func('Lee')
args_func('lee', 'kim')
args_func('lee', 'kim', 'park')
# 튜플 형태로 보냄
# 가변인자를 가능케함

# **kwargs(언패킹)


def kwargs_fuinc(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("-----")


kwargs_fuinc(name1='lee')
kwargs_fuinc(name1='lee', name2='park', name3='choi')


# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)


# 중첩함수
def neted_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num+100)


neted_func(100)


# 람다식 예제
# 메모리절약, 가독성, 코드 간결
# 함수는 객체 생성-> 리소스(메모리) 할당
# 람다는 즉시 실행함수(힙 초기화)-> 메모리 초기화

# 남발시에는 가독성 오히려 감소


# def mul_func(x, y):
#   return x*y


# lambda x, y: x*y


def mul_func4(x, y):
    return x*y


print(mul_func4(10, 50))


lambda_mul_func = lambda x, y:  x*y


print(lambda_mul_func(20, 30))


# 람다 함수 -> 할당
def func_final(x, y, func):
    print('>>>>', x*y*func(100, 100))
