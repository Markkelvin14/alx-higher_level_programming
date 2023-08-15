#!/usr/bin/node
const Num = parseInt(process.argv[2]);
function factorial (Num) {
  if (Num === 1 || isNaN(Num)) {
    return (1);
  } else {
    return (Num * factorial(Num - 1));
  }
}
console.log(factorial(Num));
