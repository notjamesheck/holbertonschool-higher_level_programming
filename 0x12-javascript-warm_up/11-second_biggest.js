#!/usr/bin/node
// comment

let len = process.argv.length;

function second (len) {
  let arr = [];
  for (let i = 2; i < len; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort();
  return (arr[1]);
}

if (len < 4) {
  console.log(0);
} else {
  console.log(second(len));
}
