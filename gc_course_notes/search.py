# linear search for use in unsorted list
def is_in(my_list, value_to_find):
    i = 0
    while (i<len(my_list)):
        if my_list[i] == value_to_find:
            return True
        else:
            i+=1
    return False

# binary search more efficient for sorted list
def binary_in(my_list, value_to_find):
    if len(my_list) < 1:
        return False
    low = 0
    high = len(my_list)-1
    if my_list[low] == value_to_find or my_list[high] == value_to_find:
        return True
    while low < (high-1):
        midpoint = low + (high-low) // 2 #integer division (drops remainder)
        if my_list[midpoint] == value_to_find:
            return True
        elif my_list[midpoint] < value_to_find:
            low = midpoint
        else:
            high = midpoint
    return False

# search that returns location of value found (or invalid index)
def binaryRtnIndexIn(my_list, value_to_find):
    if len(my_list) < 1:
        return False
    low = 0
    high = len(my_list)-1
    if my_list[low] == value_to_find:
        return low
    elif my_list[high] == value_to_find:
        return high
    while low < (high-1):
        midpoint = low + (high-low) // 2 #integer division (drops remainder)
        if my_list[midpoint] == value_to_find:
            return midpoint
        elif my_list[midpoint] < value_to_find:
            low = midpoint
        else:
            high = midpoint
    return -1

favorite_foods = ['barbeque', 'chicken and dumplings', 'gumbo', 'ice cream', 'pecan pie', 'pizza']
print(binary_in(favorite_foods, 'gumbo'))
print(binary_in(favorite_foods, 'coconut'))