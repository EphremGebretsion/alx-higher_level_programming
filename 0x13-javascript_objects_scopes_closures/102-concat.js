#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
let file1;
let file2;
fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  file1 = data;
  fs.readFile(args[3], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    file2 = data;
    const concat = file1 + file2;
    fs.writeFile(args[4], concat, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
