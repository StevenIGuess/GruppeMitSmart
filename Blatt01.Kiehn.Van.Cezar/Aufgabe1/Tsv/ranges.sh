#!/bin/bash
cat islands.tsv | tail -n +2 | cut -f 1,2 | sort -n -u