# for
for i in [1, 2, 3]: # 차례대로 출력
	print(i)

for i in "가나다라": #차례대로 출력
	print(i)

for i in {"a":1, "b":2}: # key값 출력
	print(i)

# renge : 0부터 정한 숫자 앞까지(python에서는 index 앞까지 출력)
for i in range(10):
	print(i)

# range(시작, 종료, 스텝)
for i in range(1, 10, 2): # 1부터 9까지 2개씩
	print(i)

# 1부터 10까지 배열에 넣기
empty = []

for i in range(1, 11):
	empty.append(i)

print(empty)