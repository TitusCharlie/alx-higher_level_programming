#!/usr/bin/node

const request = require('request');
const process = require('process');

if (process.argv.length !== 3) {
    console.log('Usage: ./3-starwars_title.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
    if (error) {
        console.log('Error:', error);
    } else {
        const data = JSON.parse(body);
        console.log(data.title);
    }
});