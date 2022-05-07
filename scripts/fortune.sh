#!/usr/bin/env bash

## run fortune, store the message, and cowsay it in various way

message=$(mktemp)
now=$(date +"%s")
mypath=$(dirname $0)

## Create the history path if missing

if [ ! -d "${mypath}/histo" ]; then
    mkdir ${mypath}/histo
fi

## Purge older messages than ten days

find ${mypath}/histo -type f -mtime +10

## generate today's fortune

fortune > $message

cat $message | cowsay > ${mypath}/cowsay.txt
cat $message | cowsay -f tux > ${mypath}/tuxsay.txt

rm $message

## Copy them to the histo folder for the rss feed

cp ${mypath}/cowsay.txt ${mypath}/histo/cowsay_${now}.txt
cp ${mypath}/tuxsay.txt ${mypath}/histo/tuxsay_${now}.txt

## execute the python script to generate the web pages and the rss feed

/usr/bin/env python3 ${mypath}/fortune.py

## cleanup the mess

rm ${mypath}/cowsay.txt
rm ${mypath}/tuxsay.txt
