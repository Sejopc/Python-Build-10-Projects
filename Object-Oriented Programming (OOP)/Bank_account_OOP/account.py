class Account: # Class

    def __init__(self, filepath): # Constructor
        self.filepath = filepath # Instance variables (variables defined inside methods.). Used ONLY by the same instance of the class. Also a Data member. Also referred as attributes.
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount): # Object Method Instance
        self.balance -= amount
        
    def deposit(self, amount): 
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file: # We want to override the file balance amount.
            file.write(str(self.balance))

class Checking(Account): # Inheritance
    """ 
    # DOCSTRING
    This class generates a checking account object. DOCSTRING provides information about a class.
    """


    type = "checking" # Class variable (declared outside of the methods of the class). Shared by ALL instances of the class. Also a Data member. Also referred as attributes.

    def __init__(self, filepath, fee): # Constructor
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount): # Object Method Instance
        self.balance = self.balance - amount - self.fee


'''
account = Account("/Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Object-Oriented Programming (OOP)/Bank_account_OOP/balance.txt")
print(account) # This will print <PackageNname.module.class> when imported as "from Bank_account_OOP import account"
# i.e:
# >>> from Bank_account_OOP import account
# <Bank_account_OOP.account.Account object at 0x7ff76bada710>
# Where,
# Bank_account_OOP is that PackageName
# account is module (which is account.py script)
# Account is the Class of the module

print(account.balance)
account.deposit(300)
print(account.balance)
account.commit()
'''

checking = Checking("/Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Object-Oriented Programming (OOP)/Bank_account_OOP/balance.txt", 10) # Object Instance (aka Instantiation)
checking.transfer(10)
print(checking.balance)
checking.commit()
print(checking.__doc__) # prints the DOCSTRING for the Class.