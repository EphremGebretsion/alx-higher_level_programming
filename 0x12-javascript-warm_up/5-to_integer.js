#!/usr/bin/node
const nn = parseInt(process.argv[2]);
if (nn) {
  console.log('My number:', nn);
} else {
  console.log('Not a number');
}
