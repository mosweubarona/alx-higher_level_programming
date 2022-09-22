#!/bin/bash
#header variable X-School-User-Id must be sent with the value 98
curl -sX GET -H 'X-Schoo-User-Id:98' "$1"
