#!/usr/bin/node
function factorial (x) {
  if (!x) { return (1); }
  if (x === 1 || x === 0) {
    return (1);
  } else {
    if (x > 0) {
      return (x * factorial(x - 1));
    }
  }
}
const nn = factorial(parseInt(process.argv[2]));
console.log(nn);
