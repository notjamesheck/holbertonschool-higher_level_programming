#!/usr/bin/node
// comment

const ep = `http://swapi.co/api/films/${process.argv[2]}`;

let req = require('request');

req({ uri: ep, method: 'GET', json: true }, function (error, response, body) {
  if (error) throw error;
  console.log(body.title);
});
