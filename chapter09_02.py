#csv 파일 읽기 및 쓰기
#csv:MEME - text/csv 통신타입

import csv
#예제1
with open('/resource/test1.csv','r') as f:
    reader = csv.reader(f)
    #객체 확인
    print(reader)
    #next(reader) #header skip 할때 사용
    #타입
    print(type(reader))
    #속성
    print(dir(reader))
    print(dir(reader)) #__iter__

    print()

    for c in reader:

        print(c)
        #타입확인
        print(type(c))
        #list to str

        print(''.join(c))

#예제2
with open('/resource/test2.csv','r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:

        print(c)
        

#예제3
with open('/resource/test2.csv','r') as f:
    reader = csv.DicReader(f)
    print(reader)
    #next(reader) #header skip 할때 사용
    #타입
    print(type(reader))
    #속성
    print(dir(reader))
    for c in reader:
        print(c)
        for k,v in c.items():
            print(k,v)
        print('--------------')
    
    
#예제4
w=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv','w',encoding='utf-8') as f:
    print(dir(csv))
    wt=csv.writer(f)

    #dir 확인
    #print(dir(wt))
    #타입 확인
    #print(type(wt))
    for v in w:
        wt.writerow(v)
    

#예제5
with open('./resource/write2.csv','w',encoding='utf-8') as f:
    #필드명

    fields= ['one','two','three']

    #dict writer
    wt=csv.DictWriter(f, fieldnames=fields)
    #header wirter
    wt.writeheader

    for v in w:
        wt.writerow({'one':v[0],'two':v[1],'three':v[2]})
        