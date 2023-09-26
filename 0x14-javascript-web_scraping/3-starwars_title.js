#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const episode = process.argv[2];
request(url + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Try again');
  }
});
