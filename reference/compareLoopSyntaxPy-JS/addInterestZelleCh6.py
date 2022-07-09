def addInterest(balances, intRate):
    for acct in range(len(balances)):
        balances[acct] = balances[acct] * (1+intRate)
    return balances

def addInterestOrig(balance, intRate):
    newBalance = balance * (1+intRate)
    return newBalance

def test1():
    amount = 1000
    rate = 0.05
    updatedBalance = addInterestOrig(amount, rate)
    print("{:.2f}".format(updatedBalance))

def test2():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    updatedBalances = addInterest(amounts, rate)
    for balance in range(len(updatedBalances)):
        newBalance = updatedBalances[balance]
        print("{:.2f}".format(newBalance))

print("test1:")
test1()
print("test2:")
test2()