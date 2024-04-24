#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
req.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const respObj = JSON.parse(body);
  console.log(respObj.films.length);
});
