#!/usr/bin/node

const request = require('request');
const process = require('process');

if (process.argv.length !== 3) {
    console.log('Usage: ./2-statuscode.js <URL>');
    process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response) => {
    if (error) {
        console.log('Error:', error);
    } else {
        console.log('code:', response.statusCode);
    }
});