#딕셔너리 쌍 추가, 삭제하기
# json 데이터폼이랑 똑같음{key :value}

#딕셔너리 쌍 추가하기
a = {1:'a'}
a[2]='b'
print(a)

a['name']='Lee'
print(a)

a[3]=[1,2,3]
print(a)

#딕셔너리 요소 삭제하기
# del a[key] 지정된 Key에 해당은 딕셔너리가 삭제된다.
del a[1]
print(a)

#딕셔너리를 사용하는 방법
#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey':10,'julliet':99}
print(grade['pey'])
print(grade['julliet'])

a = {1:"a",2:'b'}
print(a[1])
print(a[2])

dic = {'name': 'Lee', 'phone':'01092541305', 'birth':'1125'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리 만들 때 주의할 사항
# dic에서 key값은 고유하므로 중복되는 key값을 설정해 놓으면 마지막 하나를 제외한 나머지 것들이
# 모두 무시된다.
# 리스트(배열)를 key값으로 사용할수 없다. // a = {[1]: value} 불가

#딕셔너리 관련 함수들
#Key 리스트 만들기(keys)
dic = {'name': 'Lee', 'phone':'01092541305', 'birth':'1125'}
print(dic.keys())

for k in dic.keys():
    print(k)


#Value 리스트 만들기(values)
print(list(dic.keys()))

#Key, Value 쌍 얻기(items)
print(dic.items())

#Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)

#Key로 Value얻기(get)
print(dic.get('name'))
print(dic['name'])

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in dic)
print('email' in dic)