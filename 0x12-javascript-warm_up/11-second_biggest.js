#!/usr/bin/node
// comment

let len = process.argv.length;

function second (len) {
  let arr = [];
  for (let i = 2; i < len; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr.sort();
  return (arr[`${arr.length - 2}`]);
}

if (len < 4) {
  console.log(0);
} else {
  console.log(second(len));
}
