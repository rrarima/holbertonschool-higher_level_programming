#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dict2 = {};
for (const key in dict) {
  if (dict2[dict[key]] === undefined) {
    dict2[dict[key]] = [key];
  } else {
    dict2[dict[key]].push(key);
  }
}
console.log(dict2);
