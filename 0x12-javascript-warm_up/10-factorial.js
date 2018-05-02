#!/usr/bin/node
// comment

var num = parseInt(process.argv[2]);

var factorial = function (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

console.log(factorial(num));
