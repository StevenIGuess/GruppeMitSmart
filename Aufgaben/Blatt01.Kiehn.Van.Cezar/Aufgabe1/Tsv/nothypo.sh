#!/bin/bash
cat islands.tsv | tail -n +2 | grep -v "hypothetical protein"