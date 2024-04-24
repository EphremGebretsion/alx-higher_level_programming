#!/usr/bin/node
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
req.get(url, (err, resp, body) => {
  if (err) { return; }
  fs.writeFile(fileName, body, 'utf8', (ferr) => {
    if (ferr) {
      console.log(ferr);
    }
  });
});
