'''
딕셔너리
- 키-값 쌍으로 묶어 데이터를 저장하는 자료형
- 키는 유일해야 함. 값은 중복 가능
- 변경가능한 자료형
- 순서가 보장되지 않았다가 python 3.7 버전 이후 순서가 보장됨
'''

# dict 만들기
d1 = {}                 # 빈 dict 만들기
print(type(d1))         # <class 'dict'>

person = {"name": "홍길동", "age": 25}
print(person)               # {'name': '홍길동', 'age': 25}

# dict 함수로 생성
d2 = dict()
print(d2, type(d2))         # {} <class 'dict'>

# 키가 문자열일 때 가능
movie = dict(title = "interstela", director = "nolan")
print(movie, movie["director"])         # {'title': 'interstela', 'director': 'nolan'} nolan

# 리스트, 튜플로 만들기
pairs = [("name", "luna"), ("age","20"), ("job", "dev")]
person2 = dict(pairs)
print(person2)                          # {'name': 'luna', 'age': '20', 'job': 'dev'}

# zip 함수 활용
keys = ["title", "director", "year"]
values = ["기생충", "봉준호", "2019"]
movie2 = dict(zip(keys, values))
print(movie2)                           # {'title': '기생충', 'director': '봉준호', 'year': '2019'}

# 키로 사용할 수 없는 자료형
# 키 - 불변 자료형만 사용해야한다
d1 = {(1,2,3): (1,2,3)}                 # 튜플 사용 가능
d2 = { 1 : 10 }                         # 숫자 사용 가능
# d3 = {[1,2,3]: "리스트 값을 키로?"}    # TypeError: unhashable type: 'list'

# dict 데이터 조회
print(person2["name"])
print(person2["age"])
# print(person2["city"])                # KeyError: 'city'

# get 메서드를 활용한 조회
print(person2.get("name"))
print(person2.get("email"))             # None -> default값
print(person2.get("email", "이메일이 존재하지 않습니다"))       # 이메일이 존재하지 않습니다

# get 사용 예제
user_data = {
    "username" : "luna",
    "email" : "luna@spreatics.com",
    "password" : "1234"
}


# key = input("조회할 정보를 입력하세요(username, email, password): ")
# result = user_data.get(key, "존재하지 않는 데이터입니다.")
# print(result)

# 데이터 추가 및 수정
# 1) 기본적인 추가, 수정 방법
user_data["phone"] = "010-1234-5678"
user_data["username"] = "lunaaaa"
print(user_data)                    
# {'username': 'lunaaaa', 'email': 'luna@spreatics.com', 'password': '1234', 'phone': '010-123-4567'}

# 2) update 메서드 활용
user_data.update({"nickname" : "luna"})

# 키가 문자열인 경우
user_data.update(phone="010-2345-6789")

# 다른 딕셔너리 추가
extra_data = {"city": "seoul"}
user_data.update(extra_data)

print(user_data)                    
# {'username': 'lunaaaa', 'email': 'luna@spreatics.com', 'password': '1234', 'phone': '010-2345-6789', 'nickname': 'luna', 'city': 'seoul'}


# 데이터 삭제
del user_data["city"]
print(user_data)
# {'username': 'lunaaaa', 'email': 'luna@spreatics.com', 'password': '1234', 'phone': '010-2345-6789', 'nickname': 'luna'} 

# 키로 제거
nickname = user_data.pop("nickname")
print("pop >>", user_data, nickname, sep=" /// ")
# pop >> /// {'username': 'lunaaaa', 'email': 'luna@spreatics.com', 'password': '1234', 'phone': '010-2345-6789'} /// luna

# 가장 마지막 요소 제거
phone = user_data.popitem()
print(user_data, phone, sep=" /// ")
# {'username': 'lunaaaa', 'email': 'luna@spreatics.com', 'password': '1234'} /// ('phone', '010-2345-6789')

# dict 비우기
user_data.clear()
print(user_data)                    # {}

# dict 삭제하기
del user_data
# print(user_data)                    # 이미 삭제했기 때문에 NameError: name 'user_data' is not defined


# 실습1
user = {}
user["username"] = "skywalker"
user["email"] = "sky@example.com"
user["level"] = 5
print(user)                             # {'username': 'skywalker', 'email': 'sky@example.com', 'level': 5}

email_value = user["email"]
print(email_value)                      # sky@example.com

user["level"] = 6
print(user)                             # {'username': 'skywalker', 'email': 'sky@example.com', 'level': 6}

phone = user.get("phone", "미입력")
print(phone)                             # 미입력

user.update({"nickname": "sky"})
user.pop("email")
user.setdefault("signup_date", "2025-07-10")

print(user)                             # {'username': 'skywalker', 'level': 6, 'nickname': 'sky', 'signup_date': '2025-07-10'}


# 실습2
students = {}
students["Alice"] = 85
students["Bob"] = 90
students["Charlie"] = 95
print(students)                          # {'Alice': 85, 'Bob': 90, 'Charlie': 95}

students["David"] = 80
students["Alice"] = 88

students.pop("Bob") 

print(students)                          # {'Alice': 88, 'Charlie': 95, 'David': 80}



# 메서드
user_data = {
    "username" : "luna",
    "email" : "luna@spreatics.com",
    "password" : "1234"
}

# keys : 모든 키를 반환
print("키", user_data.keys())               # 키 dict_keys(['username', 'email', 'password'])
print("키", list(user_data.keys()))         # 키 ['username', 'email', 'password']

# values : 모든 값을 반환
print("값", list(user_data.values()))       # 값 ['luna', 'luna@spreatics.com', '1234']

# items : 모든 키 값 쌍을 반환
print("쌍", list(user_data.items()))        # 쌍 [('username', 'luna'), ('email', 'luna@spreatics.com'), ('password', '1234')]

