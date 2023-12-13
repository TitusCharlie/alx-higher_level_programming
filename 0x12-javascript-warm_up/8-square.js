#!/usr/bin/node

const size = process.argv[2];
const sizeInt = parseInt(size, 10);

if (!isNaN(sizeInt)) {
  for (let column = 0; column < sizeInt; column++) {
    for (let row = 0; row < sizeInt; row++) {
      process.stdout.write('X');
    } console.log();
  }
} else {
  console.log('Missing size');
}
