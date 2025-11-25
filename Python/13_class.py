'''
class(클래스)
- 데이터와 기능을 하나로 묶는 구조
- 개념적(기능적)으로 유사한 관계에 있는 것들을 묶어줌

'''
'''

# 클래스 기본 문법
# 클래스의 정의
class ClassName:
    # 생성자(constructor) :  인스턴스(객체)가 생성될 때 호출
    # 인스턴스 변수를 초기화, 기본 상태 설정
    # 하나의 클래스에서 하나만 정의 가능
    def __init__(self, name):
        # 인스턴스 변수
        # self : 인스턴스(객체) 자기 자신을 가리킴
        self.name = name 
        self.age = 0
    
    # (인스턴스) 메서드
    def method_name(self): 
         print(f"이 인스턴스의 이름은 {self.name}입니다.")      # I1

# 인스턴스 생성
my_instance = ClassName("I1")
print(my_instance.name)                     # 이 인스턴스의 이름은 I1입니다.
my_instance.method_name()

another_instance = ClassName("I2")
another_instance.method_name()              # 이 인스턴스의 이름은 I2입니다.




# <실습 1-1>
class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
        self.current_page += pages
        if self.current_page > self.total_pages:
            self.current_page = self.total_pages
            print("책을 끝까지 다 읽었어요.")

    def progress(self):
        percent = (self.current_page / self.total_pages) * 100
        return (f"현재 읽은 분량: {percent: .1f} % 입니다")
            
book1 = Book("넥서스", "유발 하라리", 500, 1)
book1.read_page(50)
print(book1.progress())              # 현재 읽은 분량: 10.2 % 입니다



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Book:
    def __init__(self, title, author, total_pages, current_page = 0):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
            self.current_page += pages
            if self.current_page > self.total_pages:
                self.current_page = self.total_pages

    def progress(self):
        percent = (self.current_page/self.total_pages) * 100
        return (f"현재 책을 읽은 분량은 {percent:.1f} % 입니다")
            
book = Book("해리포터 불의잔", "J.K.롤링", 608)

book.read_page(345)
print(book.progress())              # 현재 책을 읽은 분량은 64.1 % 입니다



# <실습1-2>
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

width = int(input("가로를 입력하세요: "))   
height = int(input("세로를 입력하세요: ")) 
    
my_rect = Rectangle(width, height)

print(f"사각형의 넓이는 {my_rect.area()} 입니다.")        # 가로를 입력하세요: 20 / 세로를 입력하세요: 50
                                                            # 사각형의 넓이는:  1000.0



# 클래스 변수
# - 클래스가 가지고 있는 변수
# - 모든 인스턴스가 공유할 수 있음

class Dog:
    # 클래스 변수
    kind = "강아지"
    
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "구름", 10)

print(dog1.kind)        # 강아지
print(dog2.kind)        # 강아지
print(Dog.kind)         # 강아지


# 클래스 메서드 
# 클래스 자체를 대상으로 동작하는 메서드
# 클래스 데이터를 조작하는데 사용

class Book2:
    book_count = 0

    def __init__(self, title, author):
        Book2.book_count += 1
        self.title = title
        self.author = author

    # 클래스 메서드
    @classmethod        # 데코레이터
    def get_count(cls):
        print(f"현재 {cls.book_count}권의 책을 가지고 있다.")


book1 = Book2("B1","author1")
book2 = Book2("B2","author2")

print(Book2.book_count)                 # 2
Book2.get_count()                       # 현재 2권의 책을 가지고 있다.



# 정적 메서드
# - 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 함수
# - 클래스나 인스턴스의 상태에 의존하지 않는 일반 함수
# - 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않음

class OperationTool:
    @staticmethod       # 데코레이터
    def add(a, b):
        return a + b
    
print(OperationTool.add(10, 20))            # 30



# <실습2>

class User:
    total_users = 0

    def __init__(self, username, points):
        User.total_users += 1
        self.username = username
        self.points = points
        
    def add_points(self, amount):
        self.points += amount
        
        
    def get_level(self):
        if self.points >= 500:
            return "Gold"
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"
    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수: {cls.total_users}" )

u1 = User("kim", 0)
print(u1.username)              # kim
u1.add_points(100)
print(u1.get_level())           # Silver
User.get_total_users()          # 총 유저 수: 1



# 접근 제어와 정보 은닉
# 데이터 무결성을 보호하기 위함
# 코드 안정성을 향상 시키기 위함

class Person2:
    def __init__(self, name, age):
        # public
        self.name = name
        # private :언더바(__) 2개를 변수 앞에 붙여서 정의
        self.__age = age

    # getter
    def get_age(self):
        return self.__age
    
    # setter
    def set_age(self, value):
        if value > 120 or value < 0:
            print("유효하지 않은 나이입니다.")
        else:
            self.__age = value


p1 = Person2("lee", 15 )
print(p1.name)

# print(p1.__age) -> X      # AttributeError
print(p1.get_age())         # 15
p1.set_age(-10)             # 유효하지 않은 나이입니다.


# @property 데코레이터
# - 메서드를 속성처럼 보이게 만들어주는 데코레이터

class Ex:
    def __init__(self):
        self.__value = 0

    # getter
    @property
    def value(self):
        return self.__value

    # setter
    @value.setter
    def value(self, val):
        if val < 0:
            print("유효하지 않은 값입니다.")
        else:
            self.__value = val

ex1 = Ex()
print(ex1.value)            # 0
ex1.value = 100
print(ex1.value)            # 100
ex1.value = -100            # 유효하지 않은 값입니다.




# <실습3-1> UserAccount클래스: 비밀번호 보호
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password = new_pw
            print("비밀번호가 변경되었습니다.")
        else:
            print("비밀번호가 일치하지 않습니다.")

    def check_password(self, password):
        return self.__password == password

user = UserAccount("admin", "codingon123")
print(user.username)                                   # admin
# print(user.__password)                               # AttributeError

user.change_password("abc123", "Dog123")               # 비밀번호가 일치하지 않습니다.
user.change_password("codingon123", "Cat123")          # 비밀번호가 변경되었습니다.

print(user.check_password("Cat123"))                   # True
print(user.check_password("Dog123"))                   # False

# <실습3-2> Student 클래스: 성적 검증(@property 사용)
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property                       # getter
    def score(self):
        return self.__score

    @score.setter                   # setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("성적은 0에서 100 사이여야 합니다.")

s1 = Student("Alice", 85)
print(s1.name)
print(s1.score)         # 85

s1.score = 105
print(s1.score)         # ValueError: 성적은 0에서 100 사이여야 햡니다.




# 상속
# 부모 클래스의 속성과 메서드를 물려받아 새로운 자녀 클래스 만드는 것

# 상속 기본 문법
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("동물이 울음소리를 냅니다.")
    
# 자녀 클래스
class Dog(Animal):
    pass

dog = Dog("구름이")
dog.bark()                  # 동물이 울음소리를 냅니다.
print(dog.name)             # 구름이



# super() 사용

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("동물이 울음소리를 냅니다.")
    
# 자녀 클래스
class Dog(Animal):
    def __init__(self, name, age):
        # super 는 부모를 가리킴
        super().__init__(name, age)


dog = Dog("구름이", 12)
dog.bark()                  # 동물이 울음소리를 냅니다.
print(dog.name)             # 구름이
print(dog.age)              # 12


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 메서드 오버라이딩

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 오버라이딩
    def bark(self):
        print("동물이 울음소리를 냅니다.")
    
# 자녀 클래스
class Dog(Animal):
    def __init__(self, name, age, species):
        # super 는 부모를 가리킴
        super().__init__(name, age)
        self.species = species
    
    def bark(self):
        super().bark()
        print("멍멍")

dog = Dog("구름이", 12, "포메라니안")
dog.bark()                              # 동물이 울음소리를 냅니다. # 멍멍  
print(dog.name)                         # 구름이
print(dog.species)                      # 포메라니안



# <실습4>
class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printinfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")
    
    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
    
    def area(self):
        area = self.base * self.height
        print(f"{self.sides}각형의 넓이: {area}")

class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        area = int((self.base * self.height / 2))
        print(f"{self.sides}각형의 넓이: {area}")
        

r = Rectangle(4, 10, 5)                               # 변의 개수: 4 / 밑변의 길이: 10 / 4각형의 넓이: 50
r.printinfo()
r.area()

print()

t = Triangle(3, 8, 6)                                 # 변의 개수: 3 / 밑변의 길이: 8 / 3각형의 넓이: 24
t.printinfo()
t.area()


# 추상 클래스 (Abstract Class)
# 클래스의 구조를 정의하는 클래스

from abc import ABC, abstractclassmethod

class Animal(ABC):
    # 추상 메서드
    @abstractclassmethod
    def bark(self):
        pass

class Dog(Animal):
    def bark(self):
        print("멍멍")

# a = Animal()              # TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'bark'
a = Dog()
a.bark()                    # 멍멍



# <실습5>
from abc import ABC, abstractclassmethod

class Payment(ABC):
    @abstractclassmethod
    def pay(self, amount):
        pass
    
class CardPayment(Payment):
    def __init__(self):
        super().__init__()
    
    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다.")

card = CardPayment()
card.pay(5000)                      # 카드로 5000원을 결제합니다.

cash = CashPayment()
cash.pay(3000)                      # 현금으로 3000원을 결제합니다.


'''









