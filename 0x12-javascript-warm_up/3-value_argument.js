#!/usr/bin/node
const element = process.argv[2];
if (element === undefined) {
  console.log('No argument');
} else {
  console.log(element);
}
