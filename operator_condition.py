'''
OPERATOR AND CONDITION
    1 - operator
    2 - condition
    3 - logical operators
'''

print("======= operators =========")

a = 19
b = 5

print("a / b:", a/b)
print("a > b:", a > b)
print("a // b:", a//b)

print("a ** 2 ", a**2)


c = dict(name="muza", age=25)
d = dict(name="muza", age=25)
print("c == d:", c == d)  # checks value
print("c is d:", c is d)  # chechs reference
e = d  # e gets d's reference
print("e is d:", e is d)

e["name"] = "michael"
print(d["name"])
