#!/usr/bin/node

const inputDict = require('./101-data').dict;

// Function to swap keys and values in a dictionary
function swapKeysAndValues (obj) {
  const result = {};
  for (const key in obj) {
    const value = obj[key];
    if (!result[value]) {
      result[value] = [key];
    } else {
      result[value].push(key);
    }
  }
  return result;
}

const outputDict = swapKeysAndValues(inputDict);

console.log(outputDict);
