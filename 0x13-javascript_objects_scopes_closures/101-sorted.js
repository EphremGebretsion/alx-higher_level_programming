#!/usr/bin/node
const mydict = require('./101-data.js').dict;
const resdict = {};
for (const key in mydict) {
  const newkey = mydict[key];
  if (!(newkey in resdict)) {
    resdict[newkey] = [];
  }
  resdict[newkey].push(key);
}
console.log(resdict);
