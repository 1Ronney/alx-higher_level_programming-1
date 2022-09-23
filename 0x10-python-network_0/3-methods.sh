#!/usr/bin/env bash
# This is a Bash script that takes in a URL and
# displays all HTTP methods the server will accept.
curl -X OPTIONS -sI "$1" | grep "Allow" | tr ':' '\n' | tail -1
