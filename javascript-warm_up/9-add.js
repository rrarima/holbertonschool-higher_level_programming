#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const args = process.argv.slice(2);
const sum = add(args[0], args[1]);

console.log(sum);
