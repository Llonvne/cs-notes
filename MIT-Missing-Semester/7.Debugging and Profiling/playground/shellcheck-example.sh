#!/bin/bash
# Example: a refactored script following ShellCheck recommendations

for f in ./*.m3u
do
  if grep -qi "hq.*mp3" "$f"; then
    echo "Playlist $f contains a HQ file in mp3 format"
  fi
done
