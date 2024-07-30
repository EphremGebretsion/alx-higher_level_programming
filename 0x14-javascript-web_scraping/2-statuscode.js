#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
