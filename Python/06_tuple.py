'''
튜플
- 순서가 존재하는 여러 데이터의 모음
- 불변 (immutable) 자료형
'''

# 튜플 생성
my_tuple = (1, 2, 3, 4)
print(my_tuple)                     # (1, 2, 3, 4)
print(type(my_tuple))               # <class 'tuple'>

my_tuple2 = 5, 6, 7, 8
print(my_tuple2)                    # (5, 6, 7, 8)
print(type(my_tuple2))              # <class 'tuple'>

# 원소가 하나인 튜플 생성
single_el_tuple = (100,)
print(single_el_tuple)              # (100,)
print(type(single_el_tuple))        # <class 'tuple'>

# 튜플 생성 함수로 생성
my_tuple2 = tuple()
print(my_tuple2)                    # ()

my_tuple3 = tuple("codingon")
print(my_tuple3)                    # ('c', 'o', 'd', 'i', 'n', 'g', 'o', 'n')

# 언패킹
# 시퀀스에 저장된 여러 값을 여러 변수에 나눠 저장하는 것
# 튜플, 리스트, 문자열...
apple, banana, kiwi = ("apple", "banana", "kiwi")
print(apple, banana, kiwi)          # apple banana kiwi


# 불변성 (immutable)
# - 객체가 생성된 이후 내부 데이터를 변경할 수 없는 것
# my_tuple[0] = 100                 # TypeError

# 삭제
# del my_tuple[1]                   # TypeError

# 튜플 자체는 삭제 가능, but 원소 삭제는 불가
# del my_tuple
# print(my_tuple)                    # NameError

# 튜플 수정
my_tuple4 = (10, 20, 30)
new_tuple = (100,) + my_tuple4[1:]
print(my_tuple4)                        # (10, 20, 30)
print(new_tuple)                        # (100, 20, 30)

# 실습1

user = ("minji", 25, "Seoul")
resorted_user = ("eunji",) + user[1:]
print(resorted_user)                    # ('eunji', 25, 'Seoul')

name, age, city = resorted_user
print(name, age, city)                  # eunji 25 Seoul

users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji"))             # 3
print(users.index("soojin"))            # 2

sorted_users = sorted(users)
print(sorted_users)                     # ['eunji', 'minji', 'minji', 'minji', 'soojin']

