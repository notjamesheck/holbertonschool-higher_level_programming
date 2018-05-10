#!/usr/bin/node
// comment

const url = `${process.argv[2]}`;
var request = require('request');
request(url, function (error, response, body) {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
