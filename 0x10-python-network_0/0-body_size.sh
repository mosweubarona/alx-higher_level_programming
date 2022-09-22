#!/bin/bash
#display size of url body
curl -sI "$1" | grep 'Content-Length:' | cut -d ' ' -f2
