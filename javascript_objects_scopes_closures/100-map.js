#!/usr/bin/node
const array1 = require('./100-data.js').list;
console.log(array1);
console.log(array1.map((element, index) => element * index));
