#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (err, res, body) {
  if (err) return console.log(err);
  if (res.statusCode !== 200) return console.log(`code: ${res.statusCode}`);
  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) return console.log(err);
  });
});
