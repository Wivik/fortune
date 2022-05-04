#!/usr/bin/env bash

## run fortune, store the message, and cowsay it in various way

message=$(mktemp)
mypath=$(dirname $0)

fortune > $message

cat $message | cowsay > ${mypath}/cowsay.txt
cat $message | cowsay -f tux > ${mypath}/tuxsay.txt

rm $message

## execute the python script

/usr/bin/env python3 ${mypath}/fortune.py

## cleanup the mess

rm ${mypath}/cowsay.txt
rm ${mypath}/tuxsay.txt
