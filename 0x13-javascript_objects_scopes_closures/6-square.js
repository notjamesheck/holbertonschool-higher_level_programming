#!/usr/bin/node
// extends method to square object

const S = require('./5-square');

class Square extends S {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(Array(this.width + 1).join(c));
    }
  }
}

module.exports = Square;
