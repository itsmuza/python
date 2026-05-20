
# task - K

def countVowels(data):
    count = 0
    for c in data:
        if c in "euioaEUIOA":
            count += 1
    return count


print(countVowels("string value"))
