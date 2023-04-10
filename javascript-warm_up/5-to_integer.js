#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log(`My Number: ${num}`);
}
