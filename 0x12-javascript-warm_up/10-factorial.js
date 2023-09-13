#!/usr/bin/node

function factorial (number) {
  if (number === 0) {
    return 1;
  } else {
    return factorial(number - 1) * number;
  }
}

const numberInt = parseInt(process.argv[2]);
if (!isNaN(numberInt)) {
  const result = factorial(numberInt);
  console.log(result);
} else {
  console.log('NaN');
}
