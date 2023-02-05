#Exception
# 예외종류
#SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError
#문법적으로는 예외가 없지만, 코드 실행 프로세스에서 발생하는 예외 중요

#예외는 반드시처리
#로그는 반드시 남긴다.
#예외는 던져진다.
#예외 무시

#신택스에러
#print('error)
#print('error'))
#if True:
#   pass

#Name error :참조없음
#a=10
#b=14
#print(c)

#ZeroDevision Error
#print(100/0)

#index ERror
#x=[50,70,90]
#print(x[56])

#KeyError
dic={
    'name':"Lee",
    'age':41,
    'City':'Bussan'

}

#print(dic['hobby']) #에러 발생
#print(dic.get('hobby')) getmethod는 unknown을 반환

#예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외처리 권장(EAFP)

#Attirbute Erorr :모듈 클래스에 이쓴ㄴ 잘못된 속성 사용예외

#import time
#print(time.time2()) 없는 속성 실행

#value Error
#x=[10,50,90]
#x.remove(50)
#print(x)
#x.remove(200)

#file not found Error
#f=open('test.txt')

#Type Error: 자료형에 맞지 않는 연산을 수행을 경우
#x=[1,2]
#y=(1,2)
#z='test'

#print(x+y)
#print(x+z)
#print(y+z)
#print(x+list(y)) 형변환해서 처리해야함


#예외처리 기본
#try : 에러가 발생할 가능성이 있는 코드 실행
#except 에러명 : 여러개 가능
#else: try 블록의 에러가 없을 경우 실행
#finally: 항상 실행

name=['Kim','Lee','Park']
#예제1
# try:
#     z='Kim'
#     x=name.index(z)
#     print('{} Found it! {} in name'.format(z,x+1))
# except ValueError:
#     print('Not Found it ! - Occured Value Error!')
# else:
#     print('Ok Else')

# print()
# print('pass')


#예제2
# try:
#     z='Kim'
#     x=name.index(z)
#     print('{} Found it! {} in name'.format(z,x+1))
# except: #except Exception: 처럼 쓰기도 함
#     print('Not Found it ! - Occured Value Error!')
# else:
#     print('Ok Else')

# print()
# print('pass')

#예제3
# try:
#     z='Kim'
#     x=name.index(z)
#     print('{} Found it! {} in name'.format(z,x+1))
# except Exception as e:
#     print(e)
#     print('Not Found it ! - Occured Value Error!')
# else:
#     print('Ok Else')
# finally:
#     print('OK Finally')
# print()

#예제4
#예외 발생: raise
#raise 키워드로 예외 직접 발생
try:
    a='Park'
    if a=='Kim':
        print('OK Pass')
    else:
        raise ValueError
except ValueError:
    print("Occured Exception ")

else:
    print("OK else")
    


