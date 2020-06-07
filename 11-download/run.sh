#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

YOUTUBE_IDS_FILE=$DIR"/../10-get-video-ids/data/youtube_ids"

#$DIR/batch.sh < $YOUTUBE_IDS_FILE

head -n3 < $YOUTUBE_IDS_FILE
