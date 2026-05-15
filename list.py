fruits = ['apple', 'banana', 'kiwi', 'cherry']

new_fruits = fruits[0:2]
print(new_fruits)
print(fruits[::2])
print(fruits[::-1])


print("list methods")
# append(), insert(), pop(), remove(), clear(), sort(), index()

numbers = [2, 3, 4]

numbers.append(5)
print(numbers)
numbers.insert(0, 1)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(3)
print(numbers)
del numbers[0:2]
print(numbers)
print(numbers.index(4))
numbers.clear()
print(numbers)


nums = [4, 2, 1, 5, 3]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


numbs = [5, 2, 12, 61]
new_numbs = sorted(numbs)
print(numbs)
print(new_numbs)
