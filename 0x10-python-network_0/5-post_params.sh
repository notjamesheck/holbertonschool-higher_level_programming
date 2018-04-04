#!/bin/bash
# cURL POST parameters
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -sH "Content-Type: application/x-www-form-urlencoded" -sX POST "$1"
