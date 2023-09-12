#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 && arg2) {
  console.log(`${arg1} is ${arg2}`);
} else {
  const arg1 = 'undefined';
  const arg2 = 'undefined';
  console.log(`${arg1} is ${arg2}`);
}
