# 홍길동의 평균 점수를 구해라
a = 80
b = 75
c = 55
result = int((a + b + c) / 3)
print(result)

# 자연수 13이 홀수인지 짝수인지 판별
a = 13
if a%2==0:
    print("짝")
        
if a%2==1:
    print("홀")


# 주민등록번호를 앞뒤로 나눠서 출력
a = "971125-1234567"
yyyymmdd = a[:6]
num = a[7:]
print(yyyymmdd, num)

# 문자열 a:b:c:d를 replace 함수를 사용하여 a#b#c#d로 출력
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 출력
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# ['Life','is','too','short'] 리스트를 Life is too short 문자열로 출력
a = ['Life','is','too','short']
result = a[0]+" "+a[1]+" "+a[2]+" "+a[3]
result = " ".join(a)
print(result)

# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)로 출력
a=(1,2,3)
a = a+(4,)
print(a)

# a[[1]] = 'python'을 실행하면 에러발생 이유는?
# 딕셔너리의 key값에는 리스트(배열)를 선언할 수 없다.

# a 딕셔너리에서 'B'의 값을 추출
a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(result)

# a 리스트에서 중복된 숫자들을 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet= set(a)
print(aSet)
a=list(set(a))
print(a)

# while문으로 1~1000까지의 자연수 중 3의 배수의 합
result=0
i=1
while i <=1000:
    if i%3==0:
        result +=i
    i+=1

print(result)

# while문을 사용하여 별찍기 작성
i=0
while i<=5:
    i+=1
    if i>5: break

    print("*"*i)

# for문을 사용해 1~100까지의 숫자 출력
for i in range(1,101):
    print(i)

# for문을 사용하여 학급의 평균 점수를 구해라
a=[70,60,55,75,95,90,80,80,85,100]
result =0

for i in a:
    result +=i

avg=result/len(a)
print(int(avg))

# 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드에
# 내포(list comprehension)를 사용하여 표현
numbers = [1,2,3,4,5]

result=[]
for n in numbers:
    if n%2==1:
        result.append(n*2)

result1 = [n*2 for n in numbers if n%2 ==1]
print(result1)

# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해보자
def is_odd(number):
    if number % 2 == 1:
        return True
    else :
        return False

print(is_odd(4))
print(is_odd(3))

# 입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수를 작성해보자
def avg_input_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_input_numbers(1,28,9,10))

# 3과 6을 입력했을 때 9아 아닌 36이라는 결과값을 돌려주었을 때 오류를 수정
input1 = input("첫 번째 숫자를 입력하세요 : ")
input2 = input("두 번째 숫자를 입력하세요 : ")

result = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." %result)