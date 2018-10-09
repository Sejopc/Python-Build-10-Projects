file = open("fruits.txt")
fruits = file.read()
file.close()
fruits = fruits.splitlines()

for f in fruits:
	print(len(f))

