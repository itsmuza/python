'''
 COMPREHENSION GENERAL SYNTAX
  a) *iterable
  b) <expression> for item in iterable
  c) <expression> for item in iterable <condition>
  d) ternary for item in iterable
    
'''

# LIST COMB.
numbers = [1, 2, 3, 51, 2, 21, 81]  # a version
list_numbers = [*numbers]  # copy, different reference/id
print("list_numbers:", list_numbers)

people = [('robert', 20), ('muza', 25), ('michael', 14)]
list_people = [person[0] for person in people]  # version b
print("list_people:", list_people)

adult_people = [person[0] for person in people if person[1] > 18]  # version c
print("adult_people:", adult_people)

nums = [1, 2, 3, 4]
even_odd = ['even' if n % 2 == 0 else 'odd' for n in nums]  # version d
print("even_odd:", even_odd)


# SET AND DICTIONARY COMB.
numbs = [1, 2, 3, 5, 1, 21, 2, 4, 1]
set_numbs = {*numbs}  # a version
print("set_numbs:", set_numbs)

dict_people = {key: value for key, value in people}
print("dict_people:", dict_people)
