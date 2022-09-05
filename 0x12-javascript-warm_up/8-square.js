#!/usr/bin/node
const square = parseInt(process.argv[2]);
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    console.log('X'.repeat(square));
  }
}
