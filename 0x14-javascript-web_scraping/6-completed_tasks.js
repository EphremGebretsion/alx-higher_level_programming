#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req.get(url, (err, resp, body) => {
  if (err) { return; }
  const bodyObj = JSON.parse(body);
  const counts = {};
  bodyObj.forEach((element) => {
    const key = element.userId.toString();
    if (!(key in counts)) { counts[key] = 0; }
    if (element.completed) { counts[key]++; }
  });
  console.log(counts);
});
