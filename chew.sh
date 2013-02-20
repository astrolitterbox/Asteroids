#!/bin/sh
# generate csv out of html table

cat index.html.table | \
    sed -e :a -e 's/<[^>]*>//g;/</N;//ba' | \
    sed 's/^[ \t]*//' | \
    sed '$!N; /^\(.*\)\n\1$/!P; D' | \
    sed 's/$/,/; s/^,$//' | \
    sed ':a;N;$!ba;s/,\n/,/g' | \
    sed 's/,$//' > nasa.csv
