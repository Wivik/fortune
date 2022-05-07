#!/usr/bin/env bash

## run fortune, store the message, and cowsay it in various way

message=$(mktemp)
now=$(date +"%s")
mypath=$(dirname $0)

## generate today's fortune

fortune > $message

cat $message | cowsay > ${mypath}/cowsay.txt
cat $message | cowsay -f tux > ${mypath}/tuxsay.txt

rm $message

## execute the python script to generate the web pages and the rss feed

/usr/bin/env python3 ${mypath}/fortune.py

## cleanup the mess

rm ${mypath}/cowsay.txt
rm ${mypath}/tuxsay.txt
