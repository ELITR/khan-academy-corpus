#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../scripts

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

mkdir -p $DIR/data

python3 $DIR/../scripts/21_strip_subtitles.py --video_path $DIR/../11-download/data --subtitle_path $DIR/data
