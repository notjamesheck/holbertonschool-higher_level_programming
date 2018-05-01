#!/usr/bin/node
// comment

let myVar = process.argv.length;
if (myVar === 3) {
  console.log('Argument found');
} else if (myVar > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
