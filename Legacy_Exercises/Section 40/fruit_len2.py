file = open("fruits.txt")
content = file.readlines()

content = [line.strip() for line in content]
file.close()

for i in content:
	print(len(i))
