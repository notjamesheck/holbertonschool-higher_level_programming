#!/usr/bin/node
// prints '''x''' times “C is fun”

let x = parseInt(process.argv[2]);
if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
