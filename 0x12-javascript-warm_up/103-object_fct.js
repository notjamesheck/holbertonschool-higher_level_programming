#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function foo () {
  this.value = this.value + 1;
}
myObject.incr = foo;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
