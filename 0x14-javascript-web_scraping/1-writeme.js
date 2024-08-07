#!/usr/bin/node

const fs = require('fs');
const process = require('process');

if (process.argv.length !== 4) {
    console.log('Usage: ./1-writeme.js <file_path> <content>');
    process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.log(err);
    }
});