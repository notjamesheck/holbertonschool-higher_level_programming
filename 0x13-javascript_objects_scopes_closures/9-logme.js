#!/usr/bin/node
// prints the number of argument already printed

let cntr = 0;

exports.logMe = function (a = '') {
  console.log(`${cntr}: ${a}`);
  return cntr++;
};
