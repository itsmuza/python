from array import array

numbers = array('i', [1, 2, 3, 4, 1,])  # 'i'(integer), 'f'(float), 'd'(double)
print(numbers)
print()

numbers.append(10)
numbers.insert(0, -1)
print(numbers)

numbers.remove(1)
numbers.pop()
print(numbers)

print("======= set ========")
set_numbers = set([1, 2, 4, 6, 12])  # unique elements orderless
# set_numbers = {1,2,4,6,12}

set_numbers.add(11)
print(set_numbers)


a = {10, 20, 50}
b = {20, 40}

union = a | b  # 10, 20, 50, 40
inter = a & b  # 20
difference = a - b  # 10, 50
symmetric_difference = a ^ b # 40, 10, 50
