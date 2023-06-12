a = 1
print(a)

# 선언
num = 2
num2 = 3

# 연산
print(num + num2) #더하기
print(num - num2) # 빼기
print(num * num2) # 곱하기
print(num / num2) # 나누기
print(num // num2) # 몫
print(num % num2) # 나머지

#정수 int, 실수 float
print(type(3)) # int
print(type(3.3)) # float

# 선언
str = "안녕하세요"
str2 = '안녕'

# 문자 인덱싱, 슬라이싱
print(str[0]) # 인덱싱
print(str[0:2]) # 슬라이싱

# 선언
# True
# False

# 비교연산 ==, !=, > <=
print(1 == 1) # True
print(1 != 1) # False
print(3 < 1) # False
print(3 <= 4) # True

# CRUD(생성,조회,수정,삭제)
# create
arr = ["a", "b", "c", 1, 3]
print(arr)

# read
print(arr[0])
print(arr[0:3])

#update
arr[0] = "A"
print(arr)

# delete
del arr[0]
print(arr)

#CRUD
#create
userList = {"김철수" : 123, "박민수" : 345}

#read
print(userList["김철수"])

#update
userList["김철수"] = "123a"
print(userList)

#delete
del userList['김철수']
print(userList)