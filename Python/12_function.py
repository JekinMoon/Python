'''
함수(function)
- 특정 작업을 수행하는 코드들의 모음
- 복잡한 코드를 작은 단위로 나눌 수 있게 도와줌
- 특정한 코드들을 재사용 할 수 있게 함
'''
'''
# 사용자 정의 함수 기본 문법
# 함수의 정의 : define의 약자로 def 사용
def 함수이름 (매개변수):
    # 실행할 코드
    print(매개변수)
    return "반환값"

# 함수의 실행(호출 call)
result = 함수이름("인자")
print(result)       # 반환값

# 매개변수(Parameter): 매개 + 변수
# 매개 : 둘 사이를 연결해줌
# 함수가 실행될 때 인자로부터 입력되는 값을 함수의 코드블록으로 전달하는 역할


# 함수의 필요성 예제
a = 10
b = 20

if a > b :
    print(a - b)
else:
    print(a + b)

c = 30
d = 40

if c > d :
    print(c - d)
else:
    print(c + d)

#....


def my_func(a, b):
    if a > b:
        return a - b
    else:
        return a + b

print(my_func(10, 20))  # 30
print(my_func(30, 40))  # 70



# <실습1> 사칙연산 계산기 함수 만들기

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return float(a/b)
    else:
        return "지원하지 않는 연산입니다"

print(calculate(10, 20, "+")) # 30
print(calculate(10, 20, "-")) # -10
print(calculate(10, 20, "*")) # 200
print(calculate(10, 20, "/")) # 0.5
print(calculate(10, 20, "#")) # 지원하지 않는 연산입니다



# 키워드 인자
# 예시 1.
print("안녕하세요", "반갑습니다!", sep="-", end=" / ")          # 안녕하세요-반갑습니다! /

# 예시 2.
def my_func(a,b,c = None, operator = None):
    if operator == "+":
        return a + b
    else:
        return c
    
print(my_func(10,20))                                           # None
print(my_func(10,20, operator= "+"))                            # 30

# 기본값 인자
# 단, 기본값 매개변수는 뒤쪽에 위치해야함
def greet(name, message= "안녕하세요~!"):
    print(f"{name}님, {message}")

# 호출 시 인자 생략 -> 기본값 사용
greet("Jekin")                                          # Jekin님, 안녕하세요~!
greet("Jekin", "반갑습니다!")                           # Jekin님, 반갑습니다!

# 위치 가변 인자
# 여러개의 값을 유동적으로 받을 수 있음
# 값이 튜플 형태로 받아짐

def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))                               # 15


# 키워드 가변 인자
# 여러 키워드 인자를 유동적으로 받을 수 있다
# 딕셔너리 형태로 값이 입력됨

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_info(name = "Jekin", age = 20, city = "seoul")            # name : Jekin / age : 20 / city : seoul


# <실습2-1>
def average(*args):
    if len(args) == 0 :
        return "입력값이 없습니다"
    return sum(args) / len(args)

print(average(10,20,30,40,50,60,70,80,90,100))      # 55.0
    

# <실습2-2>
# 1) 
def longgest(*args):
    answer = ""
    for s in args:
        if len(s) > len(answer):
            answer = s
    return answer
print(longgest("apple","watermelon", "grape", "kiwi" ))         # watermelon

# 2)
def longgest2(*args):
    if len(args) == 0:
        return "입력값이 없습니다"
    return max(args, key=len)
print(longgest2("apple","watermelon", "grape", "kiwi" ))         # watermelon

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
def max_word(*args):
    return max(args, key=len)
print(max_word("apple", "banana", "kiwi", "orange", "grape", "pineapple"))   # pineapple


# <실습2-3> 사용자 정보 출력함수
# dict.items() 활용
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_info(name = "Sang-Ik", age = 37, city = "Busan")  # name : Sang-Ik / age : 37 / city : Busan


# <실습2-4>
def discount_price(**kwargs):
    for key, value in kwargs.items():
        discounted = value * 0.9
        print(f"{key} : 할인가 {discounted} (원가 {value})")
discount_price(apple = 2000, watermelon=20000, chocolate=2500)     

 # apple : 할인가 1800.0 (원가 2000) / watermelon : 할인가 18000.0 (원가 20000) / chocolate : 할인가 2250.0 (원가 2500)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def items_list(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value * 0.9}")
items_list(a = 10000, b = 30000)                        # a : 9000.0 / b : 27000.0



# 전역 변수 : 함수 밖에 선언된 변수
# 지역 변수 : 함수 안에 선언된 변수

# 예제

x = 200                     # 전역변수

def my_func():
    x = 10                  # 지역변수
    print(x)                # 10

my_func()                    
print("함수 밖", x)         # 함수 밖 200


# 예제2 (UnboundLocalErr 에러)
x  = 10

def my_func2():
   x = 20                     # 주석 처리 할 경우 UnboundLocalError
   x += 5
   print("지역변수", x)        # 지역변수 25

my_func2()

print("전역변수", x)            # 전역변수 10


# 예제3 (global 사용 예제)

x  = 10

def my_func3():
   global x                 # 전역변수 사용 선언
   x += 5
   print("지역", x)         # 지역변수 15

my_func3()

print("전역", x)            # 전역변수 15


# 권장되는 패턴
# 부수효과(side effect)를 발생시키지 않는 함수를 위주로 프로그래밍

x = 10

def my_func4(x):
   x += 5
   return x

x = my_func4(x)

print("전역", x)



# <실습3> 로그인/로그아웃 전역상태 관리
current_user = None
login_count = 0

def login(name):
   global current_user
   global login_count

   if current_user == None:
      current_user = name
      print(f"{name}님 로그인 성공!")
   else:
      print("이미 로그인되어 있습니다.")
      login_count += 1
      if login_count > 4:
         print("더이상 로그인 시도를 할 수 없습니다.")

def logout():
   global current_user
   global login_count

   if current_user == None:
      print("로그인 상태가 아닙니다")
   else:
      print("로그아웃 되었습니다!")
      current_user = None
      login_count = 0


login("Ian")
login("CodingOwl")
logout()
login("CodingOwl")
print(current_user)


#~~~~~~~~~~~~~~~~~~~~~~~~~~``
current_user = ""
def login(name):
   global current_user

   if current_user == "":
      current_user = name
      print(f"{name}님 로그인 성공!")
   else:
      print("이미 로그인되어 있습니다")

def logout():
   global current_user

   current_user = ""
   print("로그아웃되었습니다")
   
login("Ian")
login("CodingOwl")
logout()
login("CodingOwl")
print(current_user)


# 재귀함수
# 1. 자기 자신을 호출하는 함수
# 2. 반드시 기본 조건 (종료 조건)이 있어야 함
# - 큰 문제를 작은 문제로 나누었을 때 일정한 패턴이 있어야 함

import time

def recursive_func(n):
    # 기본 조건
    if n == 0:
        return
    
    recursive_func(n-1)
    print("재귀 호출", n)
    time.sleep(1)

recursive_func(5)                   # 재귀 호출 1 / 재귀 호출 2 / 재귀 호출 3 / 재귀 호출 4 / 재귀 호출 5



# <실습4> 거듭제곱 (재귀함수와 거듭제곱은 '문제를 자기 자신을 이용해 정의한다'는 공통점을 가진다)
def power_rec(a, b):
    if b == 0:
        return 1
    return a * power_rec(a, b - 1)  # a * a * a * ... * 1 (-> b = 1)

print(power_rec(2,5))           # 32
# 2 * 2 * 2 * 2 * 2 * 2 * 1 -> b = 5, b = 0 이 되는 순간까지 포함 총 6개 곱하기


# <실습5> 팩토리얼
# 반복문
def factorial_num(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial_num(5))         # 120

# 재귀함수
def fact_num(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_num(n-1)
print(fact_num(5))              # 120
    


# <실습6> 피보나치 수열
# 반복문
def fibonacci_for(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b   # (a,b) = (b, a+b)    # 0 1 = 1 1 / 1 1 = 1 2 / 1 2 = 2 3 / 2 3 = 3 5 / 3 5 = 5 8
    return b

print(fibonacci_for(6))          # 8

# 재귀함수
def fibo_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibo_rec(n - 1) + fibo_rec(n - 2) 

print(fibo_rec(6))              # 8
print(fibo_rec(8))              # 21
print(fibo_rec(10))             # 55
print(fibo_rec(12))             # 144


'''

