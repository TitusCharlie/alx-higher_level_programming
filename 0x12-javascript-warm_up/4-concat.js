#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 && arg2) {
  console.log(`${arg1} is ${arg2}`);
} else {
  let arg1 = 'undefined';
  let arg2 = 'undefined';
  console.log(`${arg1} is ${arg2}`);
}
