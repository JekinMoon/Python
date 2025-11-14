'''
Set (집합)
- 원소의 중복을 허용하지 않는 여러 데이터의 모음
- 순서가 없는 컬렉션 자료형
'''
# set 만들기
s1 = {1, 2, 3}
print(s1, type(s1))                             # {1, 2, 3} <class 'set'>

s2 = {1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4}
print(s2)                                       # {1, 2, 3, 4}

# 빈 set 만들기
# - 중괄호에 원소를 넣지 않고 만들면 빈 dict으로 인식된다.
s3 = {}
print(type(s3))                                 # <class 'dict'>

# set 함수로 생성
s4 = set()
print(type(s4))                                 # <class 'set'>

# set 함수의 활용 :  원소의 중복 제거
my_list = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
s5 = set(my_list)
print(s5)                                       # {1, 2, 3, 4}

# 인덱싱 X 
# s1[1]                                         # TypeError: 'set' object is not subscriptable

# 자료형 제한
# - 가변 자료형은 원소로 사용할 수 없다.
# s1 = {1,2,3,[1,2,3]}                            # TypeError: unhashable type: 'list'

# set 연산
# 집합의 연산 : 합집합, 교집합, 차집합, 대칭차집합
a = {1, 2, 3}
b = {3, 4, 5}

# 합집합 (|, .union)
s_union1 = a | b
s_union2 = a.union(b)
print(s_union1)                                     # {1, 2, 3, 4, 5}
print(s_union2)                                     # {1, 2, 3, 4, 5}

# 교집합 (&, .intersection)
s_inter1 = a & b
s_inter2 = a.intersection(b)
print(s_inter1)                                     # {3}
print(s_inter2)                                     # {3}

# 차집합 (-, .difference)
s_diff1 = a - b
s_diff2 = a.difference(b)
print(s_diff1)                                      # {1, 2}
print(s_diff2)                                      # {1, 2}
print(b-a)                                          # {4, 5}

# 대칭 차집합 (^, .symmetric_difference)
s_symm1 = a ^ b
s_symm2 = a.symmetric_difference(b)
print(s_symm1)                                      # {1, 2, 4, 5}
print(s_symm2)                                      # {1, 2, 4, 5}

# 실습 1-1
submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
new_submissions = len(set(submissions))
print("제출자 명단: ", set(submissions))                # 제출자 명단: {'kim', 'choi', 'lee', 'park'}
print("제출한 학생 수: ", new_submissions)              # 제출한 학생 수:  4


# 실습 1-2
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

inter = user1 & user2
print("공통 관심 장르: ", inter)                          # 공통 관심 장르: {'Drama', 'Action'}

symm = user1 ^ user2
print("서로 다른 장르: ", symm)                           # 서로 다른 장르: {'Romance', 'SF'}

union = user1 | user2
print("전체 장르: ", union)                               # 전체 장르: {'Drama', 'SF', 'Romance', 'Action'}

# set 메서드
s1 = {1,2,3}

# 원소 추가
s1.add(4)
print(s1)                                                 # {1, 2, 3, 4}

# 여러 원소 추가
s1.update((5,6,7))
print(s1)                                                 # {1, 2, 3, 4, 5, 6, 7}

# 원소 제거
s1.remove(4)
print(s1)                                                 # {1, 2, 3, 5, 6, 7}

# s1.remove(100)                                          # KeyError: 100 - 존재하지 않는 원소 삭제 시도시 에러

s1.discard(100)
s1.discard(6)
print(s1)                                                 # {1, 2, 3, 5, 7}

deleted = s1.pop()                                        # 임의의 값 하나 제거
print(s1, deleted)                                        # {2, 3, 5, 7} 1

# 부분 집합 (subset) 관련 메서드
a = {10, 20, 30, 40, 50}            # 상위집합
b = {20, 30, 40}                    # 부분집합
c = {10, 200, 300, 400, 500}        

# 부분집합 여부 판단
print(b.issubset(a))                # True
print(a.issubset(b))                # False

# 상위집합 여부 판단
print(a.issuperset(b))              # True
print(b.issuperset(a))              # False

# 공통 원소가 없는지 확인
print(a.isdisjoint(b))              # False
print(a.isdisjoint(c))              # False
print(b.isdisjoint(c))              # True


# 실습 1-3
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}
print("지원 자격 충족 여부: ", job_required.issubset(my_certificates))            # 지원 자격 충족 여부: True

