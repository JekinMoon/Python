'''
조건문
- 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
- 조건 : 참/거짓을 구분할 수 있는 문장
'''

# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행

'''
a = int(input())
if a > 10:
    print("a는 10보다 커요")                # a는 10보다 커요
print("조건문 종료")                        # 조건문 종료

# 들여쓰기 에러 예시 
if a > 10:
    print("조건문 종료")                    # 조건문 종료

#   print("a는 10보다 커요") # IndentationError

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
if a > 100:
    pass        # 에러가 안뜸



# <실습1>
weather = input("오늘 날씨를 입력하세요(비/맑음): ")

if weather == "비":
    print("우산을 챙기세요!")               # 비 / 우산을 챙기세요!

if weather == "맑음":
    print("선크림을 바르세요!")             # 맑음 / 선크림을 바르세요!


# if - else 문
# 조건이 참일 때는 if문을, 조건이 거짓일 때는 else문을 실행
# else -> ~ 아니라면 의 의미 -> 조건이 필요X, if문과 반드시 같이 나와야 함.
a = int(input())
if a > 10:
    print("a는 10보다 커요")
else:
    print("a는 10보다 작아요")

    
#<실습2>
number = int(input("정수를 입력해 주세요: "))
if number % 2 == 0:
    print("짝수입니다.")                # 10 / 짝수입니다.
else:
    print("홀수입니다.")                # 15 / 홀수입니다.


# if - elif - else 구문
# elif : else if 의 약자
# elif 에서 조건을 반드시 적어야한다
# if 가 있어야만 elif 사용 가능하다

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

     
# <실습3>
age = int(input("나이를 입력해주세요: "))

if 0 <= age <= 12 :
    print("전체관람가")
elif 13 <= age <= 15 :
    print("12세 이상 관람가")
elif 16 <= age <= 18 :
    print("15세 이상 관람가")
else:
    print("청소년 관람 불가 가능")



age = int(input("나이를 입력해주세요: "))

if age >= 19 :
    print("청소년 관람 불가 가능")
elif age >=16:
    print("15세 이상 관람가")
elif age >=13:
    print("12세 이상 관람가")
else:
    print("전체 관람가")



#<실습4>
A = int(input("초를 입력해주세요: "))

hour = A // 3600
minute = ( A %  3600 ) // 60
second = A % 60

if hour > 0:
    print(f"{hour}시간 {minute}분 {second}초")
elif minute > 0:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")        # 20 / 20초 ,  90 / 1분 30초 , 4567 / 1시간 16분 7초



hour, minute, second = 0,0,0
input_second = int(input("초를 입력해주세요: "))

# 60s = 1m, 60m = 1h

minute = input_second // 60
second = input_second % 60
hour = minute // 60

minute %= 60
if hour > 0:
     print(f"{hour}시간 {minute}분 {second}초")
elif minute > 0:
     print(f"{minute}분 {second}초")
else:
     print(f"{second}초")



# 중첩 조건문
# 하나의 if문 안에 또다른 if문을 사용하는 것

username = input("관리자 아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if username == "admin":
    if password == "abcd":
        print("로그인 성공")
    else:
        print("비밀번호가 잘못됐습니다")
else:
    print("잘못된 사용자입니다.")



# <실습5>

coin = int(input("금액을 입력해주세요: "))
food = (input("음식을 입력해주세요(김밥/삼각김밥/도시락): "))

if food == "김밥":
    price = 2500
    if coin >= price:
        print(f"{food} 구매 성공!")
    else:
         print("금액이 부족합니다.")
elif food == "삼각김밥":
    price = 1500
    if coin >= price:
        print(f"{food} 구매 성공!")
    else:
         print("금액이 부족합니다.")    
elif food == "도시락":
    price = 4000
    if coin >= price:
        print(f"{food} 구매 성공!")
    else:
         print("금액이 부족합니다.")
else:
    print("유효하지 않은 음식명입니다.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1)
money = int(input("금액을 입력해주세요: "))
food = (input("음식을 입력해주세요(김밥/삼각김밥/도시락): "))

KIMBAB = "김밥"                 # 상수(대문자)
SAMKIM = "삼각김밥"
DOSIRAK = "도시락"

k_price, s_price, d_price = 2500, 1500, 4000

if food == KIMBAB:
    if money >= k_price:
        print(f"{KIMBAB}을 구입했습니다")
    else:
        print("금액이 부족해요")
elif food == SAMKIM:
    if money >= s_price:
         print(f"{SAMKIM}을 구입했습니다")
    else:
        print("금액이 부족해요")
elif food == DOSIRAK:
    if money >= s_price:
         print(f"{DOSIRAK}을 구입했습니다")
    else:
        print("금액이 부족해요")
else:
    print("입력이 잘못됐습니다")


# 2) 딕셔너리 사용
money = int(input("금액을 입력해주세요: "))
food = (input("음식을 입력해주세요(김밥/삼각김밥/도시락): "))

prices = {
    "김밥": 2500,
    "삼각김밥": 1500,
    "도시락": 4000
}

if food in prices:
    if money >= prices[food]:
        print(f"{food}을 구입했습니다.")
    else:
        print(f"금액이 부족해요")
else:
    print("입력이 잘못됐습니다.")






'''




