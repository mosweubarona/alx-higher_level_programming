#!/bin/bash
#header variable X-School must be sent with the value 98
curl -s "$1" -X GET -H "X-School-User-Id: 98"
