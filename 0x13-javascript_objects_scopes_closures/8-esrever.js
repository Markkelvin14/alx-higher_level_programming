#!/usr/bin/node
exports.esrever = function (list) {
  const NewList = [];
  for (let m = 0; m < list.length; m++) {
    NewList.unshift(list[m]);
  }
  return NewList;
};
