#파일 읽기쓰기
#읽기모드 r, 쓰기모드 w, 추가모드 a, 텍스트모드 t, 바이너리 b
#상대경로 (../) (./) , 절대경로('C:/Django/example..')

#파일 읽기(read)

#예제1

f= open('./resource/it_news.txt', 'rt', encoding='UTF-8') #기본 인코딩 파이선은 utf-8
#속성확인

print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
cts= f.read()
print(cts)
f.close()


#예제2
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c=f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

#예제3
#read(): 전체읽기, read(10): 10byte #int형에 맞는 바이트수만큼 읽어온다
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c=f.read(20)
    print(c)
    c=f.read(30)
    print(c)
    #커서가 내부적으로 읽은 범위까지를 기억하고 있따.
    f.seek(0,0)
    c=f.read(20)
    print(c)

print()

#예제4
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c=f.readline()
    print(c)

print()

#readlines: 전체를 읽은후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts=f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
    

#파일쓰기
with open('./resource/contents1.txt','w') as f:
    f.write('I love python\n')
#예제2
with open('./resource/contents1.txt','at') as f:
    f.write('I love python2222\n')

#예제3
#writelines : 리스트->파일
with open('./resource/contents2.txt','w') as f:
    list=['Oragne\n','Apple\n','Banana\n','Melon\n']
    f.writelines(list)

#예제4
with open('./resource/contents3.txt','at') as f:
    f.write('Test Text Wirte', file =f)
    f.write('Test Text Wirte', file =f)
    f.write('Test Text Wirte', file =f)
