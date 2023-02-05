#파이썬 내장 함수
#str(), int(), tuple 형변환 이미 학습
#절대값 abs()
from re import A


print(abs(-3))
#all: iterable 요소 검사(참, 거짓) 모두 만족해야
print(all([1,2,3]))
#any: 하나라도 만족하면 오케
print(any([1,2,0]))

#chr: 아스키 -> 문자, ord: 문자->아스키

print(chr(67))
print(ord('C'))

#enumerate: 인덱스 +iterable 객체 생성

for i, name in enumerate(['abc','bcd','efg']):
    print(i, name)


#filter 반복가능한 객체요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x)>2

print(list(filter(conv_pos,[1,-3,2,0,-5])))
print(list(filter(lambda x: abs(x)>2, [1,-3,2,0,1])))

#id: 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

#len : 욧소의 길이 반환
print(len('1dfsdfsad'))
print(len([12,34,5,6,7,7]))

#max min
print(max([1,2,3,4,5]))
print(min(['python study']))

#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-2,3,4,-10])))
print(list(lambda x: abs(x),[1,-2,-9,-10]))

#pow :제곱 값 반환
print(pow(2,10))

#range: 반복가능한 객체(iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

#round 반올림
print(round(6.2323,3))
print(round(5.6))

#sorted :반복가능한 객체 (list tuple set, dic) 정렬후 반환
print(sorted([6,7,12,3,54,2]))
a= print(sorted([6,7,12,3,54,2]))
print(a)

#sum: 반복가능한 객체의 합 반환
print(sum([6,7,8,9,0,1]))
print(sum(range(1,101)))


#type 
print(type(3))
print(type({}))
print(type(()))
print(type([]))

#zip :반복가능한 객체의 요소를 묶어서 반환 튜플로반환?
print(list(zip([10,20,30],[40,50,60])))


