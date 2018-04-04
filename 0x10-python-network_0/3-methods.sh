#!/bin/bash
# cURL only methods
curl -sI "$1" | grep "Allow: " | cut -d" " -f2-4 | tr-d "\r"
