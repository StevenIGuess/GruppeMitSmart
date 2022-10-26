#!/bin/bash
cat alignments.sam | tail -n +4 | cut -f 3 | grep -v "*" | sort -u