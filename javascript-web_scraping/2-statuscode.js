#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res) => {
  console.log(err || `code: ${res.statusCode}`);
});
