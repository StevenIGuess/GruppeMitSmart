wordlist.txt was created by the following command

cat /usr/share/dict/web2a | tr ' ' '\n' | tr '-' '\n' | sort -u | grep -v '^$'

where /usr/share/dict/web2a is the file from macos 10.15.7
