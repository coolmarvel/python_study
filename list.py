#리스트 자료형
#리스트의 인덱싱과 슬라이싱
#리스트의 인덱싱
a=[1,2,3]
print(a[0])
print(a[1]+a[2])
print(a[-1])

b = [1,2,3,['a','b','c']]
print(b[3])
print(b[3][1])
print(b[-1][1])

#리스트의 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])
print(a[:2])
print(a[2:])

a="12345"
print(a[0:2])

#리스트 연산하기
a=[1,2,3]
b=[4,5,6]

#리스트 더하기(+)
print(b+a)
print(a+b)

#리스트 반복하기(*)
print(a*3)

#리스트 길이구하기
print(len(a))

#리스트의 수정과 삭제
a[2]=4
print(a)

del a[1]
print(a)

#리스트에서 값 수정하기
#del 함수 사용해 리스트 요소 삭제하기
a = [1,2,3,4,5]
del a[2:]
print(a)

#리스트 관련 함수들
#리스트에 요소 추가(append)
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
print(a)

#리스트 뒤집기(reverse)
a=['a','c','b']
a.reverse()
print(a)

#위치 반환(index)
a=[1,2,3]
print(a.index(3))
print(a.index(1))

#리스트에 요소 삽입(insert)
a=[1,2,3]
a.insert(0,4)
print(a)
a.insert(3,5)
print(a)

#리스트 요소 제거(remove)
a=[1,2,3,1,2,3]
print(a)
a.remove(3)
print(a)

#리스트 요소 끄집어내기(pop)
a=[1,2,3]
a.pop(1)
print(a)

#리스트에 포함된 요소 x의 개수 세기(count)
a=[1,2,3,1]
print(a.count(1))

#리스트 확장(extend)
a=[1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
print(a)
# a.extend([4,5])는 a += [4,5]와 동일하다.