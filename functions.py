'''
functions
1 - define vs call
2 - parametr vs arguemtn
3 - keyword and default arguments
4 - scope
'''

print("===== define vs call =======")


# builtin function -> print() type()
# function -> reusable block of code
# instead of block {} in java, python uses indentation

# DEFINE - parameter
def greet(a):
    # pass
    print("MIT", a)


def greeting(b):
    print("greeting is executed")
    return f"HI {b}"


# CALL - argument
greet(41)
result = greeting("WORLD")
print(result)


print("===== keyword and default arguments")


# define
def give_greet(name="Michael", age=20):
    print("function executed")
    return f"Hi {name}, you are {age} years old"


# call
print(give_greet("muza", 25))

b = 5


def calculate(a, b):
    print(a*b)


calculate(2, 3)
