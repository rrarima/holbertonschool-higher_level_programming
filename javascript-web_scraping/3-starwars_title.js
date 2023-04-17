#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';
const idNumber = process.argv[2];

request(`${URL}${idNumber}`, (err, res, body) => {
  if (err) return console.log(err);
  if (res.statusCode !== 200) return console.log(`code: ${res.statusCode}`);
  console.log(JSON.parse(body).title);
});