# 람다 (lambda) 함수
# 익명 함수
# 간단한 함수를 한줄로 표현할 때 사용

# 람다 함수의 기본 문법
# lambda 매개변수: 표현식
# - 표현식 :  값이 반환되는 식

# 일반 함수
def add(x, y):
    return x + y

# 람다함수 
add_func = lambda x, y : x + y
print(add_func(3, 5))               # 8

# 람다로 값을 반환하고 사용을 끝내는 경우
print((lambda x: x ** 2)(10))       # 100


# 람다 함수의 활용
# 1. map 에서 활용
my_list = [1,2,3,4]

# 일반 함수를 사용
def square_func(x):
    return x ** 2

# 함수를 인자로 받는 함수
print(list(map(square_func, my_list)))          # [1, 4, 9, 16]

# 람다함수를 사용
print(list(map(lambda x : x ** 2, my_list)))    # [1, 4, 9, 16]


# 2. filter 에서 활용
my_list2 = [1,2,3,4,5,6,7,8,9,10]

# 일반 함수 사용
def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, my_list2)))                  # [2, 4, 6, 8, 10]

print(list(filter(lambda x : x % 2 == 0, my_list2)))    # [2, 4, 6, 8, 10]


# 3. sorted 에서 활용
my_list3 = ["apple", "banana", "watermelon", "grape"]
print(sorted(my_list3, key=lambda word: len(word)))     # ['apple', 'grape', 'banana', 'watermelon']




# <실습 7-1> 특정조건 만족하는 튜플만 추출하기
students = [("Alice", [80, 90]), ("Bob", [60, 65]), ("Charlie", [70, 70])]

print(list(filter(lambda s : sum(s[1])/len(s[1]) >= 70, students)))   # [('Alice', [80, 90]), ('Charlie', [70, 70])]


# <실습 7-2> 키워드 맨 앞단어만 추출 리스트 만들기
sentences = ["Python is fun", "Lambda functions are powerful", "Coding is creative"]
print(list(map(lambda s : s.split()[0], sentences)))    # ['Python', 'Lambda', 'Coding']


# <실습 7-3> 튜플 리스트에 있는 나이를 기준으로 오름차순 정렬하기
people = [("Alice", 30), ("Bob", 25), ("Charlie",35)]

print(sorted(people, key=lambda age : age[1]))        # [('Bob', 25), ('Alice', 30), ('Charlie', 35)]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
solution = lambda a, b: max(int(str(a) + str(b)), 2 * a * b)
print(solution2(2, 91))
print(solution2(91, 2))