#파이썬 패키지
#패키지 작성 및 사용법
#파이선은 패키지로 분할 된 개별적인 모듈로 구성
#상대경로 ..(), .(모듈 내부에서만 사용)
#__init__.py :Python3.3 부터는 없어도 패키지로 인식 > 단 , 하위 호환을 위해 작성을 추천
#__init__.py : __all__ = ['module1','moduleTest'] 허가할 모듈 설정
#예제
import sub.sub1.module1
import sub.sub2.module2

#사용

sub.sub1.module1.mod1_test2()
sub.sub1.module1.mod1_test1()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()


#예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 #alias


module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test2()
m2.mod2_test1()

print()
print()
print()


#예제3

from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test2()
module1.mod1_test1()

module2.mod2_test1()
module2.mod2_test2()

#pychache 는 런타임시 빠르게 실행을 위해 파이썬이 생성 하는 런타임 환경 캐시


