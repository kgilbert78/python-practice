fruits = ["apple", "banana", "cherry"]
for eachFruit in fruits:
    # eachFruit represents the ITEM AT the index
    print(eachFruit)

# RESULT:
# apple
# banana
# cherry

# ... more like JS fruits.map((eachFruit) => { console.log(eachFruit) } than js loop)

for eachFruit in range(len(fruits)):
    # eachFruit represents the INDEX NUMBER, like JS for loop.
    print(eachFruit, fruits[eachFruit])

    # https://www.programiz.com/python-programming/methods/built-in/enumerate
for count, item in enumerate(fruits):
    print(count, item)

# RESULT (BOTH):
# 0 apple
# 1 banana
# 2 cherry


# DEMO OF MAP FUNCTION

def addition(n):
    doubled = n + n
    return str(doubled)

numbers = (1, 2, 3, 4)

result = map(addition, numbers)

result_concatenated = " ".join(result)
print(result_concatenated)
