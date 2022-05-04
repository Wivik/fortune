#!/usr/bin/env bash

## run fortune, store the message, and cowsay it in various way

message=$(mktemp)

fortune > $message

cat $message | cowsay > cowsay.txt
cat $message | cowsay -f tux > tuxsay.txt

rm $message

## execute the python script

/usr/bin/env python3 fortune.py

## cleanup the mess

rm cowsay.txt
rm tuxsay.txt
