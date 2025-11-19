'''
# for문
# - 이터러블(순회 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

# 리스트 반복
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}")                    # I like apple / I like banana / I like cherry

# 문자열 반복
my_str = "Apple"
for char in my_str:
    print(char)                                 # A p p l e

# 튜플 반복
coords = [(1,2), (10,15), (-6,8)]

# 언패킹 (구조분해 가능)
for x,y in coords:
    print(f"x좌표: {x}, y좌표: {y}")            # x좌표: 1, y좌표: 2 / x좌표: 10, y좌표: 15 / x좌표: -6, y좌표: 8

# 딕셔너리 반복
person = {
    "name": "kim",
    "age": 15,
    "address": "seoul"
}

# 기본
for key in person:
    print(f"key: {key}, value: {person[key]}")      # key: name, value: kim / key: age, value: 15
                                                    # key: address, value: seoul

# value 만 가져오기
for value in person.values():                       
    print(f"value: {value}")                        # value: kim / value: 15 / value: seoul

# item 가져오기
for key, value in person.items():
    print(f"key:{key}, value: {person[key]}")       # key:name, value: kim / key:age, value: 15 / key:address, value: seoul


# set 반복
my_set = {1,2,3,4}

for s in my_set:
    print(s)                                        # 1 / 2 / 3 / 4

# <실습 1-1>
numbers = [3, 6, 1, 8, 4]
doubled = []

for number in numbers:
    doubled.append(number * 2)
print(doubled)                 # [6, 12, 2, 16, 8]

# <실습 1-2>
words = ["apple", "banana", "kiwi", "grape"]
lengths = []
for word in words:
    lengths.append(len(words))
print(lengths)                  # [5, 6, 4, 5]

# <실습 1-3>
coordinates = [(1,2), (3,4), (5,6), (7,8)]

x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)
print(f"x좌표: {x_values}")         # x좌표: [1, 3, 5, 7]
print(f"y좌표: {y_values}")         # y좌표: [2, 4, 6, 8]


# for문과 range( )
# range 함수 : 지정된 범위의 정수 시퀀스 생성

# 기본 문법
# range(start, end, step)
# - start: 생략 가능. 기본값 0
# - end: end -1 까지 생성
# - step: 생략 가능. 기본값 1

range(1,5)

for i in range(1,5):
    print(i)            # 1 2 3 4

for i in [1,2,3,4]:
    print(i)            # 1 2 3 4



# start 생략
for i in range(10):
    print(i)            # 0 1 2 3 4 5 6 7 8 9


# 간격 (step) 지정
for i in range(0,11,2):
    print(i)            # 0 2 4 6 8 10

for i in range(11,0,-2):
    print(i)            # 11 9 7 5 3 1


# <실습2-1>
sum = 0
for i in range(1,11):
    sum += i
print(sum)                # 55
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
num = int(input("숫자를 입력하세요: "))
sum = 0

for i in range(num +1):
    sum += i
print(sum)

# <실습 2-2>
dan = int(input("출력하고 싶은 단을 입력하세요: "))
for i in range(1,10):
    print(f"{dan}x{i} = {dan*i}")       # 3단 (3x1 = 3 / 3x2 = 6 / 3x3 = 9 / 3x4 = 12 / 3x5 = 15 / 3x6 = 18 / 3x7 = 21 / 3x8 = 24 / 3x9 = 27)


# <실습 2-3>
result = 0
for i in range(3,101,3):
    result += i
for i in range(1,101):
    if i % 3 == 0:
        result += i

print("3의 배수의 합: ", result)                # 3366



# <실습 2-4>
n = int(input("숫자를 입력하세요: "))
for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i)        # 100 (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(10,n+1,10):
    print(i)            # 100 (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)



# 루프 제어문 (break, continue, pass)
# - 특정 조건 하에서만 작동하도록 구현
# 
# break : 반복을 즉시 중단
for i in range(10):
    print(i)                        # 0 1 2 3 4 5
    if i == 5:
        break
    print(i)
print("반복종료")                   # 0 1 2 3 4 반복종료


# continue : 현재 반복을 넘어감
for i in range(5):
    if i == 2:
        print("continue = 건너뜀")
        continue
    print(i)                        # 2 실행 안함
print("반복종료")                   # 0 1 continue=건너뜀 3 4 반복종료 


# pass : 아무 동작도 하지 않고 자리만 차지
for i in range(10):
    pass


# for - else 구문
for i in range(5):
    print(i)                        
else:
    print("반복종료")               # 0 1 2 3 4 반복종료

for i in range(5):
    if i == 2:
        break
    print(i)                        # 0 1
else:
    print("반복종료") 


# 중첩 for문
# - 하나의 for 문 안에 다른 for 문이 들어있는 구조


# 이중 for 문
for i in range(5):
    for j in range(5):
        print("i, j", i, j)
    print()                             #  i, j 0 0 / i, j 0 1 / i, j 0 2 / i, j 0 3 / i, j 0 4
                                        #  i, j 1 0 / i, j 1 1 / i, j 1 2 / i, j 1 3 / i, j 1 4
                                        #  i, j 2 0 / i, j 2 1 / i, j 2 2 / i, j 2 3 / i, j 2 4
                                        #  i, j 3 0 / i, j 3 1 / i, j 3 2 / i, j 3 3 / i, j 3 4
                                        #  i, j 4 0 / i, j 4 1 / i, j 4 2 / i, j 4 3 / i, j 4 4



 

# <실습3-1>
for i in range(2,10):
    print(f"[{i}단]")
    for j in range(1, 10):
        print(f"{i}x{j} = {i*j}")
    print()


# <실습3-2>
#1)
n = int(input("몇 줄?> "))
for i in range(1, n+1):
    print('*' * i)

n = int(input("몇 줄?> "))
for i in range(1, n+1):
    print((" " * ( n - i ) + "*" * ( 2 * i - 1)))

n = int(input("몇 줄?> "))
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)

#2)
# 왼쪽 정렬
n = int(input("몇 줄?> "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

# 가운데 정렬
n = int(input("몇 줄?> "))

for i in range(1, n+1):
    # 공백 출력
    for j in range(n-i):
        print(" ", end="")
    # 별 채우기
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 오른쪽 정렬
n = int(input("몇 줄?> "))

for i in range(1, n+1):
    # 공백 출력
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

    

  
'''


# 리스트 컴프리헨션
# - for문을 리스트에 한줄로 축약하여 새 리스트를 생성하는 문법
# - [표현식(리스트의 원소) for 변수 in 반복대상 if 조건]
# - 표현식 : 값을 유도하는 식 (표현)

# for문 이용
squares = []
for x in range(1,6):
    squares.append(x ** 2)
print(squares)              # [1, 4, 9, 16, 25]

# 리스트 컴프리헨션
squares2 = [x ** 2 for x in range(1,6)]
print(squares2)             # [1, 4, 9, 16, 25]


# 조건문 추가하기
squares3 = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares3)             # [4, 16, 36, 64, 100]


# <실습4-1> 제곱값 리스트 만들기
squares = [x ** 2 for x in range(1,11)]
print(squares)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# <실습4-2> 3의 배수만 리스트로 만들기
result = [x for x in range(1, 51) if x % 3 == 0]
print(result)             # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# <실습4-3> 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
words = [fruit for fruit in fruits if len(fruit)>=5]
print(words)             # ['apple', 'banana', 'cherry', 'orange']



