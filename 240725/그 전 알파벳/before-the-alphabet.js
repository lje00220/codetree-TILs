const fs = require("fs");
let input = fs.readFileSync(0).toString().trim();

if (input === "a") {
    console.log("z");
} else {
    input = String.fromCharCode(input.charCodeAt(0) - 1);
    console.log(input);
}