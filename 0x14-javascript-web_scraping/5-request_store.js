#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const process = require('process');

if (process.argv.length !== 4) {
    console.log('Usage: ./5-request_store.js <URL> <file_path>');
    process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
    if (error) {
        console.log('Error:', error);
    } else {
        fs.writeFile(filePath, body, 'utf-8', (err) => {
            if (err) {
                console.log('Error:', err);
            }
        });
    }
});