#!/usr/bin/node
/* prints a message depending
on the number of arguments passed */

let myVar = process.argv.length;
if (myVar === 3) {
  console.log('Argument found');
} else if (myVar > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
