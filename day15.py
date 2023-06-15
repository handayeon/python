class User:
	def __init__(self, name, number, age):
		self.name = name
		self.number = number
		self.age = age

	def basicInfo(self):
		print(f"이름 : {self.name} \n번호 : {self.number} \n나이 : {self.age}")

man = User("김민석", "010-1234-5678", 28)
man.basicInfo()