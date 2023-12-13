#!/usr/bin/node

const firstArg = process.argv[2];
const intValue = parseInt(firstArg, 10);

if (!isNaN(intValue)) {
  console.log(`My number: ${intValue}`);
} else {
  console.log('Not a number');
}
