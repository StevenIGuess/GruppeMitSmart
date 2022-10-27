#!/bin/bash
./references.sh | cat > references.tmp && cat alignments.sam | tail -n +4 | grep -f references.tmp | cat && rm references.tmp