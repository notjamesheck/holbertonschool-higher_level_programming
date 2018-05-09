#!/usr/bin/node
// prints the number of argument already printed

exports.logMe = function (item) {
  let i = 0;
  function poop (item) {
    function poop (i) {
      console.log(`${i++}: ${item}`);
      return i++;
    }
    console.log(i);
    return poop(i);
  }
  console.log(i);
  return poop(item);
};
