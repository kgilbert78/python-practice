def sum_of_n3(n):
    sum = 0
    for i in range(1, n+1):
        print("i =", i)
        print("sum =", sum)
        sum = sum + i
        print("sum + i =", sum, "\n")
    return sum


print("\nwhat sum_of_n loop is doing:\n")

print(sum_of_n3(10))
