#들여쓰기
#조건문이란 무엇인가?
#비교연산자
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시 가능")
else:
    print("걸어서 집에")

#x in s, x not in s
print('a' in ('a','b','c'))
print('n' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시 가능")
    pass
else:
    print("택시 불가능")

#다양한 조건을 판단하는 elif
pocket = ['paper','cellphone']
card =True
if 'money' in pocket:
    print('택시 가능')
elif card:
    print('택시 가능')
else:
    print("택시 불가능")

#조건부 표현식
score = 100
if score >= 60:
    message ="success"
else:
    message = "filure"

message = "success" if score >=60 else "failure"
print(message)