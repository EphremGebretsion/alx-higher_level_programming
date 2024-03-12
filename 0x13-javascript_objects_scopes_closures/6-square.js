#!/usr/bin/node
const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c) {
    let ch = c;
    let row = '';
    if (!c) { ch = 'X'; }
    for (let i = 0; i < this.height; i++) { row += ch; }
    for (let h = 0; h < this.height; h++) { console.log(row); }
  }
};
