'''
    LOOP 
        1 - for
        2 - break/else
        3 - while
'''

text = "MIT"

for letter in text:
    print(letter)

nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n)

car_obj = dict(name="tesla", year=2024, model='Y')
for key in car_obj:
    print(key, car_obj[key])

for key, value in car_obj.items():
    print(key, value)

range_obj = range(5)
for n in range_obj:
    print(n)

for x in range(1, 20, 2):
    if x > 10:
        break
        print(x)
else:
    print("reached else")

print()
num = 20
while num > 5:
    print(num)
    num -= 2

print()
count = 0
while True:
    count += 1
    x = int(input("Enter a number: "))
    if x == 41:
        print("You found the number in", count, "step")
        break
    else:
        print("Try again")
