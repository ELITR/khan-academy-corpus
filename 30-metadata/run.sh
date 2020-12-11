#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../scripts

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

mkdir -p $DIR/data

python3 $DIR/../scripts/30_metadata.py --topic_tree_backup $DIR/../10-get-video-ids/data/topic_tree.json --output_path $DIR/data
