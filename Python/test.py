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
    print(i, end="   ")
    
'''
# 달력 출력하기

import calendar
calendar.setfirstweekday(calendar.SUNDAY)

year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))

cal = calendar.month(year, month)
print(cal)

'''