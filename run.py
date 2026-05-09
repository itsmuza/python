a = 10
print("a:", a)

message = "MIT"
print(message)

print(type(message))

# Dunder __init__, __builtins__

'''  
In python, there are builtin tools:
1 - TYPES -> int float str list dict
2 - FUCNTION -> print() len() input() type() str()
3 -> CONSTANTS -> True False None
'''

print(dir(__builtins__))


# in java, variable is a name storage location
# in python, variable is named reference
print("======== number =========")
count = 100
print(f"value {count} and type {type(count)}")


result1 = count.bit_count()  # method
result2 = count.numerator

print(result1, result2)


print("======== string ========")
# MOTHOD: upper() lower() title() find() replace()

course = "AI python fullstack"
result3 = type(course)
print(result3)
print(course.title())
print(course.upper())
print(course)

result = course.replace("fullstack", "masterclass")
print(result)


print("========= boolean ==========")

# functions -> type() input() bool() int() str()
# y = input("give your value for y: ")
# print("Y:", y)
# print(y.isnumeric())

# Truthy True 100 -100 "MIT"
# Falsy False 0 "" None
test_falsy = "" or False or None or 0 or ""
print("The falsy:", bool(test_falsy))
