const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let sumVal = 0;

for (let i = 1; i < input.length; i++) {
    if (input[i] % 2 != 0 && input[i] % 3 == 0) {
        sumVal += Number(input[i]);
    }
}

console.log(sumVal);