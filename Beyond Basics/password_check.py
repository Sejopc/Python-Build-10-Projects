correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while password != correct_password:
    password = input("Wrong password! Enter again: ")

# print("Hi", name, "you are logged in") -> not the right way to string format.
print("Hi %s %s, you're logged in" %(name,surname)) #correct way.
