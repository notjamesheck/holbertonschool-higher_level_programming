#!/usr/bin/node
// comment

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

function add (a, b) {
  console.log(`${a + b}`);
}
add(a, b);
