#External Function
# 종류: sys,pickle, shutil, temfile, time,random

#예제1
import sys
print(sys.argv) #google 검색

#예제2
#sys.exit()

#예제3 파이썬 패키지 위치
print(sys.path)

#pickle: 객체 파일쓰기

import pickle 

#예제4 쓰기
f=open("test.obj", "wb")
obj={1:'pytho',2:"study", 3:'basic'}
pickle.dump(obj,f)

f.close()

#예제5 읽기
f=open('test.obj','rb') #read/binary 읽기
data = pickle.load(f)
print(data, type(data))
f.close()

#os: 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 관련
#mkdir, rmdir(비어있으면 삭제), rename

#예제6
import os
print(os.environ)
print(os.environ["USERNAME"])

#예제7(현재경로)

print(os.getcwd())

#time: 시간 관련 처리
import time
#예제8
print(time.time())

#예제9
print(time.localtime(time.time()))

#예제10
print(time.ctime())

#예제11
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#예제12
for i in range(5):
    print(i)
    time.sleep(1)

#random 
import random

#예제13
print(random.random()) #0~1 실수
#예제14
print(random.randint(1,45))
print(random.randrange(1,45))
#예제15 섞기
d=[1,2,3,4,5,6]
random.shuffle(d)
print(d)

#예제16(무작위 선택)
c = random.choice(d)
print(c)


#webrowser : 본인 os의 웹브라우저 실행

import webbrowser
webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com')
