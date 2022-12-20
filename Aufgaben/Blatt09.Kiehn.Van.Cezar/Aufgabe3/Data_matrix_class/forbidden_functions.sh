#!/bin/sh
# grep '^def' data_matrix.py | sed -e 's/^def //' -e 's/(.*//' > .forbidden.txt
grep -wqf forbidden.txt data_matrix_class.py
if test $? -ne 1
then
  echo "$0: data_matrix_class.py possibly calls one of the functions in forbidden.txt, while it is supposed to only use the methods of class DataMatrix"
  exit 1
fi
