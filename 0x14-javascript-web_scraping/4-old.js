#!/usr/bin/node
const req = require('request');
const url = process.argv[2] + '/';
const charURL = 'https://swapi-api.alx-tools.com/api/people/18/';
req.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const respObj = JSON.parse(body);
  let count = 0;
  const last = respObj.count;
  for (let i = 0; i < last; i++) {
    if (respObj.results[i].characters.includes(charURL)) { count++; }
  }
  console.log(count);
});
