#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) return console.error(error);
  if (response.statusCode !== 200) return console.error(`Status code ${response.statusCode}`);

  const tasks = JSON.parse(body);
  const completedTasksByUser = tasks.reduce((acc, task) => {
    if (task.completed) {
      const userId = task.userId;
      acc[userId] = (acc[userId] || 0) + 1;
    }
    return acc;
  }, {});

  console.log(completedTasksByUser);
});
