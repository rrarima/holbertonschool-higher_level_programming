#!/usr/bin/node
const fs = require('fs');
console.log(fs.readFileSync(process.argv[2], 'utf8'));
