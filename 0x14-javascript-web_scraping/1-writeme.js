#!/usr/bin/node
// comment

const fs = require('fs');

let file = process.argv[2];

let text = process.argv[3];

fs.writeFile(file, text, (err) => {
  if (err) throw err;
});
