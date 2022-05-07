#!/usr/bin/env bash

## run fortune, store the message, and cowsay it in various way

message=$(mktemp)
mypath=$(dirname $0)
day=$(date +"%d")
month=$(date +"%m")
# day="20"
# month="09"
## generate today's fortune

fortune > $message

## we adapt the cowsay file according to a date
case $day$month in
    "0405") cat $message | cowsay -f vader > ${mypath}/cowsay.txt; cat $message | cowsay -f vader > ${mypath}/tuxsay.txt ;;
    "2305") cat $message | cowsay -f turtle > ${mypath}/cowsay.txt; cat $message | cowsay -f turtle > ${mypath}/tuxsay.txt ;;
    "0106") cat $message | cowsay -f supermilker > ${mypath}/cowsay.txt; cat $message | cowsay -f supermilker > ${mypath}/tuxsay.txt ;;
    "0607") cat $message | cowsay -f kiss > ${mypath}/cowsay.txt; cat $message | cowsay -f kiss > ${mypath}/tuxsay.txt ;;
    "0808") cat $message | cowsay -f meow > ${mypath}/cowsay.txt; cat $message | cowsay -f meow > ${mypath}/tuxsay.txt ;;
    "1008") cat $message | cowsay -f moofasa > ${mypath}/cowsay.txt; cat $message | cowsay -f moofasa > ${mypath}/tuxsay.txt ;;
    "2009") cat $message | cowsay -f head-in > ${mypath}/cowsay.txt; cat $message | cowsay -f head-in > ${mypath}/tuxsay.txt ;;
    "3110") cat $message | cowsay -f skeleton > ${mypath}/cowsay.txt; cat $message | cowsay -f skeleton > ${mypath}/tuxsay.txt ;;
    *) cat $message | cowsay > ${mypath}/cowsay.txt; cat $message | cowsay -f tux > ${mypath}/tuxsay.txt ;;
esac

# if [ "$day$month" = "0405" ]; then
#     cat $message | cowsay -f vader > ${mypath}/cowsay.txt
#     cat $message | cowsay -f vader > ${mypath}/tuxsay.txt
# elif [ "$day$month" = "0808" ]; then
#     cat $message | cowsay -f skeleton > ${mypath}/cowsay.txt
#     cat $message | cowsay -f skeleton > ${mypath}/tuxsay.txt
# elif [ "$day$month" = "31" ] && [ "$month" = "10" ]; then
#     cat $message | cowsay -f skeleton > ${mypath}/cowsay.txt
#     cat $message | cowsay -f skeleton > ${mypath}/tuxsay.txt
# else
#     cat $message | cowsay > ${mypath}/cowsay.txt
#     cat $message | cowsay -f tux > ${mypath}/tuxsay.txt
# fi
rm $message

## execute the python script to generate the web pages and the rss feed

/usr/bin/env python3 ${mypath}/fortune.py

## cleanup the mess

rm ${mypath}/cowsay.txt
rm ${mypath}/tuxsay.txt
