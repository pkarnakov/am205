#!/bin/sh -eu

run () {
  rate=25
  dirname=$1
  output=pcavideo_${dirname}.mp4
  if [ -f "$output" ] ; then
    echo "skip existing '$output'"
    return
  fi
  cmd="ffmpeg -y -v error -framerate $rate -r $rate -i '$dirname/a_%05d.png' -c:v libx264 -vf format=yuv420p '$output'"
  echo "$cmd"
  eval "$cmd"
}

run paris
run paris_first3
run paris_zero3

run sunrise
run sunrise_first3
run sunrise_zero3

run vietnam
run vietnam_first3
run vietnam_zero3
