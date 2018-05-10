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
}

module.exports = Rectangle;
