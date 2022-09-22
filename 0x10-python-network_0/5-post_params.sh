#!/bin/bash
#variable email to test@gmail.com, subject to will be here for PLD
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
