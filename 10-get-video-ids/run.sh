#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../scripts

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

mkdir -p $DIR/data

python3 $DIR/../scripts/10_get_video_ids.py --topic_tree_url "https://www.khanacademy.org/api/v1/topictree" --topic_tree_backup $DIR"/data/topic_tree.json" --youtube_ids_backup $DIR"/data/youtube_ids"
