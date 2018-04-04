#!/bin/bash
# cURL POST parameters
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -Xs POST "$1"
