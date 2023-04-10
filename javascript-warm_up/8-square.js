#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
