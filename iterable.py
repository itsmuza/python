print("======== iterable objects / range ==========")
# iterable objects -> string dict tuple list range map filter

range_obj = range(3)
print("range:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")

print("======== dictionary =========")
# dictionary is JSON object
person = {"name": "justin", "age": 25, "single": True}
person_obj = dict(name="justin", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)

# method: get()
# name - person_obj["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")  # -> None
balance = person_obj.get("balance", 0)  # -> 0

print(f"name: {name}, hobby: {hobby}, balance: {balance}")

del person_obj["single"]
for key, value in person_obj.items():
    print(f"the key: {key}, value {value}")
