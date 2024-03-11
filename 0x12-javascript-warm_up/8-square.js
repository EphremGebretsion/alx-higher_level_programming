#!/usr/bin/node
const nn = parseInt(process.argv[2]);
if (!nn) {
  console.log('Missing size');
} else {
  let column = '';
  for (let i = 0; i < nn; i++) {
    column += 'X';
  }
  for (let i = 0; i < nn; i++) {
    console.log(column);
  }
}
