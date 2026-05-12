'''
CLASS
1 - what is class
2 - ordinary vs static properties
3 - special methods
'''

print("========= what is class =========")
# class - blueprint for object creation
# structure - state constructor method


class Person:
    # state
    message = "class state property"
    # constructor

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
    # method

    def introduce(self):
        print(f"{self.name} says: hello")

    def say_age(self):
        print(f"{self.age} years old")

    @classmethod
    def help(cls):
        print("this is person class")


person1 = Person("muza", 25)
person2 = Person("Michael", 15)
person3 = Person("Jhon", 22)

# ordinary state
name = person1.name
print(name)

# ordinary method
person1.say_age()
person2.introduce()

print(Person.message)

Person.help()


print("===== special/magic methods")
# python's most common special methods are below:
# __init__ / __new__ / __str__ / __call__ / __getitem__


class Car:
    # state
    description = "this class makes cars"

    # constructor
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, _name, _year):
        self.name = _name
        self.year = _year

    # method
    def start_engine(self):
        print(f"{self.name} started engine")

    def stop_engine(self):
        print(f"{self.name} stopped engine")

    def __str__(self):
        return f"car.name: {self.name} was produced in {self.year} year"

    def __call__(self):
        print("Object called as function")
        return True


my_car = Car("Tesla", 2025)
my_car.start_engine()
my_car.stop_engine()
print(my_car)
response = my_car()
print(response)
