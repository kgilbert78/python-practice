# Recursively find the maximum element of a list

def maxto(lst):
#PRE: The list is NOT empty
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0],maxto(lst[1:]))


def main():
    print()
    print("Let's find the maximum element of a list of numbers")
    print()
                   
    print("enter a non-empty list in python format, e.g.,  [23, 45, 32, 99, 10, 4]")
    print()
    myList = eval(input(""))

    print()
    print("The maximum element is ",maxto(myList))
    print()

main()
