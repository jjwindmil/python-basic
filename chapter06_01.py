#객체 지향
#oop, self, 인스턴스 메소드, 인스턴스 변수
#클래스 와 인스턴스의 차이 이해
# 네임스페이스: 객체를 인스턴스화 할때 저장된 공간 (내부 변수)
#클래스 변수는 직접 접근, 아래예에서는 species 가 클래스 변수
# 인스턴스 변수는 각각 다름
#예제1

class Dog: #모든 클래스는 object를 상속받는다
    #클래스 속성
    species = 'firstdog'
    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #클래스의 초기화 함수는 __init__(첫번째 인자는 self)

#클래스 정보 (틀 정보, 설계도)
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("test", 5)
d = Dog("test", 5)

#비교
print(a==b, id(a),id(b),id(c), id(d))

#네임스페이스
print("a : ", a.__dict__) #딕셔너리 형태
print("b : ", b.__dict__)


#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name,a.age,b.name,b.age))

if a.species =='firstdog':
    print('{0} is a a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

#예제2
#self 의 이해

class SelfTest:
    def func1(): #클래스메소드임
        print('Func1 called')
    def func2(self):#인스턴스 메소드임
        print(id(self))
        print('Func2 called')

f=SelfTest();
print(dir(f))

print(id(f))
#f.func1() #error 발생 예외처리 우선함.
SelfTest.func1()
#SelfTest.func2() #에러 발생하는게 맞음 인스턴스 메소드이기때문에 아래처럼 호출해야함
SelfTest.func2(f)


#클래스 변수, 인스턴스 변수
class Warehouse:
    #클래스 변수
    stock_num=0 #재고

    def __init__(self,name):
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num+=1

    def __del__(self):
        Warehouse.stock_num-=1


user1 = Warehouse("Lee")
user2 = Warehouse("Cho")


print(Warehouse.stock_num)

#Warehouse.stock_num=50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print(user1.stock_num)


#인스턴스를 메모리에서 삭제
del user1
print('after ', Warehouse.__dict__)


#예제4

class Dog: #모든 클래스는 object를 상속받는다
    #클래스 속성
    species = 'firstdog'
    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #클래스의 초기화 함수는 __init__(첫번째 인자는 self)

    def info(self):
        return '{} is {} yeard old'.format(self.name, self.age)
    
    def bark(self, sound):
        return "{} says {} !!".format(self.name, sound)



#인스턴스 생성
c= Dog('july',4)
d= Dog("Marry", 6)
#메소드 호출
print(c.info())
print(c.bark("Wal Wal"))
print(d.bark("Mung Mung"))

