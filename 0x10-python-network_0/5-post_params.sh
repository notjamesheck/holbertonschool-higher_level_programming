#!/bin/bash
# cURL POST parameters
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -H "Content-Type: application/x-www-form-urlencoded" -X POST "$1"
