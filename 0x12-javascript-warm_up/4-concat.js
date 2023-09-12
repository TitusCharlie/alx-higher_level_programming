#!/usr/bin/node

const arg1 = 'undefined';
const arg2 = 'undefined';

if (process.argv[2] && process.argv[3]) {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
} else {
  console.log(`${arg1} is ${arg2}`);
}
