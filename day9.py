# or
print((1 == 1) or (1 == 3)) # True

# and
print((1 == 1) or (1 == 3)) # False

# not
print(not(True)) # False

# 단일 조건
a = 1
if a == 1:
	print("a는 1이다.")

existID = "a123"
existPassword = "qwer1234"

newID = "a123"
newPassword = "qwer0987"

if (existID == newID) and (existPassword == newPassword):
	print("로그인 성공")

# 다중 조건
if (existID == newID) and (existPassword == newPassword):
	print("로그인 성공")
elif (existID == newID) and (existPassword != newPassword):
	print("비밀번호를 잘못 입력했습니다.")
else:
	print("존재하지않는 ID입니다.")