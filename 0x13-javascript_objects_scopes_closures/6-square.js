#!/usr/bin/node
const Presquare = require('./5-square');
class Square extends Presquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let m = 0; m < this.width; m++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
