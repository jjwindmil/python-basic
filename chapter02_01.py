# Chapter02-01
# 파이썬 완전 기초
# print

# 기본출력
import sys
print()

# seperator
print("P", "Y", "T", "H", "O", "N", sep="|")
print("010", "1111", "1234", sep="-")
print("python", "google.com", sep="@")

# end 옵션
print("Test  end option", end="")
print("kikiki")

# file 옵션

print("learn python", file=sys.stdout)
# print("learn python", file="test.txt") 해당 파일에 문장을 쓰는 형식


# format(d,s,f) 옵션
# %s
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('onew', 'two'))

print('%10s' % ("nice"))
print("{:>10}".format("nice"))

print("%-10s" % ("niceeee"))
print("{:10}".format("niceeee"))

print("{:_>10}".format("nice"))
print("{:^10}".format("nice"))

print("%.5s" % ("nice"))
print("%10.5s" % ("nicestudy"))

print("{:10.5}".format("nicestudy"))

# %d
print("%d %d" % (1, 2))
print("{} {}".format(1, 2))
print("%4d" % (42))
print("{:4d}".format(42))

# %f

print("%f" % (3.1414141414141414))
print("{:f}".format(3.1415926539))

print("%06.2f" % (3.14159265432892))
print("{:06.2f}".format(3.14159265432892))
