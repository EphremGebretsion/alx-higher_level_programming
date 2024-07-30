#!/usr/bin/node
const req = require('request');
const moviID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + moviID + '/';
req.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const bodyObj = JSON.parse(body);
  const characters = bodyObj.characters;
  for (let i = 0; i < characters.length; i++) {
    req.get(characters[i], (err, resp, body) => {
      if (err) { return; }
      console.log(JSON.parse(body).name);
    });
  }
});
