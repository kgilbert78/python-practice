import time


def sum_of_n(n):
    start = time.time()

    sum = 0
    for i in range(1, n+1):
        sum = sum + i

    end = time.time()

    return sum, end-start


print("\nsum_of_n loop:\n")

for i in range(5):
    print("Sum is %d, required %10.7f seconds to calculate" % sum_of_n(100000))

print("\nsum_of_n with 5 values:\n")

print("Sum is %d, required %10.7f seconds to calculate" % sum_of_n(10000))
print("Sum is %d, required %10.7f seconds to calculate" % sum_of_n(100000))
print("Sum is %d, required %10.7f seconds to calculate" % sum_of_n(1000000))
print("Sum is %d, required %10.7f seconds to calculate" % sum_of_n(10000000))
print("Sum is %d, required %10.7f seconds to calculate" % sum_of_n(100000000))


print("\nrevised_sum_of_n with 5 values:\n")

# def sum2_of_n(n):
#     return ((n*(n+1))/2)


def sum2_of_n(n):
    start = time.time()
    result = (n*(n+1))/2
    end = time.time()
    return result, end-start


# print(sum2_of_n(10000))
# print(sum2_of_n(10000))
# print(sum2_of_n(1000000))
# print(sum2_of_n(10000000))
# print(sum2_of_n(100000000))


print("Sum is %d, required %10.7f seconds to calculate" % sum2_of_n(10000))
print("Sum is %d, required %10.7f seconds to calculate" % sum2_of_n(100000))
print("Sum is %d, required %10.7f seconds to calculate" % sum2_of_n(1000000))
print("Sum is %d, required %10.7f seconds to calculate" % sum2_of_n(10000000))
print("Sum is %d, required %10.7f seconds to calculate" % sum2_of_n(100000000))
