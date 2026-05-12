'''
    CLASS deep dive
        1 - encapsulation
        2 - inheritance 
        3 - polimorphism
'''

# encapsulation -> name (public), __name (private), _name (protected)


class Account:
    description = "this class makes bank accounts"

    def __init__(self, _owner, _amount):
        self.__owner = _owner
        self.__amount = _amount

    def get_name(self):
        print(f"{self.__owner}")

    def get_balance(self):
        print(f"{self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("* deposit *")
        self.__amount += amount

    def withdraw(self, amount):
        print("* withdraw *")
        self.__amount -= amount

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        self.__owner = new_owner

    def change_owner(self, new_owner):
        self.__owner = new_owner


my_account = Account("muza", 1000)
my_account.get_balance()
my_account.deposit(2500)
my_account.withdraw(2000)
my_account.get_balance()

print(my_account.owner)
my_account.change_owner("Michael")
my_account.get_name()

my_account.owner = "John"
my_account.get_name()
