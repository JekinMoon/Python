'''
# print("Hello World")


# 65세까지 몇년 남았을까?

user = input ("성명 입력 >> ")
age = int(input("나이 입력 >> "))
futureAge = 65-age
print("{:-^30}".format("입력 정보 확인"))
print("{}님은 65세까지 {}년 남았습니다.".format(user, futureAge))

'''

# <로또번호 만들기>
import random

lotto = set()

while len(lotto) < 6:
    lotto.add(random.randint(1,45))

print("===로또번호 생성===")
for i in lotto:
    print(i, end="  ")

'''   

# 달력 출력하기

import calendar
calendar.setfirstweekday(calendar.SUNDAY)

year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))

cal = calendar.month(year, month)
print(cal)



print("=== 간단한 계산기 ===")

# 사용자로부터 두 숫자 입력받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 계산 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")


'''

# D-day 계산기
from datetime import datetime
target = input("\n D-Day 목표 날짜를 입력하세요 (YYYY-MM-DD): ")
target_date = datetime.strptime(target, "%Y-%m-%d").date()
today = datetime.today().date()
delta = (target_date - today).days

if delta > 0:
    print(f"D-{delta}")
elif delta == 0:
    print("D-Day!")
else:
    print(f"D+{-delta}")





