// Zelle Ch 6 addInterest program translated to JS:

const addInterest = (balances, intRate) => {
    const newBalances = []
    for (const acct of balances) {
        newBalances.push(acct * (1 + intRate))
    }
    return newBalances
}

const test2 = () => {
    const amounts = [1000, 2200, 800, 360];
    const rate = 0.05;
    const updatedBalances = addInterest(amounts, rate);
    for (const balance in updatedBalances) {
        let newBalance = updatedBalances[balance]
        console.log(newBalance.toFixed(2))
    }
}

const addInterestOrig = (balance, intRate) => {
    let newBalance = balance * (1 + intRate)
    return newBalance
}

const test1 = () => {
    const amount = 1000
    const rate = 0.05
    updatedBalance = addInterestOrig(amount, rate)
    console.log(updatedBalance.toFixed(2))
}

console.log("test1:")
test1()
console.log("test2:")
test2()