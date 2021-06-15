# 2 types of errors in Python: Syntax errors, and Exceptions.

#Syntax errors
print(1)
int(9)
int(999)
print(2)
#print 3 # -> this will only give error on python 3. Just put () around the parameters, and done.

# Exceptions
a = 1
b = "2"
print(int(2.5))
#print(a + b) # Error, unsuported type for +: 'int' + 'str'
print(a + float(b))
print(str(a) + b)

c = 3 # if I delete this line, line 19 will print 'c' is not defined (NameError).
print(c)
