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


# <실습2-1> 실제 거리 계산: 좌표 두 점 사이 거리 구하기
import math as m

x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))    # (0,0)
# x1, y1 = int(x1), int(y1)
x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))    # (3,4)

dist = round(m.sqrt(m.pow((x2-x1),2) + m.pow((y2-y1),2)))

print(f"두점 사이의 거리: {dist: }")                            # 두점 사이의 거리: 5

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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



# random 모듈 :  랜덤 값(난수) 생성시 사용
import random

# 1. 난수 생성

# random() : 0 이상 1 미만의 float 난수 반환
print(random.random())

# uniform(a,b) : a 이상 b 이하의 실수 난수 반환
print(random.uniform(1, 10))

# randint(a,b) : a 이상 b 이하의 정수 난수 반환
print(random.randint(1, 100))

# randrange(start, stop, step) : 범위 안의 정수 난수 반환, 간격 지정 가능
print(random.randrange(0, 100, 5))

# 2. 랜덤 선택
fruits = ["apple", "banana", "watermelon", "grape", "orange"]

# choice(seq) :  시퀀스에서 임의의 요소 1개 반환
print(random.choice(fruits))

# choices(seq, k) :  시퀀스에서 "중복 허용" k개 요소 리스트 반환
print(random.choices(fruits, k=2))

# 섞기
# sample(seq, k) : 시퀀스에서 "중복 없이" k개 요소 리스트 반환
print(random.sample(fruits, k=2)) 

# shuffle(seq) : 시퀀스의 요소를 무작위로 섞음 -> 원본 시퀀스를 변경함
numbers = [1,2,3,4,5]
print(random.shuffle(numbers))
print(numbers)


# <실습3> 로또 번호 뽑기
# 1)
import random
result = sorted(random.sample(range(1,46), k=6))
print(result)

# 2)
lotto = []
while len(lotto) < 6:
    number = random.randint(1, 45)
    if number in lotto:
        continue
    lotto.append(number)

lotto.sort()
print(lotto)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
nums = range(1,46)
print(sorted(random.sample(nums, k=6)))     # [14, 16, 29, 36, 37, 40]



# <실습4> 가위, 바위, 보 게임 만들기
import random

RPS = ["가위", "바위", "보"]
win_count = 0

while win_count < 3:
    com_choice = random.choice(RPS)
    user_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")

    print(f"유저의 선택: {user_choice}")
    print(f"컴퓨터의 선택: {com_choice}")

    if user_choice == com_choice:
        print("무승부")
    elif((user_choice == '가위'and com_choice == '보') or 
        (user_choice == '바위'and com_choice == '가위') or 
        (user_choice == '보'and com_choice == '바위')):
        print("승리")
        win_count += 1
    elif user_choice in RPS:
        print("패배")
    else:
        print("잘못된 입력입니다.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random

options = ["가위", "바위", "보"]

computer = random.choice(options)
user = input("가위, 바위, 보 중 하나만 입력하세요: ")

if user not in options:
    print("잘못된 입력입니다. 가위, 바위, 보 중 하나만 입력하세요!")

else:
    if user == computer: 
        print("무승부")
    elif (user == '가위'and computer == '보') or (user == '바위'and computer == '가위') or (user == '보'and computer == '바위'):
        print("승리")
    else:
        print("패배")




# datetime 모듈
# 날짜와 시간의 생성, 조작, 현실 변환과 같은 시간 관련 기능을 제공한다
import datetime

# 1. 날짜/시간 구하기
# 현재 날짜와 시간 구하기
now = datetime.datetime.now()
print(now)

# 오늘 날짜만 구하기
today = datetime.date.today()
print(today)

# 2. 날짜/시간 형식 변환
formatted = now.strftime("%Y/%m/%d %H:%M:%S") 
print(formatted)

parsed = datetime.datetime.strptime(formatted,"%Y/%m/%d %H:%M:%S")
print(parsed)                              


# 3. 날짜/시간 연산
dt = datetime.date(2025, 11,4)
passed_time = today - dt
print(f"{passed_time.days}일이 지났습니다.")

# 4. 요일 반환 : weekday
# 0: 월요일 ~ 7: 일요일
days = ["월", "화", "수", "목", "금", "토", "일"]
day_num = today.weekday()
print(days[day_num])

# datetime 또는 date 객체에는 년/월/일 시간 등이 속성으로 들어있음
print(datetime.datetime.now().year)


# <실습 5> 다음 생일까지 남은 날짜 계산하기
import datetime
# 사용자로부터 생일을 입력받음
b_month,b_day = map(int, input("생일을 입력해주세요(MM-DD): ").split("-"))
# 오늘 날짜 구하기
today = datetime.date.today()
# 올해 생일을 date 객체로 변환
b_day_this_year = datetime.date(today.year, b_month, b_day)
# 오늘 날짜와 올해 생일을 비교
if today > b_day_this_year:
    # 올해 생일이 지났으면 내년으로 설정
    b_day_next = datetime.date(today.year + 1, b_month, b_day)
else:
    # 올해로 설정
    b_day_next = b_day_this_year

# 남은 일수 계산
days_left = (b_day_next - today).days
print(f"다음 생일까지 {days_left}일 남았습니다.")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import datetime

month, day = map(int, input("생일을 입력해주세요(MM-DD): ").split("-"))
today = datetime.date.today()
b_day = datetime.date(today.year, month, day)

if b_day < today:
    b_day = datetime.date(today.year + 1, month, day)
d_day = (b_day - today).days
print(f"생일:  {month}월 {day}일")

if d_day == 0:
    print("생일 축하합니다.")
else:
    print(f"생일까지 {d_day}일 남았습니다")   # 생일: 7월 25일 / 생일까지 241일 남았습니다
                                            


# calender 모듈
# 날짜와 달력 관련 기능을 제공

import calendar

# 달력 조회
print(calendar.prmonth(2025,11))
print(calendar.prcal(2026))

# 텍스트로 값을 반환
print(calendar.month(2025, 11))

# 요일 반환
print(calendar.weekday(2025, 12,1))       # 2   (0: 월요일 ~ 7: 일요일)


# time 모듈
# 시간의 측정, 지연, 변환과 같은 시간 관련 기능 제공

import time

# 1. 시간 반환
# time()
# Unix 타임스탬프로 반환 (1970.1.1부터 경과 초)
print(time.time())

# ctime() :  현재 시간을 문자열로 반환
print(time.ctime())
print(time.ctime(0))        # 기준시 (1970.01.01 09:00:00)

# strftime(): 원하는 포맷의 문자열로 시간 객체 변환
lt = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
print(formatted)            # 2025-11-26 12:39:14

# strptime() : 문자열을 struct_time 객체로 변환
parsed = time.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed)               # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=26, tm_hour=12, tm_min=39, tm_sec=14, tm_wday=2, tm_yday=330, tm_isdst=-1)

