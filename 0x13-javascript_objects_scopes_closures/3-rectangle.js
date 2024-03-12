#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let w = 0; w < this.width; w++) {
      row += 'X';
    }
    for (let h = 0; h < this.height; h++) {
      console.log(row);
    }
  }
};
