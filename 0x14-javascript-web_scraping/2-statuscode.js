#!/usr/bin/node
// comment

const path = process.argv[2];

let req = require('request');

req({ uri: path, method: 'GET' }, function (error, response, body) {
  if (error) throw error;
  console.log(`code: ${response.statusCode}`);
});
