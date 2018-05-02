#!/usr/bin/node
/* prints two arguments passed to it,
 in the following format: arg “is” arg */

let a = process.argv[2];
let b = process.argv[3];
console.log(`${a} is ${b}`);
