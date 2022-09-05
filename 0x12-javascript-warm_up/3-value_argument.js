#!/usr/bin/node
const Arg = process.argv[2];
if (Arg === undefined) {
  console.log('No argument');
} else {
  console.log(Arg);
}
