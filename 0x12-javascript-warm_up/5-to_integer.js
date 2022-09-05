#!/usr/bin/node
const toInt = parseInt(process.argv[2]);
if (isNaN(toInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + toInt);
}
