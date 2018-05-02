#!/usr/bin/node
// call a function x times

exports.callMeMoby = function (x, theFunction) {
  for (; x > 0; x--) {
    theFunction();
  }
};
