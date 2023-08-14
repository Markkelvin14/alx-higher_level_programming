#!/usr/bin/node
const element = process.argv[2];
if (isNaN(element)) {
  console.log('Not a number');
} else {
  console.log('My number:', element | 0);
}
