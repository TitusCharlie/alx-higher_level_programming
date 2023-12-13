#!/usr/bin/node

function factorial (number) {
  if (number < 1 || isNaN(number)) {
    return 1;
  } else {
    return factorial(number - 1) * number;
  }
}

const numberInt = parseInt(process.argv[2]);
console.log(factorial(numberInt));
