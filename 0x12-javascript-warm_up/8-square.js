#!/usr/bin/node
// script that prints a square

let x = parseInt(process.argv[2]);
if (!x) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log(Array(x + 1).join('x'));
  }
}
