#!/usr/bin/node
let Box = process.argv;
if (Box.length <= 3) {
	console.log(0);
} else {
	console.log(Box.sort().reverse()[1]);
}
