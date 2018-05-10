#!/usr/bin/node
// comment

let f = require('fs');

let path = process.argv[2];

let string = process.argv[3];

f.writeFile(path, string, 'utf-8', function (error) {
  if (error) throw error;
});
