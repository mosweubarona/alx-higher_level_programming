#!/bin/bash
#  sends a request to a URL passed as an argumen
curl -sI -w '%{response_code}' "$1" -o /dev/null
