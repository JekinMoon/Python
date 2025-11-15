# 사용자 입력 (input)
# -input 함수 : 콘솔을 통해 사용자로부터 문자열 형태로 입력을 받음


# input 함수 사용법
# my_input = input("콘솔에 띄울 설명")
# name = input("이름을 입력하세요: ")
# print(name)

# 숫자로 활용 시 '형 변환' 필요
# a = int(input())
# b = int(input())
# print(a + b)

# c = float(input())
# d = float(input())
# print(c + d)

# 여러 자료 입력하기
# 문자열을 쪼개주는 함수 : split()
# - 기본 구분자 : 공백
# 과일1, 과일2, 과일3 = input().split()
# print(과일1, 과일2, 과일3)

# 다른 구분자 사용
# apple, banana, grape = input().split("-")
# print(apple, banana, grape)

# 실습3
# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요: "))
# print(f"안녕하세요. 저는 {name}이고, {age}살입니다.")

# 실습4-1
# 가로 = int(input("가로를 입력하세요: "))    # 가로: 20 
# 세로 = int(input("세로를 입력하세요: "))    # 세로: 10
# 넓이 = 가로*세로        
# 둘레 = 2*(가로+세로)

# print(f"넓이: {넓이}" )                    # 넓이: 200
# print(f"둘레: {둘레}")                     # 둘레: 60

#실습4-2
# num = int(input("네 자리 정수를 입력하세요: "))
# thousand = input()
# hundred = input()
# ten = input()
# one = input()

# print(f"천의 자리를 입력하세요: {thousand}")
# print(f"백의 자리를 입력하세요: {hundred}")
# print(f"십의 자리를 입력하세요: {ten}")
# print(f"일의 자리를 입력하세요: {one}")

#실습5
# 사람1, 사람2, 사람3 = input("발표자를 입력하세요: ").split()
# 주제1, 주제2, 주제3 = input("주제를 입력하세요: "). split()

# print(f'''발표 순서 안내입니다.
#      1조 발표자 : {사람1} - 주제: {주제1}
#      2조 발표자 : {사람2} - 주제: {주제2}
#      3조 발표자 : {사람3} - 주제: {주제3}''')

# 실습6
# year, month, day = input("년, 월, 일을 입력해주세요: ").split('.')
# hour, minute, second = input("시, 분, 초를 입력해주세요: ").split(':')

# print(f'''RE5의 개강일은 {year}년 {month}월 {day}일 
# 시작 시간은 {hour}시 {minute}분 {second}초 입니다.''')

