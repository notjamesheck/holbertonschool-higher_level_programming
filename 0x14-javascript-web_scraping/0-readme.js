#!/usr/bin/node
// comment

let f = require('fs');
f.readFile(`${process.argv[2]}`, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
