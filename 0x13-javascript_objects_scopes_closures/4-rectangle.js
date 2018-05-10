#!/usr/bin/node
// create Rectangle class
// https://stackoverflow.com/questions/42684177/node-js-es6-classes-with-require

class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log(Array(this.width + 1).join('X'));
    }
  }

  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
