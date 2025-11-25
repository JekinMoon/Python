# 모듈
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것

'''
# 모듈 불러오기(1)
import hello 
hello.greeting("lee")               # Hello, lee!

# 모듈 불러오기(2)
from hello import greeting
greeting("lee")                     # Hello, lee!

# 모듈 불러오기(3)
from hello import * #전체불러오기
introduce("sin", 20)                # 제 이름은 sin이고, 나이는 20입니다.

# 모듈 불러오기(4)
import hello as h   # 별칭 사용 
h.greeting("kim")                   # Hello, kim!


# <실습1>
import calc as c

print(c.add (3,5))              # 8
print(c.subtract (5,3))         # 2
print(c.multiply(4,6))          # 24
print(c.divide (6,4))           # 1.5
print(c.divide (2,0))           # 0으로 나눌 수 없습니다. / None

    
# 패키지
# 모듈의 묶음
# 모듈을 폴더 단위로 묶어놓은 것

# 패키지에서 모듈 불러오기(1)
from my_package import calc as c

print(c.add(10, 20))                # 30

# 패키지에서 모듈 불러오기(2)
from my_package.calc import add
print(add(10, 20))                  # 30


# 파이썬 표준 라이브러리

# math 모듈 : 수학적 연산에 사용되는 모듈
import math as m

# 1. 올림 / 내림
# ceil : 올림, 소수점 지정 X
print(m.ceil(3.14))                 # 4

# floor : 내림, 소수점 지정 X
print(m.floor(3.14))                # 3

# round : 반올림, 파이썬 내장함수
print(round(3.141592, 2))           # 3.14

# 2. 제곱, 제곱근
# pow(x, y) : 제곱 - x^y
print(m.pow(2,3))                   # 8.0

# sqrt(x) : 제곱근 반환
print(m.sqrt(16))                   # 4.0

# 3. 상수
# pi : 원주율
print(m.pi)                         # 3.141592653589793

# 4. 수학 계산 편의 기능
print(m.factorial(3))               # 6

# 최대 공약수
print(m.gcd(12, 20))                # 4

# 최소 공배수
print(m.lcm(12, 20))                # 60
'''

# <실습2-1> 실제 거리 계산: 좌표 두 점 사이 거리 구하기
import math as m

x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# x1, y1 = int(x1), int(y1)
x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

dist = round(m.sqrt(m.pow((x2-x1),2) + m.pow((y2-y1),2)))

print(f"두점 사이의 거리: {dist: }")

# 0034
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
x1 = int(input("x1의 좌표 입력: "))                 # 1
y1 = int(input("y1의 좌표 입력: "))                 # 3
x2 = int(input("x2의 좌표 입력: "))                 # 5
y2 = int(input("y2의 좌표 입력: "))                 # 7

distance = m.sqrt(m.pow((x2-x1),2) + m.pow((y2-y1),2), 2)

print(f"두점 사이의 거리: {distance:.2f}")          # 두점 사이의 거리: 5.66


# <실습2-2> 상품 나누기: 최소 공배수와 최대 공약수
# math.gcd(), math.lcm() 

import math as m

students = 18
teachers = 24

max_snacks = m.gcd(students, teachers)
min_snacks = m.lcm(students, teachers)

print(f"최대 간식 개수는: {max_snacks} 개")         # 최대 간식 개수는: 6 개
print(f"최소 간식 개수는: {min_snacks} 개")         # 최소 간식 개수는: 72 개
'''