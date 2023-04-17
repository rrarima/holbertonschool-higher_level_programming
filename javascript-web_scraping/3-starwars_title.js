#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';
const idNumber = process.argv[2];

request(URL + idNumber, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
