#!/bin/sh

set -e -x

./quersumme.py 123
./quersumme.py -99
./quersumme.py ' -99'
./quersumme.py '-200 '
./quersumme.py +1234
./quersumme.py '   +1234 '
./quersumme.py '+1234 '
./quersumme.py ' 1235'
./quersumme.py '1235 '
