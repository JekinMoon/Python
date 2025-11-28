# 예외처리
# - 에러: 프로그램이 실행이 되지 않게 하는 문제
# - 예외: 에러가 발생될 것 같은 부분을 예외로 처리
# -> 프로그램이 예기치 않게 종료되는 것을 방지

# 예외 처리 기본 문법
try:
    # 예외가 발생할 수 있는 코드
    pass
except:
    # 예외가 발생했을 때 실행할 코드
    # 특정 에러를 지정 가능
    pass

# 예외 종류
# 1. IndexError
# - 리스트 인덱스 범위 오류
shop = ['반팔', '청바지', '이어폰', '키보드']
print(shop[2])
# print(shop[10])               # IndexError: list index out of range
print("예외 처리")

# 2. ValueError
# - 부적절한 값을 가진 인자를 받았을 때 발생
# number = int("hello")         # ValueError: invalid literal for int() with base 10: 'hello'
# print(shop.index("x"))        # ValueError: 'x' is not in list

# 3. ZeroDivisionError
# - 0으로 나눌 때 발생
# print(5/0)                    # ZeroDivisionError: division by zero

# 4. NameError
# - 존재하지 않는 변수를 호출할 때
# print(x)                      # NameError: name 'x' is not defined

# 5. FileNotFoundError
# - 존재하지 않는 파일을 호출할 때
# file = open('text.txt')       # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'


# 예외 처리
# 1)  단일 except
# try:
#     num = int(input("숫자를 입력하세요: "))
#     print(10 / num)
# except:
#     print("예외 발생")              # ValueError

# 2) 특정 예외 처리
# try:
#     num = int(input("숫자를 입력하세요: "))
#     print(10 / num)
# except ValueError as e:
#     print("숫자가 아닙니다", e)              # 숫자가 아닙니다 invalid literal for int() with base 10: 'ok'
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다", e)       # 0으로 나눌 수 없습니다 division by zero


# 예외 처리 구조
# try:
#     # 예외가 발생할 수 있는 코드
#     pass
# except 오류내용1:
#     # 예외가 발생했을 때 실행할 코드
#     # 특정 에러를 지정 가능
#     pass
# except 오류내용2:
#     # 특정 에러2
# else:
#     # 예외 없는 경우에 실행
# finally:
#     # 예외 발생 여부와 상관없이 실행



'''

# <실습1>
# 조건1 사용자에게 숫자를 입력받고 try 안에서 int()함수를 사용해 숫자로 변환해 num변수에 저장
# 조건2 입력받은 값이 숫자가 아니라면 에러 발생
# 조건3 예외상황 발생시 변수num은 -1로 저장
# 조건4 if, else 문 사용해서 num이 0보다 크면 "0보다 큽니다"를, 아니라면 " 숫자가 아닙니다"를 출력
try:
    user_num = int(input("숫자를 입력하세요: "))
   
except ValueError:
    user_num = -1

if user_num > 0:
    print("0보다 큽니다.")
else:
    print("숫자가 아닙니다.")


# <실습2>
# 사칙연산 계산기 프로그램 만들기
# 숫자 2개, 연산자 1개를 받을 변수를 만들기
# 연산자는 +-*/로 입력받기 
# (숫자가 아닌 문자, 연산자가 아닌 문자를 입력받았을 때 예외를 발생시킨다)
# 반복문을 사용하여 사용자가 올바른 값을 입력할 때까지 반복해준다
# 조건문을 사용하여 연산자에 따라 연산을 진행한다
# 결과값은 함수를 사용하여 (숫자1, 연산자, 숫자2, "=", 결과값) 양식으로 출력

def print_result(num1, op, num2, result):
    print(f"{num1} {op} {num2} = {result}")

while True:
    try:
        num1 = float(input("1번째 숫자: "))
        op = input("연산자(+ , - , * , / ): ")
        num2 = float(input("2번째 숫자: "))
    
        if op not in ["+", "-", "*", "/"]:
            raise ValueError("잘못된 연산자입니다.")
    
        if op == '/' and num2 == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    
        if op == '+':
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        else:
            result = num1/num2

        print_result(num1, op, num2, result)
        break
    except ValueError:
        print("입력값이 잘못되었습니다. 다시 입력하세요\n")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다. 다시 입력하세요\n")
    except Exception:
        print("알 수 없는 오류가 발생했습니다. \n")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

while True:
    try:
        a = int(input("1번째 숫자를 입력하세요: "))
        b = int(input("2번째 숫자를 입력하세요: "))
    except ValueError:
        print("숫자를 다시 입력하세요!\n")
        continue

    operator = input("연산자를 입력하세요(+ , - , * , / ): ")

    if operator not in ["+", "-", "*", "/"]:
        print("연산자를 다시 입력하세요!\n")
        continue

    result = calculate(a, b, operator)
    print(f"{a} {operator} {b} = {result}")
    break

'''
