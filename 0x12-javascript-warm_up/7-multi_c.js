#!/usr/bin/node
let countNo = Number(process.argv[2]);
if (isNaN(countNo)) {
  console.log('Missing Number of occurrences');
} else if (countNo > 0) {
  for (countNo; countNo > 0; --countNo) {
    console.log('C is fun');
  }
}
