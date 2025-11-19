'''
while문
- 조건이 True인 동안 코드를 반복하는 반복문
- 조건이 False가 되면 반복을 멈춤
- 반복횟수가 정해지지 않았을 때 사용
'''
'''
# while문 기본 문법
# 조건 : 참/거짓을 구분할 수 있는 문장
# while 조건:
    # 반복할 코드

# 무한루프
# 사용시 주의. 반드시 종료 조건 있어야 함
# while True:
#    print("반복중")
'''
'''
# 예제1
light = "green"

while light == "green":
   print("계속 가세요!")
   light = input("신호등의 신호를 입력하세요(green/yellow/red): ")

print("중지!!")         # green -> 계속 가세요! / yellow,  red -> 중지!!


# 예제2. 별도의 반복 변수를 정의
i = 0

while i < 5:
    print(i, "반복")
    i += 1
print("반복 종료")              #  반복 / 1 반복 / 2 반복 / 3 반복 / 4 반복 / 반복 종료


# <실습1-1>
secret_code = "codingonre3"
while True:
    user_code = input("비밀코드를 입력하세요: ")
    if user_code != secret_code:
        print("비밀코드가 틀렸습니다. 다시 시도하세요.")
    else:
        print("입장완료! 환영합니다")
        break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
secret_code = "codingonre3"
user_input = ""
while user_input != secret_code:
    user_input = input("비밀코드를 입력하세요: ")

print("입장이 허용되었습니다!")



# <실습1-2>
import random
secret_number = random.randint(1, 100)
guess_count = 0
is_guessed = False
user_guess = 0
print("--- 1부터 100 사이 무작위 수를 생성 중입니다. ---")
while not is_guessed:
    try:
        user_guess = int(input("숫자를 입력하세요: "))
        guess_count += 1
        if user_guess == secret_number:
            is_guessed = True
        elif user_guess > secret_number:
            print(f"{user_guess}보다는 작아요.")
        else:
            print(f"{user_guess}보다는 커요.")
    except ValueError:
        print("유효한 숫자를 입력해 주세요.")
print(f"{guess_count}번 만에 정답을 맞혔습니다.")


# 1)
import random
random_number = random.randint(1, 100)
attempts = 0

while True:
    user_guess = int(input("숫자를 입력하세요: "))
    attempts += 1

    if user_guess < random_number:
        print("업")
    elif user_guess > random_number:
        print("다운")
    else:
        print("정답!")
        print("시도한 횟수: ", attempts)
        break

# 2)        
answer = 99         # import random  / answer = random.randint(1,100) 
num = 0     # 사용자 입력 받을 변수
time = 0    # 실행 횟수를 저장할 수 있는 변수

while num != answer:
    num = int(input("1~100 사이의 수를 입력해주세요: "))
    time += 1

    if num > answer:
        print(f"정답이 {num}보다 작아요")
    elif num < answer:
        print(f"정답이 {num}보다 커요")
    
print(f"{time}번 만에 정답을 맞췄습니다")



# 루프 제어문
running = True
while running:
    if 조건1:
        running = False

    if 조건2:
        running = False


# break문
while True:
    if 조건:
        break



# 예제1
i = 0

while True:
    print(i, "실행")
    my_select = input("메뉴를 골라주세요: ")

    if my_select == "종료":
        break
    
    i += 1

print("반복문 종료")




# continue
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print("반복종료")       # 1 / 3 / 5 / 반복종료


# <실습2-1>
secret_code = "codingonre3"
user_code = ""

while True:
    user_code = input("비밀코드를 입력하세요: ")
    if user_code == secret_code:
        print("입장완료! 환영합니다")
        break
    else:
        print("비밀코드가 틀렸습니다. 다시 시도하세요.")
        


# <실습2-2>

times = 0
sum_age = 0

while times < 5:
    age = int(input("나이를 입력하세요: "))
    if age <= 0 or age > 120:
        continue
    sum_age += age
    times += 1
# average = sum_age // 5
# print(f"총 나이 합계는 {sum_age}, 평균은 {average)}입니다. ")

print(f"총 나이 합계는 {sum_age}, 평균은 {int(sum_age / times)}입니다. ")


# 중첩 while 문

# 예제
dan = 2
while dan <= 9:
    num = 1
    print(f"[{dan}단 ]")

    while num <= 9:
        num += 1
        if num % 2 != 0:
            continue
        else:
            print(f"{dan} x {num} = {dan * num}")

    print()
    dan += 1                                        
                   # [2단 ] 2 x 2 = 4 / 2 x 4 = 8 / 2 x 6 = 12 / 2 x 8 = 16 / 2 x 10 = 20
                   # [3단 ] 3 x 2 = 6 / 3 x 4 = 12 / 3 x 6 = 18 / 3 x 8 = 24 / 3 x 10 = 30
                   # [4단 ] 4 x 2 = 8 / 4 x 4 = 16 / 4 x 6 = 24 / 4 x 8 = 32 / 4 x 10 = 40
                   # [5단 ] 5 x 2 = 10 / 5 x 4 = 20 / 5 x 6 = 30 / 5 x 8 = 40 / 5 x 10 = 50
                   # [6단 ] 6 x 2 = 12 / 6 x 4 = 24 / 6 x 6 = 36 / 6 x 8 = 48 / 6 x 10 = 60
                   # [7단 ] 7 x 2 = 14 / 7 x 4 = 28 / 7 x 6 = 42 / 7 x 8 = 56 / 7 x 10 = 70
                   # [8단 ] 8 x 2 = 16 / 8 x 4 = 32 / 8 x 6 = 48 / 8 x 8 = 64 / 8 x 10 = 80
                   # [9단 ] 9 x 2 = 18 / 9 x 4 = 36 / 9 x 6 = 54 / 9 x 8 = 72 / 9 x 10 = 90

'''

# <실습3>

ID = "codingonre5"
PW = "codingon"


while True:
    user_id = input("ID를 입력하세요: ")
    if user_id != ID:
        print("ID가 존재하지 않습니다.")
    else:
        break
while True:
    user_pw = input("비밀번호를 입력하세요: ")
    if user_pw != PW:
        print("비밀번호가 틀렸습니다.")
    else:
        print("로그인 성공!")
        break


# <실습 3 추가>

ID = "codingon"
PW = "abc123"

while True:
        print("=== 로그인 화면 ===")
        print("1. 로그인")
        print("2. 종료")
        select = input("선택: ")
        
        if select == "2":
            print("종료합니다.")
            break

        if select == "1":
            id_input = input("ID: ")
            pw_input = input("PW: ")

            if id_input != ID and pw_input != PW:
                   print("로그인 실패! 다시 시도해주세요.")
                   continue
            else:
                print("로그인 성공!")
        while True:
            print("===== 메뉴 =====")
            print("1. 정보 보기")
            print("2. 설정")
            print("3. 로그아웃")
            print("================")
            menu = input("메뉴 선택 : ")

            if menu == "1":
                print("회원 정보입니다.")
                continue
            elif menu == "2":
                print("설정 화면입니다.")
                continue

            elif menu == "3":
                print("로그아웃합니다.")
                break
            else:
                print("잘못된 입력입니다.")
                continue



