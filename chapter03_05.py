# json 형태로 비슷
# {}
# 순서가 없음, 키 중복 허용안함, 수정 가능, 삭제가능

# 선언
a = {'name': 'kim', 'phone': '011132323', 'birth': '1878723'}
b = {1: "lee", 0: "Heelo"}
c = {'arr': [1, 2, 3, 4, 5]}
d = {
    'Name': "NiceMan",
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}

e = dict([
    ('Name', 'NiceMan'),
    ('City', 'Seoul'),
    ('Age', '33'),
    ('Grade', 'A'),
    ('Status', True)

])

f = dict(
    Name='NiceMan',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)


print(type(a), a)

print(a['name'])
print(a.get('name'))
# print(a['name2'])  # 존재하지않으면 에러발생
print(a.get("name2"))  # 존재하지않으면 None


# 딕셔너리 추가
a['address'] = 'seoul kangseoku'
print(a)
a['rank'] = [1, 2, 3,]
print(a)

print(len(a))
print(len(b))

# dict_keys, dict_values, dict_items: 반복문(__iter__) 에서 사용가능
print(a.keys())
print(a.values())
print(a.items())

print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))  # 튜플 형태로 리스트로 만듬

print(a.pop('name'))
print(a)

print(a.popitem())  # 랜덤하게 pop 함

print('birth' in a)
print('birrrth' not in a)

# 수정
a['test'] = 'test_dice'

a['address'] = 'dddd'

a.update(birth='910101010')
print(a)
temp = {'birth': '23131232'}
a.update(temp)
print(a)
