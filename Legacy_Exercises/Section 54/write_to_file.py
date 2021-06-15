numbers = [1, 2, 3]

myfile = open("numbers.txt", "w")
for num in numbers:
	myfile.write(str(num) + "\n")
myfile.close()
