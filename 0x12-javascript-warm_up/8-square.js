#!/usr/bin/node
let Num = process.argv[2];
if (isNaN(Num)) {
  console.log('Missing size');
} else {
  for (let m = 0; m < Num; m++) {
    console.log('X'.repeat(Num));
  }
}
