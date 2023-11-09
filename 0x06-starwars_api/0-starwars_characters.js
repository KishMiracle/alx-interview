#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
let actors = [];
const names = [];

const queryCharacters = async () => {
  await new Promise(resolve => request(API_URL, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      actors = jsonBody.characters;
      resolve();
    }
  }));
};

const queryNames = async () => {
  if (actors.length > 0) {
    for (const ac of actors) {
      await new Promise(resolve => request(ac, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No Charcter Found');
  }
};

const getCharNames = async () => {
  await queryCharacters();
  await queryNames();

  for (const n of names) {
    if (n === names[names.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames();
