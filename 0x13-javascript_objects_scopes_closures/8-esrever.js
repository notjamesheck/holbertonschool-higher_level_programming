#!/usr/bin/node
// returns the reversed version of a list
// https://alligator.io/js/slice-vs-splice/

exports.esrever = function (list) {
  for (let i = 0; i < list.length - 1; i++) {
    // inserts elem. at i, no elem. removed
    list.splice(i, 0, list.pop());
  }
  return list;
}
;
