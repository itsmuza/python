// TASK - F
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


// TASK - E
/*
function getReverse(data) {
    return data.split("").reverse().join("");
}

console.log(getReverse("muzaffar"));
*/