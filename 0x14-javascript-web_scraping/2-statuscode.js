#!/usr/bin/node
// comment

const url = process.argv[2];

let req = require('request');

req(url, function (err, response, body) {
  if (err) throw err;
  console.log('code: ', response.statusCode);
});
