#!/usr/bin/node

const x = process.argv[2];
const intValue = parseInt(x, 10);

if (!isNaN(intValue)) {
  for (let i = 0; i < intValue; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
