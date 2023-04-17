#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) return console.log(err);
  if (response.statusCode !== 200) { return console.log(`code: ${response.statusCode}`); }
  const { results: films } = JSON.parse(body);
  const count = films.reduce(
    (sum, { characters }) =>
      sum + characters.filter((char) => char.includes('18')).length,
    0
  );
  console.log(count);
});
