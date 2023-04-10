#!/usr/bin/node

function factorial (n) {
    return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

const args = process.argv.slice(2);
const input = Number(args[0]);

console.log(factorial(input));
