// Task - H
function getPositive(data) {
    arr = []
    for (let n of data) {
        if (n >= 0) arr.push(n)
    }
    return arr.join("")
}

console.log(getPositive([1, -4, 2]))



// TASK - G
/*
function getHighestIndex(numbers) {
    temp = numbers[0]
    highest_index = 0
    for (let i in numbers) {
        if (numbers[i] > temp) {
            highest_index = i 
            temp = numbers[i]
        }
    }
    return highest_index
}

console.log(getHighestIndex([44, 5, 21, 100, 12, 21, 8, 22]))
*/


// TASK - F
/*
function findDoublers(data) {
    let start_index = 0
    for (let i in data) {
        for (let j in data) {
            if (i === j) continue
            if (data[i] === data[j]) return true
        }
    }
    return false
}
console.log(findDoublers("hello"));
*/


// TASK - E
/*
function getReverse(data) {
    return data.split("").reverse().join("");
}

console.log(getReverse("muzaffar"));
*/