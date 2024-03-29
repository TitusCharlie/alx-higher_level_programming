#!/usr/bin/node

// array of numbers

let largestNum = parseInt(process.argv[2]);
let secLargest = parseInt(process.argv[2]);

function secondLargest () {
  if (process.argv.length < 4) {
    console.log(0);
    return;
  }

  // pick two numbers in the array
  for (let i = 3; i < process.argv.length; i++) {
    const currentNum = parseInt(process.argv[i]);
    if (currentNum > secLargest) {
      secLargest = currentNum;
      if (currentNum > largestNum) {
        secLargest = largestNum;
	largestNum = currentNum;
      }
    }
  }

  console.log(secLargest);
}

//print the output
secondLargest();

