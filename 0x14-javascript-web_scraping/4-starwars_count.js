#!/usr/bin/node
// comment

const ep = process.argv[2];

const wA = 'https://swapi.co/api/people/18/';

let req = require('request');

req({ uri: ep, method: 'GET', json: true }, function (error, response, body) {
  if (error) throw error;
  let c = 0;
  for (let i = 0; i < body.results.length - 1; i++) {
    c += body.results[i].characters.filter(function (val) {
      return val === wA;
    }).length;
  }
  console.log(c);
});
