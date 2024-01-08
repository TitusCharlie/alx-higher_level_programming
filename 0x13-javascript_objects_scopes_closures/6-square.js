#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  constructor(size) {
    // Call the constructor of the base class (Square)
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
      // Default to 'X' if c is undefined
      c = 'X';
    }

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareWithCharPrint;

