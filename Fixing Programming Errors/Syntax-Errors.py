# In python we have 2 types of errors:
# Syntax errors and Exceptions

# The section pretty much summs up in Finding the error in Stackoverflow, and
# using Exception for Error Handling.

# Will error.
#def divide(a,b):
#    return a/b

#print(divide(1,0))


# =====

#Will work

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("You are dividing by zero.")
    except:
        return("Division error.")

print(divide(1,0))
