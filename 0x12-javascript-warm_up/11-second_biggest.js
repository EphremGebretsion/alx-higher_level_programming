#!/usr/bin/node
const list = process.argv;
let i = 2;
let secondBigest;
let bigest;
if (list.length < 4 || !parseInt(list[2])) {
  console.log(0);
} else {
  for (bigest = parseInt(list[2]); list[i]; i++) {
    if (parseInt(list[i]) > bigest) { bigest = parseInt(list[i]); }
  }
  secondBigest = parseInt(list[2]);
  if (parseInt(list[2]) === bigest) {
    secondBigest = parseInt(list[3]);
  }
  for (let j = 2; list[j]; j++) {
    const temp = parseInt(list[j]);
    if (temp !== bigest && temp > secondBigest) {
      secondBigest = temp;
    }
  }
  console.log(secondBigest);
}
