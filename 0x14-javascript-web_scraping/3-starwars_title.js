#!/usr/bin/node
const req = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID + '/';
req.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const respObj = JSON.parse(body);
  console.log(respObj.title);
});
