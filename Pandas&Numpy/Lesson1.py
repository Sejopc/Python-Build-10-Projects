import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])
print(df1)

print("------------------------- [1]")

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ["Price", "Age","Value"])
print(df1)

print("------------------------- [2]")

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ["Price", "Age","Value"], index = ["First", "Second"])
#Index is for the Rows.
print(df1)

print("------------------------- [3]")

df2 = pandas.DataFrame([{"Name" : "Jack"}, {"Name":"John"}])
print(df2)

print("------------------------- [4]")

df2 = pandas.DataFrame([{"Name" : "Jack", "Surname" : "Johns"}, {"Name":"John"}])
print(df2)

print("------------------------- [5]")

print(df1)
print(type(df1))
#dir(df1) to see all the methods available for this class.

print("------------------------- [6]")

print(df1.mean()) #To get the Mean of all columns

print(df1.mean().mean()) #To get the mean of the mean of all columns

print(type(df1.mean()))

print("------------------------- [7]")

print(df1.Price)
print(df1.Price.mean())
print(df1.Price.max())
