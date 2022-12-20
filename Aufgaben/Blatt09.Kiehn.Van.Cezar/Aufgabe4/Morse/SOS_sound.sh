#!/bin/sh
OS=`uname -s`
if test "X${OS}Y" = "XDarwinY"
then
  SOUNDPLAYER=afplay
else
  if test "X${OS}Y" = "XLinuxY"
  then
    SOUNDPLAYER=aplay
  else
    echo "$0: unknown operating system ${OS}"
    exit 1
  fi
fi
${SOUNDPLAYER} dah.wav
${SOUNDPLAYER} dah.wav
${SOUNDPLAYER} dah.wav
${SOUNDPLAYER} dit.wav
${SOUNDPLAYER} dit.wav
${SOUNDPLAYER} dit.wav
${SOUNDPLAYER} dah.wav
${SOUNDPLAYER} dah.wav
${SOUNDPLAYER} dah.wav
