#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../scripts

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

mkdir -p $DIR/data

python3 $DIR/../scripts/31_statistics.py --video_metadata_path $DIR/../30-metadata/data/video_metadata.json --output_path $DIR/data
