def divide(a,b):
    try:
        return a / b
    except:
        return "You are dividing by zero. That is not possible. ASSHOLE"

print(divide(1,0)) # -> Error type: ZeroDivisionError: division by zero
print("End of program")

#---------------------------------

def divide2(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You are dividing by zero. That is not possible. ASSHOLE"

print(divide2(1,0)) # -> Error type: ZeroDivisionError: division by zero
print("End of program")
