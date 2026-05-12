'''
OBJECTS
1 - what is object
2 - iterable objects and range
3 - dictionary
4 - error handling system
'''

import array
import math
print("========= what is object =========")
# object has state and method properties
# everything is object in python

print(type("hello world"))
print(type(100))
print(type(array))
print(type(True))
print(type(math))


# Paradigm -> Functional Programming / OOP
# OOP 4 concepts -> Abstruction / Encapsulation / Enheritance / Polimorphism

result = math.ceil(3.6)
print(result)


print("======== error handling system =========")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    result = car_dict["origin"]
    print(result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("no speed found:", err)
except Exception as err:
    print("General error:", err)
else:
    print("Executed successfully without error")
finally:
    print("final closing logic")