# 2. 시간 지연
# sleep(seconds) :  지정한 초만큼 프로그램이 일시정지
time.sleep(1)
print("time sleep")

# 시간 측정하기
start = time.time()

for i in range(5):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행시간: {end-start: .2f}초")          # 0 / 1 / 2 / 3 / 4 / 수행시간:  5.01초


# <실습6> 타자 연습 게임 만들기
import random, time

words = [ "apple", "banana", "orange", "grape", "lemon", "peach", "melon", "cherry", "plum", "pear",
    "school", "friend", "family", "flower", "garden", "window", "bottle", "pencil", "summer", "winter",
    "happy", "future", "travel", "animal", "market", "doctor", "planet", "energy", "nature", "memory" ]

n=1

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print(f"{n}번 문제")
    questions = random.choice(words)
    print(questions)
    while True: 
        user_answer = input()

        if questions == user_answer:
            print("통과!")
            n += 1
            break
        else:
            print("오타! 다시 도전!")

end = time.time()
play_time = end - start
print(f"총 소요시간: {play_time: .2f}초")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input("[타자 게임] 준비되면 엔터! ")
start = time.time()

num_questions = 10
correct_count = 0

while correct_count < num_questions:
    word = random.choice(words)
    
    while True:  
        print(f"\n문제 {correct_count + 1} \n{word} ")
        user_input = input("")
        
        if user_input == word:
            print("통과!!")
            correct_count += 1
            break
        else:
            print("오타! 다시 도전!")

end = time.time()
total_time = end - start
print(f"타자 시간: {total_time:.2f}초")



# sys 모듈
# 파이썬 인터프리터와 관련된 다양한 기능 제공

import sys

# 파이썬 버전 정보
print(sys.version)              # 3.13.9

# 운영체제 정보
print(sys.platform)             # win32

# 프로그램 종료
print("프로그램 시작")
sys.exit()                      # 강제종료
print("실행되지 않는 코드")

'''
# OS 모듈
# 운영체제와 상호작용 할 수 있도록 도와주는 기능 제공
import os

# getcwd() : 현재 작업 디렉터리 반환
print(os.getcwd())

# listdir() : 현재 폴더 내 파일, 디렉터리 목록 반환
print(os.listdir())

# 폴더 생성
folder_name =  "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} 폴더가 이미 존재합니다.")

print(os.listdir())



