# get information from user
balance = float(input("Enter how much you want to save: "))
if (balance <= 0 ):
    print("Looks like you've already saved enough!")
    balance = 0
    payment = 1

else:
    payment = float(input("Enter how much you will save each period: "))
    while (payment <= 0):
        payment = (float(input("Please enter a positive value: ")))

numRemainingPayments = balance/payment

# calculate number of payments
print("You must make", numRemainingPayments, "more payments.")

# present information to user