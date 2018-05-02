#!/usr/bin/node
/* prints My number: "" if the
first argument can be converted to an integer */

let a = parseInt(process.argv[2]);
if (isNaN(a)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${a}`);
}
