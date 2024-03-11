#!/usr/bin/node
const nn = parseInt(process.argv[2]);
const x = 'C is fun';
if (!nn) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nn; i++) {
    console.log(x);
  }
}
