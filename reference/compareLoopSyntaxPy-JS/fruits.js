const fruits = ["apple", "banana", "cherry"];

for (let eachFruit in fruits) {
    // eachFruit represents the index number
	console.log(fruits[eachFruit])
}

for (let eachFruit = 0; eachFruit < fruits.length; eachFruit++) {
    // eachFruit represents the index number
    console.log(fruits[eachFruit])
}

fruits.map((eachFruit) => {
    // eachFruit represents the ITEM AT the index, like in python for loop
    console.log(eachFruit)
})

// RESULTS (for all 3):
// apple
// banana
// cherry